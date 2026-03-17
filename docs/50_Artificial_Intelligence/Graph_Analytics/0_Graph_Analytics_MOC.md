---
area: 🤖 artificial-intelligence
tags: [graph-analytics, graphML, network-analysis]
created: 2026-02-12
---

# 🗺️ Graph Analytics (MOC)

> Stato: #growing
> MOC Genitore: [[50_Artificial_Intelligence]]


- [[1_Graph_Analytics_Intro]] - _Concetti di base e importanza della Graph Analytics._

## Grafo: Teoria, Strutture Dati e Modelli

*Fondamenti teorici e modellazione delle strutture dati per la memorizzazione dei grafi.*

- [[2_Graph_Theory]] - _Fondamenti di teoria dei grafi, tipi di grafi e proprietà._
- [[3_Graph_Storage]] - _Strutture dati per la memorizzazione (Matrici e Liste di Adiacenza)._

## Algoritmi di Attraversamento e Routing

*Algoritmi deterministici per l'attraversamento spaziale e il routing.*

- [[4_Graph_Traversal]] - _Algoritmi di attraversamento base (BFS, DFS)._
- [[4_1_Shortest_Path]] - _Definizione del problema dei cammini più brevi._
- [[4_2_SP_Algorithms]] - _Algoritmi specifici per il calcolo del cammino minimo (es. Dijkstra, A*)._

## Analisi della Connettività e Rilevamento di Pattern

*Visione mesoscopica della rete: connettività e rilevamento di pattern.*

- [[5_Graph_Connettivity]] - _Analisi della connettività e componenti connesse._
- [[5_1_Clustering]] - _Rilevamento di comunità e struttura dei grafi._

## Importanza, Centralità e Dinamiche Stocastiche

*Metriche di rilevanza, modelli probabilistici e algoritmi di ranking web-scale.*

- [[6_Centrality_Measures]] - _Misure di centralità topologica (Degree, Betweenness, Closeness)._
- [[6_1_Markov_and_Random_Walks]] - _Random Walk, Modelli di Markov e Power Iteration._
- [[6_2_PageRank_and_HITS]] - _Algoritmi di Link Analysis: PageRank HITS e Personalized PageRank_
- [[6_3_Citation_Networks]] - _Co-Citation, Bibliographic Coupling._

## Strumenti per l'Analisi di Grafi

*Strumenti per l'analisi in-memory e la persistenza dei dati su larga scala.*

### Database a Grafo (Storage & Querying)

- [[7_Graph_Databases]] - _Introduzione ai DBMS a grafo._
- [[7_1_Neo4j]] - _Guida architetturale all'uso di Neo4j._
- [[7_2_Cypher]] - _Linguaggio di query Cypher._
- [[7_3_Graph_Algorithms_Neo4j]] - _Algoritmi di grafi eseguiti nativamente in Neo4j._
- [[7_4_Graph_Visualization_Neo4j]] - _Strumenti di visualizzazione integrati._

### In-Memory Analytics (Elaborazione Vettoriale)

- [[7_5_NetworkX]] - _Introduzione a NetworkX (Python)._
- [[7_6_Graph_Algorithms_NetworkX]] - _Implementazione algoritmica in NetworkX._
- [[7_7_Graph_Visualization_NetworkX]] - _Plotting e visualizzazione programmatica._

## Graph Machine Learning

*Estensione dei concetti topologici verso reti neurali e rappresentazioni latenti.*

- *(Placeholder per futuri appunti su GNN, Node Embeddings come Node2Vec, ecc.)*

---

## Riferimenti

- [Neo4j](https://neo4j.com/) - Sito ufficiale di Neo4j
- [Cypher](https://neo4j.com/developer/cypher/) - Documentazione ufficiale di Cypher
- [NetworkX](https://networkx.org/) - Sito ufficiale di NetworkX