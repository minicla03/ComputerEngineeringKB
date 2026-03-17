# Centrality Measures

Parent: [[5_Graph_Connettivity]]

!!!note Centralità
    La **centralità** esprime l'importanza di un nodo basandosi sul suo ruolo nel "mantenere il grafo connesso" o sulla sua facilità di accesso agli altri nodi.

!!!note Prestigio
    Il **prestigio** è una misura di importanza calcolata solo per reti dirette, poiché la direzione del legame è una proprietà fondamentale della relazione. Si basa sui cosiddetti "in-links".

## Metriche di centralità per grafi non orientati

### Degree Centrality

La **degree centrality** di un nodo $v$ è definita come il numero di vicini (nodi adiacenti) a cui è direttamente connesso

### Closeness Centrality

La **Closeness Centrality** misura quanto un nodo $v_i$ è "vicino" a tutti gli altri nodi della rete. Un nodo con alta closeness può diffondere informazioni o influenzare il resto della rete molto più velocemente rispetto agli altri.

Per un nodo $v_i$, la closeness è definita come l'inverso della somma delle distanze da quel nodo a tutti gli altri:

$$C(v_i) = \frac{n-1}{\sum_{j \neq i} d(v_i, v_j)}$$

* **Normalizzazione:** Il fattore $(n-1)$ al numeratore serve a normalizzare il valore tra 0 e 1, rendendo la misura confrontabile tra grafi di dimensioni diverse.
* **Interpretazione:** Un valore elevato indica che il nodo è situato al "centro" del grafo.

!!!warning Il legame tra Wiener Index e Closeness
    Esiste una relazione inversa tra la somma delle centralità e il Wiener Index. Poiché il denominatore della Closeness di un nodo $i$ è la somma delle distanze $D_i = \sum_{j} d(v_i, v_j)$, si può notare che la somma di tutti i $D_i$ è esattamente il doppio del Wiener Index:$$\sum_{i=1}^{n} D_i = 2W(G)$$

### Betweenness Centrality

La **Betweenness Centrality** ($g(v)$) è una misura di centralità che quantifica l'importanza di un nodo agendo come "ponte" o "intermediario" tra le altre parti di un grafo. A differenza della Closeness (che misura la vicinanza), la Betweenness identifica i nodi che controllano il flusso di informazioni all'interno della rete.

Un nodo con alta Betweenness si trova su molti **cammini minimi** (*shortest paths*) tra coppie di altri nodi. Se tale nodo venisse rimosso, molte comunicazioni nel grafo verrebbero interrotte o dovrebbero percorrere tragitti molto più lunghi.

Per un nodo $v$, la Betweenness Centrality è definita come la somma del rapporto tra i cammini minimi che passano per $v$ e il totale dei cammini minimi tra ogni coppia di nodi $s$ e $t$:

$$g(v) = \sum_{s \neq v \neq t \in V} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

Dove:

* $\sigma_{st}$: è il numero totale di cammini minimi dal nodo $s$ al nodo $t$.
* $\sigma_{st}(v)$: è il numero di tali cammini minimi che passano attraverso il nodo $v$.

Per rendere il valore confrontabile tra grafi di diverse dimensioni, si divide il risultato per il numero di coppie di nodi possibili (escluso $v$ stesso). Per un grafo non orientato:

$$g_{norm}(v) = \frac{g(v)}{(n-1)(n-2)/2}$$

## Metriche di prestigio per grafi orientati

Nei grafi diretti, l'importanza è legata alla direzione dei legami (in-links), spesso interpretata come una forma di "status":

### In-Degree Prestige

La **in-degree prestige** di un nodo $v$ è definita come il numero di archi che entrano in $v$. Un nodo con un alto in-degree è considerato prestigioso perché riceve molte connessioni da altri nodi.

### Out-Degree Prestige

La **out-degree prestige** di un nodo $v$ è definita come il numero di archi che escono da $v$. Un nodo con un alto out-degree è considerato influente perché si connette a molti altri nodi.

### Influence Domain

L'Influence Domain di un nodo $i$, indicato come $|I_i|$, rappresenta la portata della sua autorità all'interno della rete.  È il numero di nodi che possono raggiungere il nodo $i$ seguendo un percorso diretto.

Più ampio è il dominio di influenza, più il nodo è considerato un "punto di riferimento" o una destinazione per gli altri membri del network.

### Proximity Prestige

Il **Proximity Prestige ($PP$)** è una metrica più sofisticata che perfeziona il concetto di influenza, integrando non solo la quantità di nodi che raggiungono $i$, ma anche la "vicinanza" (distanza) di questi nodi.

$$PP(i)=\frac{|I_{i}|/(n-1)}{\sum_{j\in I_{i}}d(j,i)/|I_{i}|}$$

I componenti della formula sono:

* $|I_i|$: il numero di nodi nel dominio di influenza di $i$.
* $(n-1)$: il numero totale degli altri nodi nel grafo.
* $d(j,i)$: la lunghezza del cammino minimo diretto dal nodo $j$ al nodo $i$.

In sostanza, il Proximity Prestige è il rapporto tra:

1. **La frazione di nodi** che possono raggiungere $i$ rispetto al totale dei nodi possibili.
2. **La distanza media** che questi nodi devono percorrere per arrivare a $i$.

Un alto valore di $PP$ indica che il nodo è raggiungibile da una vasta porzione della rete attraverso percorsi molto brevi.

## H-Index

L'**H-Index** (o indice di Hirsch) è una metrica utilizzata per valutare il prestigio e l'autorità di un autore o di una rivista scientifica. Il suo scopo principale è creare un equilibrio tra due fattori spesso considerati separatamente: la **produttività** e l'**impatto**.

L'indice si basa su due pilastri:

1. **Produttività**: rappresenta il numero totale di pubblicazioni realizzate da un autore.
2. **Impatto**: rappresenta il numero di citazioni ricevute dai lavori pubblicati.

!!!note 
    Un autore possiede un indice pari a **$h$** se ha pubblicato almeno $h$ articoli, ognuno dei quali è stato citato da altri lavori almeno $h$ volte. In sostanza, l'H-index identifica il punto di equilibrio dove il numero d'ordine dell'articolo (ordinato per citazioni decrescenti) incrocia il numero di citazioni ricevute.

!!!example
    **Esempio A**: Un autore con articoli citati 10, 8, 5, 4 e 3 volte ha un **H-index di 4**. Infatti, ci sono 4 lavori con almeno 4 citazioni.

    **Esempio B**: Un autore con citazioni 25, 8, 5, 3 e 3 ha un **H-index di 3**. Nonostante il record di 25 citazioni su un singolo lavoro, solo 3 articoli hanno ricevuto almeno 3 citazioni.
