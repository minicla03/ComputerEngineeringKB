# Graph Connettivity

Parent: [[0_Graph_Analytics_MOC]]

La **connettività** è la proprietà che definisce quanto un grafo sia "unito" o quanto sia facile muoversi tra i suoi vertici.

## Connettività nei grafi non orientati

Un grafo non orientato $G = (V, E)$ si dice **connesso** se, per ogni coppia di vertici distinti $u, v \in V$, esiste almeno un **cammino** (*path*) che li congiunge.

Un grafo si dice **non connesso** (o disconnesso) se esiste almeno una coppia di vertici $(u, v)$ tra i quali non vi è alcun cammino.

Quando un grafo non è connesso, la sua struttura si presenta frammentata eil grafo può essere infatti visto come l'unione disgiunta di più "isole", chiamate **componenti connesse**.

Una **componente connessa** di un grafo $G$ è un sottografo connesso di $G$ che non è un sottografo proprio di un altro sottografo connesso di $G$. In altri termini, una componente connessa di un grafo $G$ è un sottografo connesso massimale di $G$.
"Massimale" significa che non è possibile aggiungere un altro vertice del grafo originale a quel sottografo senza perdere la proprietà di connettività.

## Connettività nei grafi orientati

Un grafo orientato $G = (V, E)$ si dice **fortemente connesso** se, per ogni coppia di vertici $(u, v) \in V$, esiste sia un cammino orientato da $u$ a $v$, sia un cammino orientato da $v$ a $u$.

Le **Componenti Fortemente Connesse (SCC)** sono sottografi orientati massimali che risultano fortemente connessi.

Un grafo orientato si dice **debolmente connesso** se il suo **grafo non orientato sottostante** (ottenuto ignorando la direzione degli archi) è connesso.
In altre parole, esiste un percorso tra ogni coppia di nodi, ma non necessariamente rispettando il verso delle frecce. 

Se un grafo non è nemmeno debolmente connesso, si dice semplicemente **disconnesso**.

Per trovare le componenti fortemente connesse si utilizzano tipicamente l'**algoritmo di Tarjan** o l'**algoritmo di Kosaraju**, entrambi basati su una doppia visita DFS con complessità $O(|V| + |E|)$.

* **Condensazione di un Grafo**: È possibile creare un "grafo delle componenti" dove ogni nodo rappresenta una SCC. Il grafo risultante è sempre un **DAG** (Directed Acyclic Graph), proprietà utilissima per ottimizzare i processi di calcolo distribuito.

## Analisi della connettività

!!!note
    Un **taglio** è un insieme di vertici o di archi la cui rimozione aumenta il numero di componenti connesse del grafo. In altre parole, un taglio è un insieme di elementi (vertici o archi) che, se rimossi, disconnettono il grafo.

Il taglio può avvenire sia a livello di vertici che di archi:

- **Vertici di Taglio** (o **Punti di Articolazione**): Sono vertici la cui rimozione (insieme a tutti gli archi incidenti) produce un sottografo con un numero maggiore di componenti connesse. La rimozione di un vertice di taglio da un grafo connesso genera un sottografo non connesso.
- **Archi di Taglio** (o **Ponti**): Un arco la cui rimozione produce un grafo con più componenti connesse rispetto al grafo originale.

Per quantificare la robustezza di un grafo, definiamo i seguenti parametri:

- **Connettività dei vertici $\kappa(G)$**: Il numero minimo di vertici che devono essere rimossi per disconnettere il grafo o ridurlo a un singolo vertice.
- **Connettività degli archi $\lambda(G)$**: Il numero minimo di archi che devono essere rimossi per disconnettere il grafo.

Esistono due approcci principali, uno algoritmico e uno algebrico:

- **Approccio Algoritmico (BFS/DFS)**: Partendo dal nodo sorgente, si esplora il grafo "a macchia d'olio" (Breadth-First Search) o in profondità (Depth-First Search). Tutti i nodi marcati come "visitati" alla fine del processo costituiscono l'insieme dei nodi raggiungibili. La complessità è $O(|V| + |E|)$.
- **Approccio Algebrico (Matrice di Adiacenza)**: Se analizziamo la matrice $A$, un nodo $j$ è raggiungibile dal nodo $i$ in esattamente $k$ passi se l'elemento $(i, j)$ della matrice $A^k$ è maggiore di zero:$$(A^k)_{ij} > 0$$

L'analisi della connettività serve a trovare i punti deboli. Se un sistema è connesso, ma la rimozione di un singolo nodo (un server, un ponte, un manager in un'azienda) lo divide in due sottosistemi isolati, quel nodo è un punto di articolazione. Ad esempio, progettare sistemi "fault-tolerant" dove, per interrompere il servizio, devono fallire contemporaneamente almeno $k$ componenti (connettività $k$-nodale).

## Max-Flow Min-Cut Theorem

Questo teorema serve per risolvere problemi di ottimizzazione legati al flow dei flussi in un grafo. Una rete di flusso è un multigrafo ponderato e diretto.

Il **flusso** è definito come uno spostamento di una quantità da un nodo a un altro lungo un arco. Formalmente, un flusso è una funzione $f: E \rightarrow \R^+$ che assegna a ogni arco $(u, v)$ un valore non negativo, rappresentando la quantità di "flusso" che attraversa quell'arco.

Il flusso deve rispettare due condizioni:

1. **Capacità**: Il flusso su un arco non può superare la capacità dell'arco stesso. Rappresenta il massimo flusso che può passare attraverso un arco.Formalmente, se la capacità di un arco è indicata come $c(u, v)$ e il flusso attraverso quell'arco è $f(u, v)$, allora deve soddisfare la condizione $$0 ≤ f(u, v) ≤ c(u, v)$$ per tutti gli archi $(u, v)$ all'interno della rete.
2. **Conservazione del flusso**: Per ogni nodo, ad eccezione della sorgente e del pozzo, la quantità totale di flusso che entra deve essere uguale alla quantità totale di flusso che esce. Ciò garantisce che il flusso continui senza interruzioni e non si accumuli o dissipi all'interno della rete, nonostante sia possibile consentire l'accumulo di flusso se il sistema lo richiede. Matematicamente, per ogni nodo $u$ e i nodi adiacenti rappresentati e raggruppati dai supernodi $v$ e $w$, la proprietà di conservazione del flusso è espressa come:$$\sum_{v} f(u, v) = \sum_{w} f(w, u)$$.

!!!theorem Max-Flow Min-Cut Theorem
    Il teorema afferma che in una rete di flusso, il **flusso massimo** che può passare da una sorgente (source) a una destinazione (target o sink) è uguale alla **capacità del taglio minimo** (min-cut) necessario per separare completamente la sorgente dalla destinazione. Formalmente, se $G$ è una rete di flusso con sorgente $s$ e destinazione $t$, allora:$$\text{Max-Flow}(s, t) = \text{Min-Cut}(s, t)$$
    - Massimo Flusso ($Max-Flow$): Rappresenta la quantità massima di "entità" (dati, acqua, traffico) che può transitare nella rete rispettando i limiti di capacità di ogni arco.

Questo teorema viene utilizzato per analizzare la resilienza e al'affidabilità di una rete. Per l'analisi della resilienza,si deve ricercare il numero minimo di archi e nodi che se rimossi disconnetto il grafo.

## Misure di connettività

### Eccentricità, raggio e diametro

!!!note Eccentricità
    L'eccentricità di un vertice $v$ in un grafo connesso è la distanza massima tra $v$ e qualsiasi altro vertice del grafo. Formalmente, è definita come:$$\epsilon(v) = \max_{u \in V} d(v, u)$$ Dove $d(v, u)$ è la distanza tra i vertici $v$ e $u$.
    In un grafo disconnesso, se un nodo non può raggiungerne un altro, la sua eccentricità diventa formalmente infinita.

!!!note Raggio
    Il raggio di un grafo $G$ è definito come l'eccentricità minima fra tutti i nodi del grafo. Formalmente:$$r(G) = \min_{v \in V} \epsilon(v)$$ Se il grafo è disconesso, il raggio è considerato infinito, perche non esiste nessun nodo che permette di raggiungere tutti gli altri nodi del grafo. 

!!!note Diametro
    Il diametro di un grafo $G$ è definito come la masssima eccentricità di un grafo connesso, cioè è la distanza più lunga tra qualunque coppia di vertici. Formalmente:$$d(G) = \max_{v \in V} \epsilon(v)$$ Anche in questo caso, se il grafo è disconesso, il diametro è considerato infinito, perchè non esiste nessuna coppia di nodi che permette di raggiungere tutti gli altri nodi del grafo.

### Conduttanza

La **conduttanza** di un grafo  è un parametro metrico che misura la "qualità" di un taglio nel grafo, indicando quanto sia difficile per un _walk_ uscire da un determinato insieme di nodi.

!!!note Conduttanza per i grafi non orientati
    Sia $G = (V, E)$ un grafo non orientato e $S \subset V$ un sottoinsieme di vertici. La conduttanza di $S$, indicata con $\phi(S)$, è definita come: $$\phi(S) = \frac{|\partial(S)|}{\min(\text{vol}(S), \text{vol}(V \setminus S))}$$ Dove:
    - **$|\partial(S)|$**: è il numero di archi che collegano un nodo in $S$ a un nodo fuori da $S$ (il "taglio").
    -  **$\text{vol}(S)$**: è il volume di $S$, ovvero la somma dei gradi dei nodi appartenenti a $S$ ($\sum_{v \in S} d(v)$).
    - **$\text{vol}(V \setminus S)$**: è il volume del complemento di $S$, ovvero la somma dei gradi dei nodi che non appartengono a $S$.
  
!!!note Conduttanza per i grafi diretti
    Per i grafi diretti, la conduttanza di un sottoinsieme $S$ è definita come:$$\phi_D(S)= \frac{|{\partial}_{out}(S)|}{\min( vol_{out}(S), vol_{out}(V \setminus S))}$$ Dove:
    - **$|{\partial}_{out}(S)|$**: è il numero di archi che escono da $S$ verso $V \setminus S$.
    - **$vol_{out}(S)$**: è la somma dei gradi in uscita dei nodi in $S$ ($\sum_{v \in S} d_{out}(v)$).
    - **$vol_{out}(V \setminus S)$**: è la somma dei gradi in uscita dei nodi in $V \setminus S$ ($\sum_{v \in V \setminus S} d_{out}(v)$).

In termini intuitivi, una bassa conduttanza indica la presenza di un "collo di bottiglia": un insieme di nodi densamente connessi tra loro ma scarsamente connessi al resto del grafo; mentre una conduttanza elevata suggerisce che il sottoinsieme è ben integrato con il resto del grafo, senza barriere significative alla diffusione o al flusso di informazioni.

Partendo da un grafo non orientato, e considerando il suo equivalente orientato è possibile calcolare la conduttanza con la formula per i grafi orientati.

!!!note Conduttanza globale
    La conduttanza dell'intero grafo $G$ è il valore minimo di $\phi(S)$ calcolato su tutti i possibili sottoinsiemi $S$ non banali ($\emptyset \subseteq S \subseteq$ V): $$\phi(G) = \min_{S \subseteq V} \phi(S)$$

L'analisi della conduttanza permette di caratterizzare la struttura globale del network:

- **Community Detection:** I cluster o le comunità in un grafo sono spesso identificati come sottoinsiemi di nodi con bassa conduttanza.
- **Mixing Time:** Nelle catene di Markov e nei cammini casuali (random walks), la conduttanza determina la velocità con cui il processo raggiunge la distribuzione stazionaria. Una conduttanza elevata implica che il cammino casuale "esplora" rapidamente l'intero grafo.
- **Robustezza:** Un grafo con alta conduttanza è generalmente più resiliente a guasti mirati, poiché non presenta divisioni nette o ponti critici.

!!!quote Secondo la teoria spettrale, la conduttazza, dipende da $\lambda_1$, il secondo autovalore più piccolo del **Laplaciano normalizzato** del grafo, vale la seguente relazione: $$\frac{\lambda_1}{2} \leq \phi(G) \leq \sqrt{2\lambda_1}$$ Questa disuguaglianza permette di approssimare il valore della conduttanza (che è computazionalmente difficile da calcolare esattamente, essendo un problema NP-hard) analizzando semplicemente lo spettro della matrice Laplaciana. È il fondamento teorico del **Clustering Spettrale**.

### Diametro Medio

L'**Average Diameter** misura l'efficienza del trasporto di informazioni all'interno della rete. Rappresenta la media delle distanze più brevi tra tutte le coppie di nodi possibili.

Dato un grafo $G = (V, E)$ con $n$ nodi, sia $d(v_i, v_j)$ la distanza geodetica (il cammino minimo) tra il nodo $i$ e il nodo $j$:

$$L = \frac{1}{n(n-1)} \sum_{i \neq j} d(v_i, v_j)$$

Un valore di $L$ basso indica che la rete è "stretta" (proprietà Small-World), ovvero che ogni nodo può raggiungerne un altro con pochissimi passaggi intermedi. Un valore di $L$ elevato suggerisce che la rete è "lunga" o "sparsa", con molti nodi che richiedono numerosi passaggi per essere raggiunti.

Se il grafo non è connesso, il diametro è tecnicamente infinito. In questi casi si calcola la media solo sulle componenti connesse.

!!!note Small World Graphs
    Sono reti caratterizzate da un coefficiente di clustering relativamente alto e un diametro medio ($L$) ridotto, indicando che la maggior parte dei nodi può essere raggiunta con pochi passaggi nonostante la forte aggregazione locale.

## Cliques

Una **clique** è un insieme di $S \subset V$ di vertici in un grafo non orienteato per cui ogni coppia di vertici in $S$, esiste un arco che li collega, quindi sia completo.

!!!note Clique
    Una clique in un grafo indiretto $G = (V, E)$ è un sottoinsieme dell'insieme dei vertici $C ⊆ V$, tale che per ogni due vertici in $C$, esiste uno spigolo che li connette. Questo equivale a dire che il sottografo indotto da $C$ è completo.

<div align="center">
    <img src="image-20.png" alt="clique" width="50%" height="50%">
</div>

### K-core decomposition

Il **k-core** di un grafo è un sottografo massimale in cui ogni nodo ha almeno $k$ connessioni con altri nodi all'interno del sottografo, indipendentemente da quante connessioni abbia al di fuori del sottografo stesso.

<div align="center">
    <img src="image-4.png" alt="k-core decomposition" width="50%" height="50%">
</div>

!!!note K-core decomposition steps
    Per ottenere il $k$-core di un grafo, si procede come segue:
    1. Si rimuovono tutti i nodi con grado inferiore a $k$.
    2. Si ricalcolano i gradi dei nodi rimanenti (poiché la rimozione di un nodo riduce il grado dei suoi vicini).
    3. Si ripete il processo finché tutti i nodi nel grafo rimanente hanno grado $\geq k$.

L'algoritmo di decomposizione in $k$-core è efficiente, con una complessità di $O(|V| + |E|)$, poiché ogni nodo e ogni arco viene esaminato al massimo una volta durante il processo di rimozione.

!!!warning
    Ogni clique di dimensione $k$ è contenuta in un $(k-1)$-core.

Ad esempio, una clique di 4 nodi (dove ogni nodo ha grado 3) è necessariamente parte di un 3-core. Tuttavia, un 3-core non è necessariamente una clique: può essere un insieme molto vasto di nodi dove ognuno ha semplicemente 3 vicini, risultando in una struttura molto più "sparsa" di una clique.
