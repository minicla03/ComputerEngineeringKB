# Cypher

Parent: [[7_2_Neo4j]]

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

I pattern appaiono in più luoghi in Cypher: nelle clausole `MATCH`, `CREATE` e `MERGE`, e nella clausola `WHERE`.

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

!!!warning All'interno di un singolo pattern, le relazioni saranno matchate una sola volta. Cypher applica l'isomorfismo degli archi: garantisce che un singolo arco non venga mai attraversato più di una volta all'interno dello stesso cammino.

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

La clausola `OPTIONAL MATCH` è l’equivalente funzionale del `LEFT OUTER JOIN` in SQL. È lo strumento fondamentale per interrogare un grafo quando non sei sicuro che un determinato pattern esista, ma desideri comunque mantenere i risultati ottenuti dai passaggi precedenti della query.
Se il pattern esiste lega le variabili definite nel pattern ai nodi o alle relazioni corrispondenti (esattamente come un `MATCH`).
Se il pattern NON esiste la query non fallisce e non scarta la riga. Invece, assegna il valore **`null`** a tutte le variabili introdotte in quella specifica clausola `OPTIONAL MATCH`.

```cypher
MATCH (c:Chirurgo)
OPTIONAL MATCH (c)-[:UTILIZZA]->(r:SistemaRobotico)
RETURN c.nome AS Chirurgo, r.modello AS Robot

// Analisi del Risultato:
//- Se il Chirurgo "Mario Rossi" utilizza il sistema "Da Vinci", vedrai: `Mario Rossi | Da Vinci`.
//- Se la Chirurga "Elena Bianchi" non ha alcuna relazione `:UTILIZZA` nel grafo, vedrai: `Elena Bianchi | null`.
```

Se esegui un `OPTIONAL MATCH` seguito da un `MATCH` sulla stessa variabile, il `MATCH` successivo filtrerà comunque i `null`. In breve: se rendi qualcosa opzionale, deve rimanere tale o essere gestito con attenzione nelle clausole successive e qualsiasi espressione calcolata su una variabile `null` restituirà a sua volta `null`.

Ottenuto il pattern è possibile filtrare ulteriormente i risultati con la clausola `WHERE`, che supporta espressioni complesse e funzioni di aggregazione. a sempre collocata subito dopo il `MATCH` a cui si riferisce, poiché aiuta il database a restringere il campo di ricerca già durante l'esecuzione del pattern matching.

```cypher
MATCH (p:Project)-[:DEPENDS_ON*..5]->(d:Project)
WHERE p.status = "active" AND d.status = "completed"
RETURN p.name, d.name;
```

### Agregazioni

!!!note La clausola `WITH` permette di concatenare diverse parti della query, passando i risultati di una sezione a quella successiva. È fondamentale per manipolare i dati prima di procedere con ulteriori operazioni.

Permette di fare un operazione di:

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

### Operatori universali

Gli operatori `all`, `any`, `none` e `single` sono funzioni predicative utilizzate per iterare su liste (collezioni) e verificare se i loro elementi soddisfano una determinata condizione. Sono strumenti essenziali quando si lavora con percorsi (paths) o proprietà di tipo array.

Tutti seguono la sintassi: `nome_funzione(variabile IN lista WHERE predicato)`.

`all()` restituisce `true` se **ogni singolo elemento** della lista soddisfa il predicato. È l'operatore più rigoroso: basta un solo elemento non conforme per invalidare l'intero risultato.
`any()` restituisce `true` se **almeno un elemento** della lista soddisfa il predicato. Si ferma non appena trova la prima corrispondenza (short-circuiting).
`none()` restituisce `true` se **nessun elemento** della lista soddisfa il predicato. È l'opposto logico di `any`.
`single()` restituisce `true` se **esattamente un elemento** della lista soddisfa il predicato. Se non ce ne sono, o se ce n'è più di uno, restituisce `false`.

**Short-circuiting:** `any`, `all` e `none` sono ottimizzati. Ad esempio, `all` smette di valutare la lista non appena incontra il primo elemento `false`. `single`, invece, deve scansionare potenzialmente tutta la lista per assicurarsi che non ci sia un secondo elemento valido.

## Chiamate a funzioni di procedura

La clausola `CALL` riesce a invocare routine imperative complesse scritte in linguaggi compilati (tipicamente Java).
L'invocazione di una procedura richiede di specificare il suo *namespace* (la libreria di appartenenza), il nome esatto, gli argomenti di input e l'estrazione dell'output tramite `YIELD`.

```cypher
CALL namespace.modulo.nomeProcedura(arg_posizionale, {mappa_configurazione})
YIELD variabile_output_1, variabile_output_2
```

A livello di pipeline di esecuzione, si può inserire una `CALL` in due contesti ben distinti all'interno di una query.

1. **Chiamata Standalone** quando la procedura opera a livello globale sul database, genera proiezioni in memoria o gestisce task di amministrazione. Non dipende da dati estratti in precedenza.

    ```cypher
    // Esempio: Proiezione di un grafo in RAM per la libreria GDS
    CALL gds.graph.project(
    'myProjectedGraph', // Nome del grafo in memoria
    'User',             // Label dei nodi
    'KNOWS'             // Tipo di relazione
    )
    YIELD graphName, nodeCount, relationshipCount
    RETURN graphName, nodeCount;
    ```

2. **Chiamata In-Query (Subquery)** viene inserita alla fine di una clausola `MATCH` e **viene eseguita iterativamente per ogni record** prodotto dallo stream precedente.

    ```cypher
    MATCH (u:User {status: 'active'})
    // La CALL viene eseguita N volte, calcolando il sottografo per ogni utente 'u'
    CALL apoc.path.subgraphNodes(u, {
        maxLevel: 2,
        relationshipFilter: 'KNOWS>'
    })
    YIELD node AS network_node
    RETURN u.id, count(network_node) AS second_degree_connections;
    ```

La clausola `YIELD` estrae e rende disponibili i risultati generati da una procedura chiamata tramite `CALL`. Molto spesso, i dati estratti tramite `YIELD` non sono l'output finale, ma l'input per una fase successiva di calcolo. Per evitare di interrompere il flusso, si utilizza `WITH`, che permette di filtrare, aggregare e passare le variabili correnti alle istruzioni successive.

```cypher
MATCH (start:City {name: 'Modena'})
CALL gds.bfs.stream('roadNetwork', {sourceNode: start})
YIELD path AS p
// 'WITH' agisce come una pipe logica, applicando un filtro spaziale
WITH p WHERE length(p) >= 3
RETURN nodes(p) AS distant_cities;
```

## Navigazione del Grafo

Un oggetto `path` è un'entità complessa che contiene la sequenza alternata di nodi e relazioni trovata dal motore di ricerca.

**`nodes(path)`** restituisce una lista ordinata di tutti i nodi nel cammino: `[n0, n1, n2]`.
**`relationships(path)`** restituisce una lista ordinata di tutte le relazioni nel cammino: `[r0, r1]`.

```cypher
MATCH p = (start:Pipeline)-[:NEXT*]->(end:Output)
WHERE all(n IN nodes(p) WHERE n.version = '2.1')
RETURN p
```

| Funzione | Descrizione | Utilità |
| :--- | :--- | :--- |
| **`length(path)`** | Restituisce il numero di **relazioni** nel path. | Calcolare la "distanza" tra due entità. |
| **`startNode(rel)`** | Identifica il nodo da cui parte una specifica relazione. | Verificare la direzionalità in liste filtrate. |
| **`endNode(rel)`** | Identifica il nodo in cui termina la relazione. | Analizzare l'impatto di una transizione. |
| **`type(rel)`** | Restituisce il tipo della relazione (es. "SEGMENTA"). | Filtrare dinamicamente relazioni eterogenee. |
|**`reduce()`**| Permette di accumulare un valore iterando su un path | Riduce il path secondo una condizione |

### BFS e DFS

In Cypher nativo, puoi simulare l'esplorazione definendo la profondità del pattern di matching (`-[*1..4]-`). Tuttavia, il motore di esecuzione interno (Cypher Planner) ottimizza la query per trovare i percorsi validi nel minor tempo possibile, **senza garantirti il controllo esatto sull'ordine algoritmico della visita**.

```cypher
// Esplorazione generica (ordine di attraversamento gestito dal database)
MATCH p = (start:Node {id: 'A'})-[*1..4]->(end:Node)
RETURN p;
```

> Questo approccio è sufficiente per pattern-matching di base, ma è computazionalmente rischioso su grafi densi. Non avendo il controllo sulla coda di esplorazione, rischi un'esplosione combinatoria senza poter imporre regole di terminazione anticipata (early-stopping).

Per una logica BFS o DFS sul database transazionale, la procedura `apoc.path.expandConfig` è lo strumento ingegneristico per eccellenza. Ti garantisce il controllo algoritmico a livello di singolo hop, permettendoti di filtrare l'esplorazione senza caricare la memoria.

#### Implementazione BFS (Coda FIFO)

La BFS esplora il grafo a "ondate" concentriche. È la scelta ottimale per estrarre la *k-hop neighborhood* di un nodo o per propagare informazioni in modo uniforme sulla rete.

```cypher
MATCH (start:Node {id: 'A'})
CALL apoc.path.expandConfig(start, {
    relationshipFilter: 'CONNECTED_TO>', // Specifica tipo e direzione dell'arco
    minLevel: 1,
    maxLevel: 4,
    bfs: true  // Forza esplicitamente l'architettura Breadth-First
})
YIELD path
RETURN path;
```

#### Implementazione DFS (Stack LIFO)

La DFS si spinge in profondità lungo un singolo ramo fino a raggiungere un vicolo cieco prima di fare backtracking. È ideale per simulare flussi utente, navigare alberi gerarchici complessi o identificare percorsi ciclici in una rete di dipendenze.

```cypher
MATCH (start:Node {id: 'A'})
CALL apoc.path.expandConfig(start, {
    relationshipFilter: 'CONNECTED_TO>',
    minLevel: 1,
    maxLevel: 10,
    bfs: false // Disabilitando la BFS, la procedura attiva nativamente la DFS
})
YIELD path
RETURN path;
```

GDS permette di lanciare BFS e DFS direttamente in memoria RAM, bypassando il layer transazionale.

```cypher
// Esecuzione BFS su un grafo pre-caricato in memoria
MATCH (source:Node {id: 'A'})
CALL gds.bfs.stream('myProjectedGraph', {
    sourceNode: source,
    maxDepth: 4
})
YIELD path
RETURN path;
```

Utilizzando queste librerie, la complessità asintotica per entrambe le strategie di esplorazione viene mantenuta rigorosamente a $O(V + E)$ (dove $V$ sono i vertici ed $E$ gli archi), assicurando una scalabilità lineare anche in contesti di produzione.

### Camini Minini

Per trovare il percorso più rapido tra due punti su un grafo, Cypher offre funzioni ottimizzate che evitano l'esplorazione esaustiva di ogni ramo.

```cypher
MATCH (s:Supplier {code: "SUP-A"}), (c:Customer {id: "CUST-Z"})
MATCH p = shortestPath((s)-[*..15]-(c))
RETURN p;
```

L'analisi su grafi pesati in contesti di produzione richiede l'utilizzo della libreria **Neo4j Graph Data Science (GDS)**.

#### Algoritmo di Dijkstra (Cammini Pesati)

È lo standard industriale in Cypher per trovare il percorso a costo minimo quando i pesi (es. distanza, tempo, latenza) sono strettamente non negativi. L'esecuzione avviene su un sottografo precedentemente proiettato nella RAM del server per garantire basse latenze.

```cypher
// Presuppone che il grafo 'supplyChainGraph' sia già proiettato in memoria
MATCH (source:Supplier {code: "SUP-A"}), (target:Customer {id: "CUST-Z"})
CALL gds.shortestPath.dijkstra.stream('supplyChainGraph', {
    sourceNode: source,
    targetNode: target,
    relationshipWeightProperty: 'routing_cost'
})
YIELD totalCost, nodeIds
RETURN totalCost, [nodeId IN nodeIds | gds.util.asNode(nodeId).code] AS optimal_path;
```

#### Algoritmo di A* (A-Star)

Per reti stradali, droni o topologie fisiche, GDS implementa A* calcolando l'euristica al volo. Solitamente sfrutta la formula dell'Haversine per stimare la distanza spaziale diretta (in linea d'aria) basandosi sulle coordinate geografiche dei nodi.

```cypher
MATCH (source:Location {city: "Modena"}), (target:Location {city: "Roma"})
CALL gds.shortestPath.astar.stream('routingGraph', {
    sourceNode: source,
    targetNode: target,
    relationshipWeightProperty: 'distance_km',
    latitudeProperty: 'lat',
    longitudeProperty: 'lon'
})
YIELD totalCost, nodeIds
RETURN totalCost, [nodeId IN nodeIds | gds.util.asNode(nodeId).city] AS route;
```

#### Algoritmo di Bellman-Ford

Se la tua rete modella arbitraggi di criptovalute o transazioni finanziarie dove rimborsi e tassi di cambio creano vettori di "costo negativo", Dijkstra fallisce. GDS fornisce un'implementazione nativa di Bellman-Ford per esplorare in sicurezza questi sottografi.

```cypher
MATCH (source:Wallet {id: "W-01"})
CALL gds.bellmanFord.stream('financialGraph', {
    sourceNode: source,
    relationshipWeightProperty: 'transaction_fee'
})
YIELD index, targetNode, distance
RETURN gds.util.asNode(targetNode).id AS target_wallet, distance
ORDER BY distance ASC;
```

#### Limiti Architetturali

* **Floyd-Warshall e Johnson (APSP):** Lanciare algoritmi All-Pairs con complessità spaziale quadratica e temporale cubica direttamente su un database a grafo transazionale da milioni di nodi è il modo più affidabile per causare un *Out Of Memory* fatale. GDS non li espone per l'intero grafo; si preferisce approssimare le distanze globali tramite tecniche di Graph Embedding (come *FastRP*) o calcoli decentralizzati.
* **Viterbi:** Neo4j archivia grafi di proprietà, non Catene di Markov Nascoste. Viterbi non si mappa su una query Cypher spaziale. La prassi corretta prevede l'utilizzo di Cypher solo per estrarre le matrici di transizione/emissione in formato tabellare vettoriale, delegando poi il calcolo tensoriale a script Python esterni (tramite librerie come NumPy o `hmmlearn`).