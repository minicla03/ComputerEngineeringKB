# CBRS - Content-Based Recommender System: Codice

- Caso di studio: MovieLens 100K Dataset
- Modello di grafo: utenti, film, generi, attori, registi
- Interazioni: `WATCHED`, `RATED`
- Obiettivo: raccomandare film basati sulle caratteristiche dei film che l'utente ha già apprezzato

## Approccio 1: Feature Overlap

L'obiettivo è trasformare le interazioni implicite (`WATCHED`/`RATED`) in archi di interesse espliciti (`INTERESTED_IN`) tra l'utente e le caratteristiche dei film (generi, attori, registi).

### 1 Ingerenza degli Interessi (Batch Processing)

Questa operazione "materializza" la conoscenza nel grafo. Utilizziamo una soglia di occorrenze (es. > 2) per evitare di sporcare il profilo con interessi sporadici .

```cypher
CALL apoc.periodic.iterate(
  "MATCH (u:User) RETURN u", 
  "MATCH (u)-[:WATCHED|RATED]->(m:Movie)-[:ACTS_IN|WRITTEN|DIRECTED|PRODUCED|HAS]-(f)
   WITH u, f, count(*) AS occurrences
   WHERE occurrences > 2
   MERGE (u)-[:INTERESTED_IN]->(f)",
  {batchSize: 100, parallel: false}
)
```

oppure

```cypher
MATCH (u:User)
CALL {
  WITH u
  MATCH (u)-[:WATCHED|RATED]->(m:Movie)-[:ACTS_IN|WRITED|DIRECTED|PRODUCED|HAS]-(f)
  WITH u, f, count(*) AS occurrences
  WHERE occurrences > 2
  MERGE (u)-[:INTERESTED_IN]->(f)
} IN TRANSACTIONS OF 100 ROWS
```

### 2 Generazione delle Raccomandazioni (Real-time)

Una volta popolati gli archi `INTERESTED_IN`, la query di produzione è la stessa per entrambi i metodi di batching. Il sistema calcola l'overlap (sovrapposizione) tra ciò che piace all'utente e le feature dei film non ancora visti.

```cypher
// 1. Identifica le feature di interesse dell'utente
MATCH (user:User {userId: "1"})-[:INTERESTED_IN]->(feature)

// 2. Recupera i film collegati a quelle feature
MATCH (feature)-[:ACTS_IN|WRITED|DIRECTED|PRODUCED|HAS]-(movie:Movie)

// 3. Escludi i film già visti
WHERE NOT (user)-[:WATCHED|RATED]->(movie)

// 4. Calcola il punteggio di pertinenza (rel_score)
WITH movie, count(DISTINCT feature) AS rel_score
ORDER BY rel_score DESC

// 5. Restituisce la Top 10
RETURN movie.title, rel_score
LIMIT 10
```

## Approccio 2: Feature Similarity

Questo metodo tratta gli item e i profili utenti comed ei vettori che vengono poi mappati in un **Vector Space Model (VSM)** nel quale è semplice calcolare la **Cosine Similarity**. Invece di contare semplicemente le connessioni, pesiamo matematicamente quanto un utente sia vicino a un film nello spazio delle caratteristiche.

### Vettorializzazione di item e profili utente

L'obiettivo è rappresentare ogni film e ogni utente come vettori di pesi numerici.

#### 1 Vettorializzazione degli Item

Dobbiamo creare una relazione standardizzata `HAS_FEATURE` e pre-calcolare la "norma" di ogni film (la sua lunghezza vettoriale) per ottimizzare le performance in real-time.

```cypher
CALL apoc.periodic.iterate(
  "MATCH (m:Movie) RETURN m",
  "MATCH (m)-[:ACTS_IN|WRITED|DIRECTED|PRODUCED|HAS]-(f)
   MERGE (m)-[r:HAS_FEATURE]->(f)
   SET r.weight = 1",
  {batchSize: 30, parallel: false}
)
```

oppure 

```cypher
MATCH (m:Movie)
CALL {
  WITH m
  MATCH (m)-[:ACTS_IN|WRITED|DIRECTED|PRODUCED|HAS]-(f)
  MERGE (m)-[r:HAS_FEATURE]->(f)
  SET r.weight = 1
} IN TRANSACTIONS OF 30 ROWS
```

**Pre-calcolo della Norma (da eseguire dopo uno dei precedenti):** il calcolo della norma è necessario per la formula della Cosine Similarity, che richiede di dividere il prodotto scalare per il prodotto delle norme dei vettori.

```cypher
MATCH (m:Movie)
OPTIONAL MATCH (m)-[r:HAS_FEATURE]->()
WITH m, sqrt(sum(r.weight^2)) AS movieNorm
SET m.movieNorm = movieNorm
```

#### 2 Vettorializzazione dei Profili Utente

Calcoliamo l'interesse dell'utente verso ogni feature, normalizzandolo in base al numero totale di film visti per bilanciare il profilo.

```cypher
CALL apoc.periodic.iterate(
  "MATCH (u:User) RETURN u.userId AS id",
  "MATCH (u:User {userId: id})
   OPTIONAL MATCH (u)-[:WATCHED|RATED]->(m:Movie)
   WITH u, count(DISTINCT m) AS total
   MATCH (u)-[:WATCHED|RATED]->(m:Movie)-[:HAS_FEATURE]->(f)
   WITH u, total, f, count(*) AS occ
   WHERE occ > 2
   MERGE (u)-[r:INTERESTED_IN]->(f)
   SET r.weight = occ, r.normalizedWeight = occ * 1.0 / total",
  {batchSize: 20, parallel: false}
)
```

oppure

```cypher
MATCH (u:User)
CALL {
  WITH u
  OPTIONAL MATCH (u)-[:WATCHED|RATED]->(m:Movie)
  WITH u, count(DISTINCT m) AS total
  MATCH (u)-[:WATCHED|RATED]->(m:Movie)-[:HAS_FEATURE]->(f)
  WITH u, total, f, count(*) AS occ
  WHERE occ > 2
  MERGE (u)-[r:INTERESTED_IN]->(f)
  SET r.weight = occ, r.normalizedWeight = occ * 1.0 / total
} IN TRANSACTIONS OF 20 ROWS
```

### Raccomandazione Real-time (Cosine Similarity)

Il motore ora calcola il prodotto scalare tra i pesi dell'utente e quelli del film, dividendolo per il prodotto delle loro norme.

```cypher
MATCH (u:User {userId: "2"})
// 1. Calcola la norma dell'utente a runtime
OPTIONAL MATCH (u)-[i:INTERESTED_IN]->()
WITH u, sqrt(sum(i.normalizedWeight^2)) AS userNorm

// 2. Trova film candidati tramite feature condivise
MATCH (u)-[i:INTERESTED_IN]->(f)<-[h:HAS_FEATURE]-(m:Movie)
WHERE NOT EXISTS { MATCH (u)-[:WATCHED|RATED]->(m) }

// 3. Applica la formula della Cosine Similarity
WITH m, userNorm, sum(i.normalizedWeight * h.weight) AS dot
WHERE m.movieNorm > 0 AND userNorm > 0
WITH m, dot / (userNorm * m.movieNorm) AS similarity
ORDER BY similarity DESC
RETURN m.title, similarity
LIMIT 5
```

### Feature Numeriche

L'integrazione di feature continue (come il rating medio) in uno spazio vettoriale a predominanza booleana è un classico problema di data scaling. Dobbiamo assicurarci che una dimensione vettoriale non domini matematicamente sulle altre a causa della sua magnitudine.

Moltiplicare il valore per un parametro di scaling $\alpha$ è la soluzione ottimale. Ad esempio, se i generi valgono $1$ e i rating vanno da $1$ a $5$, un $\alpha = 0.2$ ridimensiona il rating su una scala $[0.2, 1.0]$, rendendolo comparabile alle feature booleane.

#### 1 Vettorializzazione della Feature Numerica (Item)

Aggiungiamo la nuova dimensione al vettore del film collegandolo a un nodo speciale che rappresenta il rating medio.

```cypher
// Impostiamo alpha = 0.2 per scalare un rating 1-5 a un valore 0.2-1.0
WITH 0.2 AS alpha
// Creiamo un nodo feature che rappresenti concettualmente il "Rating Globale"
MERGE (meta:Feature {name: 'AverageRating', type: 'Numerical'})
WITH meta, alpha
MATCH (m:Movie)
WHERE m.imdbRating IS NOT NULL
// Creiamo la relazione e applichiamo lo scaling
MERGE (m)-[r:HAS_FEATURE]->(meta)
SET r.weight = m.imdbRating * alpha
```

#### 2 Vettorializzazione del Profilo Utente

Come indicato nella teoria, per proiettare l'utente nel VSM per le feature numeriche dobbiamo calcolare la media dei valori. Calcoliamo quindi il rating medio che l'utente è solito assegnare (o il rating medio dei film che guarda) e lo scaliamo.

```cypher
WITH 0.2 AS alpha
MATCH (meta:Feature {name: 'AverageRating', type: 'Numerical'})
MATCH (u:User)-[rel:RATED]->(m:Movie)
WITH u, meta, alpha, avg(rel.rating) AS userAvgRating
// Materializziamo l'interesse verso questa dimensione numerica
MERGE (u)-[r:INTERESTED_IN]->(meta)
// Nel caso dell'utente, il peso normalizzato diventa la sua media scalata
SET r.normalizedWeight = userAvgRating * alpha
```

### 3 Ricalcolo delle Norme Vettoriali

Avendo aggiunto una nuova dimensione geometrica ai vettori (sia per i film che per gli utenti), le norme calcolate in precedenza (la lunghezza del vettore) non sono più valide. Dobbiamo obbligatoriamente lanciare un ricalcolo *dopo* aver aggiunto le feature numeriche.

```cypher
// Ricalcolo norma Item
MATCH (m:Movie)
OPTIONAL MATCH (m)-[r:HAS_FEATURE]->()
WITH m, sqrt(sum(r.weight^2)) AS movieNorm
SET m.movieNorm = movieNorm

// Ricalcolo norma Utente
```

## Approccio 3: Similarità tra item

L'obiettivo è calcolare la similarità tra tutte le coppie di film (usando la *Cosine Similarity* o il *Dice Coefficient*) e memorizzare solo i *k* collegamenti più forti tramite archi `SIMILAR_TO` pesati.

### 1 Costruzione della Rete k-NN (Batch Processing)

```cypher
CALL apoc.periodic.iterate(
  "MATCH (m1:Movie) RETURN m1",
  "MATCH (m2:Movie) WHERE id(m1) < id(m2) // Evita calcoli speculari (A-B e B-A) e A-A
   MATCH (m1)-[r1:HAS_FEATURE]->(f)<-[r2:HAS_FEATURE]-(m2)
   WITH m1, m2, sum(r1.weight * r2.weight) AS dot
   WHERE dot > 0
   WITH m1, m2, dot / (m1.movieNorm * m2.movieNorm) AS similarity
   WHERE similarity > 0.5 // Threshold per evitare un grafo troppo denso
   MERGE (m1)-[s:SIMILAR_TO]-(m2)
   SET s.weight = similarity",
  {batchSize: 50, parallel: false}
)
```

oppure

```cypher
MATCH (m1:Movie)
CALL {
  WITH m1
  MATCH (m2:Movie) WHERE id(m1) < id(m2)
  MATCH (m1)-[r1:HAS_FEATURE]->(f)<-[r2:HAS_FEATURE]-(m2)
  WITH m1, m2, sum(r1.weight * r2.weight) AS dot
  WHERE dot > 0
  WITH m1, m2, dot / (m1.movieNorm * m2.movieNorm) AS similarity
  WHERE similarity > 0.5
  MERGE (m1)-[s:SIMILAR_TO]-(m2)
  SET s.weight = similarity
} IN TRANSACTIONS OF 50 ROWS
```

**Dettaglio strutturale** L'arco `SIMILAR_TO` è **simmetrico** e unidirezionale (o senza direzione esplicita letta a runtime), poiché la distanza tra Pulp Fiction e The Punisher è ovviamente identica in entrambe le direzioni.

### 2 Motore di Raccomandazione (Real-time)

Avendo pre-calcolato la topologia k-NN, la query in tempo reale diventa un fulmine. Il punteggio di un film candidato ($p$) è la sommatoria delle similarità con i film ($i$) che l'utente ($u$) ha già nello storico.

Formula applicata: $interest(u,p)=\sum_{i\in Items(u)}sim(i,p)$

```cypher
// 1. Parti dall'utente target e naviga verso i film che ha visto/votato
MATCH (u:User {userId: "2"})-[:WATCHED|RATED]->(seen:Movie)

// 2. Sfrutta il grafo k-NN per trovare i film simili ai suoi
MATCH (seen)-[s:SIMILAR_TO]-(candidate:Movie)

// 3. Assicurati di non suggerire film che ha già visto
WHERE NOT EXISTS { (u)-[:WATCHED|RATED]->(candidate)}

// 4. Somma i pesi delle similarità per generare lo score globale
WITH candidate, sum(s.weight) AS interest_score
ORDER BY interest_score DESC

// 5. Restituisci la Top 10
RETURN candidate.title, interest_score
LIMIT 10
```

### Usando la GDS Library

Per prima cosa, carichiamo la topologia di interesse nella RAM del server GDS. Isoliamo solo i nodi Movie e Feature, e gli archi HAS_FEATURE che li collegano.

```cypher
CALL gds.graph.project(
  'movie_features_graph',
  ['Movie', 'Feature'],
  {
    HAS_FEATURE: {
      orientation: 'UNDIRECTED'
    }
  }
)
YIELD graphName, nodeCount, relationshipCount, memoryUsage;
```

ora lanciamo l'algoritmo di similarità. La GDS analizzerà tutti i nodi Movie, confronterà le loro feature e scriverà direttamente sul database transazionale i k collegamenti più forti.



```cypher
CALL gds.nodeSimilarity.write(
  'movie_features_graph',
  {
    writeRelationshipType: 'SIMILAR_TO',
    writeProperty: 'weight',
    similarityCutoff: 0.5,
    topK: 10,
    bottomNodeLabels: ['Movie']
  }
)
YIELD nodesCompared, relationshipsWritten, computeMillis;
```

Mai lasciare proiezioni orfane in RAM una volta completato il job di batch.

```Cypher
CALL gds.graph.drop('movie_features_graph');
```

Il pregio della separazione tra modello descrittivo e predittivo è che la query API che espone il servizio agli utenti non cambia di una virgola rispetto a quella vista in precedenza.

```Cypher
MATCH (u:User {userId: "2"})-[:WATCHED|RATED]->(seen:Movie)-[s:SIMILAR_TO]->(candidate:Movie)
WHERE NOT EXISTS { (u)-[:WATCHED|RATED]->(candidate) }
WITH candidate, sum(s.weight) AS interest_score
ORDER BY interest_score DESC
RETURN candidate.title, interest_score
LIMIT 10
```

--- 

// 2. Calcolo di FastRP e scrittura dell'array sul nodo Movie
CALL gds.fastRP.write(
  'movie_features_embed_graph',
  {
    writeProperty: 'embedding', // La proprietà richiesta poi da KNN
    embeddingDimension: 128,     // Dimensione del vettore (tipicamente tra 64 e 256)
    iterationWeights: [0.0, 1.0, 0.7], // Peso dato ai cammini di lunghezza 0, 1, 2...
    nodeLabels: ['Movie']       // Calcola e scrive l'embedding solo per i Film
  }
)
YIELD nodePropertiesWritten, computeMillis;

CALL gds.knn.write(
  'movie_embeddings_graph',
  {
    nodeProperties: ['embedding'],
    writeRelationshipType: 'SIMILAR_TO_KNN',
    writeProperty: 'weight',
    topK: 10,
    similarityCutoff: 0.5,
    sampleRate: 1.0,      // 1.0 significa calcolo esatto. Valori minori attivano l'approssimazione per grafi enormi
    deltaThreshold: 0.001,
    nodeLabels: ['Movie'],
    similarityMetric: 'COSINE' // Specifica la metrica coerente con il Vector Space Model
  }
)
YIELD nodesCompared, relationshipsWritten, computeMillis;