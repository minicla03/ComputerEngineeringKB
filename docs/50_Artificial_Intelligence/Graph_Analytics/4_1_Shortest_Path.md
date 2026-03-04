# Shortest Paths

Parent: [[4_Graph_Traversal]]

Lo **shortest path problem** cerca di individuare il percorso più "rapido" o efficiente tra due vertici.

Il problema del cammino minimo può essere formulato in tre varianti principali:

1. **Single-Source Shortest Path**: Dato un **singolo nodo sorgente**, l'obiettivo è trovare il percorso più rapido per raggiungere **tutti gli altri nodi** del grafo.
2. **Single-Pair Shortest Path**: Dati un nodo **sorgente** e un nodo **destinazione** specifici, si cerca il percorso più rapido (se esiste) tra i due.
3. **All-Pairs Shortest Path**: L'obiettivo è trovare i cammini minimi tra **ogni possibile coppia** di vertici del grafo.

La natura del problema varia significativamente in base alla struttura del grafo. Possiamo avere grafi pesati o non pesati.

> **Unweighted Graphs**
> In un grafo non pesato, ogni arco ha lo stesso "costo" o "peso" (generalmente considerato come 1). L'obiettivo è trovare un percorso che minimizzi il numero di archi attraversati tra due vertici.

Per i grafi non pesati, l'algoritmo di ricerca in ampiezza (BFS) è ottimale. Esplorando il grafo a livelli, garantisce di trovare il cammino con il minor numero di archi in tempo $O(|V| + |E|)$.

> **Weighted Graphs**
> Un grafo si dice pesato quando a ogni arco è associato un numero reale (peso), che può rappresentare distanza, costo o tempo.

L'obiettivo è trovare un percorso tra due vertici tale che la somma dei pesi degli archi costituenti sia minimizzata.

- **Algoritmo di Dijkstra**: Ideale per grafi con pesi degli archi non negativi.
- **Algoritmo di Bellman-Ford**: Necessario se il grafo contiene archi con pesi negativi (purché non vi siano cicli negativi).
- **Algoritmo di Floyd-Warshall**: Utilizzato per risolvere il problema del cammino minimo tra tutte le coppie di vertici in un grafo pesato. Utilizza la programmazione dinamica per confrontare iterativamente tutti i possibili percorsi attraverso il grafo tra ogni coppia di vertici.
- **Algoritmo di A\***: Un algoritmo di ricerca euristica che utilizza una funzione di stima (euristica) per guidare la ricerca verso la destinazione, spesso utilizzato in grafi pesati per trovare il cammino più breve in modo efficiente.
- **Algoritmo di Viterbi**: Un algoritmo dinamico utilizzato principalmente per trovare il percorso più probabile in _modelli di Markov nascosti_ (HMM), ma può essere adattato per risolvere problemi di cammino minimo in grafi pesati, specialmente quando si desidera massimizzare la probabilità piuttosto che minimizzare un costo.
- **Algoritmo di Johnson**: Un algoritmo efficiente per trovare i cammini minimi tra tutte le coppie di vertici in un grafo pesato, specialmente quando il grafo è sparso. Combina l'algoritmo di Bellman-Ford per gestire i pesi negativi e l'algoritmo di Dijkstra per calcolare i cammini minimi.
