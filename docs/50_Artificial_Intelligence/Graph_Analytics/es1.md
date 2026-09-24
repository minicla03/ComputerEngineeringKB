## 1. Specifiche di Dominio: "Surgical-Data-Ops"

1.  **Entità RawData**: Rappresenta i video originali acquisiti in sala operatoria. Ogni video ha un `hospital_origin` e una `resolution`.
2.  **Entità Frame**: Un video è composto da migliaia di frame. Ogni frame ha un `timestamp` relativo al video e un `brightness_score`.
3.  **Entità Dataset**: I frame vengono raggruppati in Dataset (es. "HemoSet_v1"). Un dataset ha uno `purpose` (Training, Validation, Test).
4.  **Entità Annotation**: Ogni frame può avere più annotazioni (es. "Artery", "Blood_Pool"). L'annotazione è creata da un **Annotator** (un medico) e ha una `bounding_box` (array di coordinate) e un `confidence_score`.
5.  **Vincoli di Integrità**:
    * Un `Frame` appartiene a uno e un solo `Video`.
    * Un `Frame` può far parte di più `Dataset` (data reuse).
    * Un `Annotator` è identificato univocamente da una `license_id`.

---

```mermaid
graph LR
    classDef RawData;
    classDef Frame;
    classDef Dataset;
    classDef Annotation;
    classDef Annotator;

    RawData -- "[:COMPOSED_BY]" -- Frame
    Frame -- "[:GROUPED]" -- Dataset
    Frame -- "[:HAVE]" -- Annotation 
    Annotation -- "[:CREATED_BY]" -- Annotator

    class RawData RawData;
    class Frame Frame;
    class Dataset Dataset;
    class Annotation Annotation;
    class Annotator Annotator;
```

## 2. Alimentazione del Database (Cypher)

Esegui questo script per creare l'infrastruttura di base.

```cypher
// Creazione Video e Frame
CREATE (v1:Video {id: "VID_001", hospital: "Gemelli", duration_sec: 120})
CREATE (f1:Frame {id: "F_001", timestamp: 10.5, quality: "High"})
CREATE (f2:Frame {id: "F_002", timestamp: 10.6, quality: "High"})

// Creazione Dataset
CREATE (ds:Dataset {name: "HemoSet_2026", version: "1.0", status: "Draft"})

// Creazione Annotatori
CREATE (a1:Annotator {license_id: "MED_99", name: "Dr. Bianchi", seniority: "Senior"})

// Relazioni iniziali
CREATE (f1)-[:EXTRACTED_FROM]->(v1)
CREATE (f2)-[:EXTRACTED_FROM]->(v1)
CREATE (f1)-[:INCLUDED_IN]->(ds)
```

---

## 3. Task di Modellazione e Querying

### Task 1: Definizione dello Schema (Constraints & Indexes)
Per garantire che il sistema scali correttamente:
* Crea un **vincolo di unicità** su `id` per i nodi `Frame`.
* Crea un **indice di ricerca** sulla proprietà `hospital` del nodo `Video`.

```cypher
CREATE INDEX frame_unique FOR (f:Frame) ON f.id IS UNIQUE
CREATE INDEX annotator_unique FOR (a:Annotator) ON a.license_id IS UNIQUE
CREATE INDEX video_idx FOR (rd:rawData) ON rd.hospital
```

### Task 2: Modellazione delle Annotazioni (Creazione nodi e relazioni)
Il Dr. Bianchi (`MED_99`) ha appena completato l'annotazione del frame `F_001`.
* Crea un nodo `Annotation` con proprietà `label: "Artery"`, `bbox: [10, 20, 150, 200]` e `created_at: timestamp()`.
* Crea la relazione `PRODUCED` tra l'annotatore e l'annotazione.
* Crea la relazione `REFERENCES` tra l'annotazione e il frame `F_001`.

```cypher
MATCH (ann:Annotator {license_id: 'MED_99'})
MATCH (f:Frame {id: 'F_001'})
CREATE (a:Annotation {label: "Artery", bbox: [10, 20, 150, 200], created_at: timestamp()})
MERGE (ann)-[:PRODUCED]->(a)
MERGE (a)-[:REFERENCES]->(f);

```

### Task 3: Evoluzione del Modello (Attributi e Etichette)
Dobbiamo classificare i dataset in base alla loro criticità.
* Aggiungi una nuova etichetta (Label) chiamata `:Certified` a tutti i nodi `Dataset` che contengono più di 0 frame (usa `MATCH` e `COUNT`).
* Aggiorna lo `status` del dataset "HemoSet_2026" da "Draft" a "Ready".

```cypher
MATCH (:Frame)-[:INCLUDED_IN]->(ds:Dataset)
WITH ds, count(f) AS frameCount
WHERE frameCount > 0
SET ds:Certified;

MATCH (ds:Dataset{name: 'HemoSet_2026})
SET ds.name = "Ready"

```

### Task 4: Query di Integrità e Qualità (Interrogazione complessa)
Scrivi una query che restituisca:
* Il nome dell'annotatore e il numero totale di annotazioni prodotte, ma solo per i frame che appartengono al video proveniente dall'ospedale "Gemelli".
* Ordina i risultati per numero di annotazioni decrescente.

MATCH (a:Annotator)-[:PRODUCE]->(ann:Annotation)-[:REFERENCES]->(:Frame)-[:EXTRACTED_FROM]->(:Video{hospital: 'Gemelli'})
RETURN a.name, COUNT(ann) AS tot_ann
ORDER BY tot_ann DESC

### Task 5: Analisi di Riuso (Graph Pattern Matching)
È fondamentale sapere se i dati di test sono "inquinati" da dati di training.
* Trova tutti i `Frame` che sono inclusi contemporaneamente in due `Dataset` diversi.
* Restituisci i nomi dei due dataset e l'ID del frame condiviso.

MATCH (f:Frame)-[:INCLUDED_IN]->(ds1:Dataset), (f)-[:INCLUDED_IN]->(ds2:Dataset)
WHERE ds1.name <> ds2.name AND elementId(ds1)< elementId(ds2)
RETURN ds1.name, ds2.anme, f.id