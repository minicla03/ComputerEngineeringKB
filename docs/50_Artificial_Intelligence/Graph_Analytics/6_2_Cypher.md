# Cypher

Parent: [[6_1_Neo4j]]


## Definizione dello Schema e Integrità

Sebbene i database a grafi siano flessibili, l'integrità dei dati deve essere garantita tramite vincoli e indici.

I vincoli impediscono la duplicazione di entità chiave e assicurano la qualità del dato.

!!!note `CREATE CONSTRAINT` è usato per definire vincoli di unicità e di esistenza, garantendo che i dati inseriti rispettino le regole stabilite.

```cypher
// Garantisce l'unicità dell'ID dipendente
CREATE CONSTRAINT FOR (e:Employee) REQUIRE e.employeeId IS UNIQUE;

// Assicura che ogni progetto abbia un titolo
CREATE CONSTRAINT FOR (p:Project) REQUIRE p.title IS NOT NULL;
```

## CRUD di Nodi, Relazioni e Proprietà

!!!note `CREATE` è usata per creare nodi, relazioni, proprietà e constraints all'interno del grafo. C

La sintassi di base è la seguente:

```cypher
CREATE (n:Label {property: value})
```

Crea nuovi elementi senza verificare se esistono già, quindi si possono avere dei duplicati in quanto non c'è un controllo di unicità.

!!!note `MERGE` funge da "Match or Create": cerca il pattern e, se non lo trova, lo crea. Garantisce l'idempotenza. Se il pattern esiste, si comporta come un `MATCH`; se non esiste, come un `CREATE`.

```cypher
// Assicura l'esistenza di un'abilità senza duplicarla
MERGE (s:Skill {name: "Python"});
```

Inoltre la, `MERGE` permette di differenziare le azioni in base all'esito della ricerca tramite le clausole ON CREATE e ON MATCH.


```cypher
MERGE (p:Project {title: "Project Icarus"})
ON CREATE SET p.createdAt = timestamp() // Eseguito solo se il progetto è nuovo
ON MATCH SET p.lastAccessed = timestamp(); // Eseguito se il progetto esisteva già
```

### Indici

Creare indici sulle proprietà utilizzate frequentemente nei filtri di ricerca per velocizzare l'operazione di Node Index Seek.

```cypher
CREATE INDEX FOR (e:Employee) ON (e.name);
```

---

La clausola `SET` permette di aggiornare proprietà o etichette.

- **Proprietà singole:** Permette di cambiare un valore o aggiungerlo se non esistente.
    ```cypher
    MATCH (n:User {username: 'mrossi'})
    SET n.lastLogin = datetime(), n.status = 'Active'
    ```
- **Etichette (Labels):** Utilizzata per cambiare il "ruolo" di un nodo nel grafo.
    ```cypher
    MATCH (n:User {username: 'mrossi'})
    SET n:Admin
    ```
- **Sostituzione integrale:** Utilizzando l'operatore `=`, è possibile sovrascrivere l'intero set di proprietà con una nuova mappa di dati.

A differenza della cancellazione del nodo, `REMOVE` agisce solo sui componenti interni (proprietà o etichette).

- **Eliminare una proprietà:** Il campo scompare dal nodo senza influenzare il resto.

    ```cypher
    MATCH (n:User {username: 'mrossi'})
    REMOVE n.temporaryToken
    ```

- **Rimuovere un'etichetta:** Fondamentale quando un nodo cambia categoria.

    ```cypher
    MATCH (n:Admin)
    WHERE n.permissions = 'None'
    REMOVE n:Admin SET n:User
    ```

L'integrità referenziale impedisce di eliminare un nodo che possiede ancora delle relazioni.

- `DELETE` funziona SOLO se il nodo è isolato. Se il nodo ha relazioni attive, il database restituirà un errore per proteggere la coerenza del grafo.
- `DETACH DELETE` elimina il nodo e tutte le relazioni entranti e uscenti.

    ```cypher
    MATCH (n:User {username: 'mrossi'})
    DETACH DELETE n
    ```

## Pattern Matching

Il **pattern matching** è una delle caratteristiche più potenti di Cypher, permettendo di esprimere query complesse in modo intuitivo.

!!!note Il comando `MATCH` è l'equivalente della `SELECT` in SQL. Viene utilizzato esclusivamente per individuare pattern esistenti nel database.
Il pattern è descritto indicando i nodi cerchi e le relazioni come frecce.

I pattern appaiono in più luoghi in Cypher: nelle clausole MATCH, CREATE e MERGE, e nella clausola WHERE.

```plaintext
(a)-[]->(c)
```

Si può specificare etichette per i nodi e tipi per le relazioni, oltre a proprietà per entrambi.

```plaintext

(a:User:Admin)-[]->(b) //può avere più etichette
(a)-[:FRIENDS_WITH]->(b) //specifica il tipo di relazione
(a)-[:WORKS_ON {role: "Developer"}]->(b) //specifica proprietà sulla relazione
(a)-[r:REL_TYPE1|REL_TYPE2]->(b) //specifica più tipi di relazione
(a:User {name: "Alice"})-[]-(b) //specifica proprietà sul nodo
```

!!!warning All'interno di un singolo pattern, le relazioni saranno matchate una sola volta.

Il **Variable-length matching** permette di interrogare catene di relazioni senza conoscerne a priori la profondità esatta. In Cypher, questo si ottiene utilizzando l'asterisco * all'interno della definizione della relazione.

!!!note La struttura base segue il formato: -[TYPE*minHops..maxHops]->.

- *: Ricerca a profondità arbitraria .
- *3: Ricerca esattamente a 3 salti di distanza.
- *1..3: Ricerca tra 1 e 3 salti di distanza.
- *..5: Ricerca fino a un massimo di 5 salti.

Spesso non serve solo il nodo finale, ma l'intera sequenza di nodi che compone il cammino.

```cypher
MATCH path = (start:Project)-[:DEPENDS_ON*..5]->(end:Project)
RETURN nodes(path) AS ProgettiNelCammino,
       relationships(path) AS Relazioni,
       length(path) AS NumeroSalti;
```

Ottenuto il pattern è possibile filtrare ulteriormente i risultati con la clausola `WHERE`, che supporta espressioni complesse e funzioni di aggregazione. a sempre collocata subito dopo il `MATCH` a cui si riferisce, poiché aiuta il database a restringere il campo di ricerca già durante l'esecuzione del pattern matching.

```cypher
MATCH (p:Project)-[:DEPENDS_ON*..5]->(d:Project)
WHERE p.status = "active" AND d.status = "completed"
RETURN p.name, d.name;
```

!!!note La clausola `WITH` permette di concatenare diverse parti della query, passando i risultati di una sezione a quella successiva. È fondamentale per manipolare i dati prima di procedere con ulteriori operazioni. Permette di fare un operazione di:

- **filtraggio intermedio:** È possibile utilizzare `WHERE` subito dopo un `WITH` per escludere risultati prima di eseguire un nuovo `MATCH`.
- **aggregazione:** Permette di raggruppare dati (ad esempio contando elementi con `count()`) e utilizzare il risultato del calcolo nel resto della query.
- **alias e trasformazioni:** Consente di rinominare variabili o eseguire calcoli complessi, rendendo il set di dati più pulito per le clausole successive.
- **limitazione dei risultati:** Si può usare `ORDER BY`, `SKIP` o `LIMIT` all'interno di un `WITH` per isolare solo i record più rilevanti prima di continuare la ricerca nel grafo.

```cypher
//Immaginiamo un database di una libreria. 
//Vogliamo trovare gli autori che hanno scritto più di 5 libri e, 
//solo per loro, vedere se hanno vinto dei premi.

// 1. Trova gli autori e i loro libri
MATCH (a:Author)-[:WROTE]->(b:Book)

// 2. Raggruppa per autore e conta i libri
WITH a, count(b) AS numeroLibri
WHERE numeroLibri > 5

// 3. Ora che abbiamo solo gli "autori prolifici", cerchiamo i loro premi
MATCH (a)-[:WON]->(p:Award)

// 4. Restituisci il nome dell'autore e il premio
RETURN a.name, p.title, numeroLibri

```

Senza il `WITH`, Cypher cercherebbe di collegare ogni singolo autore a ogni premio e ogni libro contemporaneamente. Usando `WITH`, abbiamo "isolato" una lista ristretta di autori (quelli con più di 5 libri) e abbiamo dato istruzione al database di proseguire la ricerca del `MATCH` successivo solo per quei profili specifici.

## Navigazione dei Cammini

Per trovare il percorso più rapido tra due punti, Cypher offre funzioni ottimizzate che evitano l'esplorazione esaustiva di ogni ramo.

```cypher
MATCH (s:Supplier {code: "SUP-A"}), (c:Customer {id: "CUST-Z"})
MATCH p = shortestPath((s)-[*..15]-(c))
RETURN p;
```
