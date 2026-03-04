# Shortest Path Algorithms

Parent: [[4_1_Shortest_Path]]

## Algoritmo di Dijkstra

Ideale per grafi con pesi degli archi non negativi.

## Algoritmo di Bellman-Ford

Necessario se il grafo contiene archi con pesi negativi (purché non vi siano cicli negativi).
  
## Algoritmo di Floyd-Warshall

Utilizzato per risolvere il problema del cammino minimo tra tutte le coppie di vertici in un grafo pesato. Utilizza la programmazione dinamica per confrontare iterativamente tutti i possibili percorsi attraverso il grafo tra ogni coppia di vertici.

## Algoritmo di A\*

Un algoritmo di ricerca euristica che utilizza una funzione di stima (euristica) per guidare la ricerca verso la destinazione, spesso utilizzato in grafi pesati per trovare il cammino più breve in modo efficiente.

## Algoritmo di Viterbi

Un algoritmo dinamico utilizzato principalmente per trovare il percorso più probabile in _modelli di Markov nascosti_ (HMM), ma può essere adattato per risolvere problemi di cammino minimo in grafi pesati, specialmente quando si desidera massimizzare la probabilità piuttosto che minimizzare un costo.

## Algoritmo di Johnson

Un algoritmo efficiente per trovare i cammini minimi tra tutte le coppie di vertici in un grafo pesato, specialmente quando il grafo è sparso. Combina l'algoritmo di Bellman-Ford per gestire i pesi negativi e l'algoritmo di Dijkstra per calcolare i cammini minimi.
