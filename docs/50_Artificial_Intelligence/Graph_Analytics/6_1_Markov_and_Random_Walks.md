# 6_1_Markov_and_Random_Walks

Parent: [[6_Centrality_Measures]]

## Markov Chains

Una **Markovian chain** è un modello matematico di un fenomeno stocastico che evolve nel tempo (discreto o continuo) un cui la **probabilità di transizione** da uno stato ad un altro dipende solo dallo stato attuale e non da come si è arrivati a quello stato.

!!!note Propretà di Markov
    La **memoria limitata** (memoryless) è la caratteristica  di una catena di Markov, che implica che il futuro è indipendente dal passato dato il presente.

Una catrna di markov è definita da tre componenti:

1. **Spazio degli Stati ($S$):** L'insieme di tutte le possibili configurazioni del sistema. Applicato ai grafi, ogni nodo rappresenta uno stato discreto.
2. **Transizioni:** I passaggi da uno stato all'altro, che in un grafo corrispondono direttamente agli archi che collegano i nodi.
3. **Matrice di Transizione ($A$):** Una matrice stocastica in cui l'elemento $A_{ij}$ quantifica la probabilità di transitare dallo stato $i$ allo stato $j$ in un singolo passo.

Data una sequenza di variabili aleatorie $\{X_0, X_1, X_2, \dots, X_t\}$, il processo è formalmente markoviano se rispetta l'equazione:
$$P(X_{t+1} = j \mid X_t = i, X_{t-1} = i_{t-1}, \dots, X_0 = i_0) = P(X_{t+1} = j \mid X_t = i)$$

Una catena di Markov è **omogenea** se un processi in cui la probabilità di transizione al tempo $t_i$ non dipende dal tempo stesso, ma solo dallo stsato del sistema al tempo predente $S(t_{i-1})$. Se è omogenea a stati finiti, la catena di markov può essere rappresentata dalla **matreice di transizione** $A \in \R^{N \times N}$, dove $N$ è il numero di stati. Insieme alla matrice di transizione, si definisce anche il **vettore di probabilità iniziale** $v_0 \in \R^N$ che definisce le probabilià che la catena inizi in ciascuno degli stati.

Gli elementi della matrice rapprenentano le probabilità di transizione tra stati, e ogni riga della matrice deve sommare a 1, riflettendo la natura stocastica del processo. Le probabilità di transizione nella diagonale principale rappresentano la probabilià di rimanere nello stesso stato, mentre le probabilità fuori diagonale rappresentano la probabilità di transizione verso stati diversi.

L'avanzamento del processo stocastico di un singolo passo, dal tempo $t_i$ al tempo $t_{i+1}$, si definisce attraverso la seguente moltiplicazione matriciale:

$$v_{i+1} = A^T \times v_i$$

Si ottiene così il **vettore di Stato ($v_{i+1}$)**, sempre un vettore colonna di dimensione $N$ che fotografa lo stato del sistema al tempo $t_i$, indicando la distribuzione di probabilità di trovarsi in ciascun nodo. La somma dei suoi elementi (norma $L_1$) è sempre $1$. Spesso si inizializza uniformemente a $[1/N, 1/N, \dots, 1/N]^T$.

Questo prodotto matriciale rappresenta l'evoluzione del sistema, con la matrice di transizione che agisce come un operatore lineare che trasforma la distribuzione di probabilità da uno stato all'altro. Iterando questo processo, si può osservare come la distribuzione di probabilità evolve nel tempo, e in molti casi converge a una distribuzione stazionaria, che è un punto fisso del processo.

!!!note Distribuzione di stato stazionario
    Si tratta di una distribuzione verso cui la catena converge, indipendentemente dallo stato iniziale, all'aumentare del numero di passi. Quindi, se si continua ad applicare la matrice di transizione, il vettore di stato si stabilizzerà su questa distribuzione stazionaria, che rappresenta la probabilità di trovarsi in ciascuno stato dopo un numero infinito di passi. La distribuzione stazionaria è un punto fisso del processo, soddisfacendo l'equazione $v = A^T v$.

L'applicazione iterativa e ininterrotta di questa equazione, calcolando il vettore al tempo $t_{i+1}$ usando il vettore al tempo $t_i$, prende il nome di **Power Iteration**. 

L'algoritmo procede ricalcolando il vettore di stato e arrestandosi solo quando viene raggiunta la convergenza.

## Random Walks

La catena di Markov può essere rappresentata come un grafo diretto e quindi con la matrice di adiecenza normalizzata di un grafo per ottenere la matrice di transizione. In questo contesto, il processo di Markov prende il nome di **Random Walk**.

!!!note Random Walk
    Un **Random Walk** è un processo stocastico che descrive un percorso costituito da una successione di passi casuali su un grafo. In un random walk, a ogni passo, si sceglie casualmente uno dei nodi adiacenti al nodo corrente e ci si sposta verso quel nodo.

Per derivare la matrice di transizione da un grafo, è necessario normalizzare la matrice di adiacenza del grafo in modo che ogni riga sommi a 1, trasformando così i pesi degli archi in probabilità di transizione.

### Random Surfing e Teletrasporto

Il **Random Surfing** è una variante del random walk che introduce un meccanismo di teletrasporto per superare i limiti topologici intrinseci delle reti complesse, come i *dead end* (nodi senza uscite) e le *spider trap* (sottografi fortemente connessi che intrappolano il random walker).

Per superare questi problemi, si regolarizza l'equazione introducendo il parametro di teletrasporto $\alpha$. L'equazione di aggiornamento generale diventa una combinazione lineare:

$$v_{i+1} = (1-\alpha) A^T v_i + \alpha \begin{bmatrix} \frac{1}{N} \\ \vdots \\ \frac{1}{N} \end{bmatrix}$$

* **Il primo termine** $(1-\alpha) A^T v_i$ modella la normale navigazione strutturale seguendo gli archi uscenti con una probabilità attenuata.
* **Il secondo termine** $\alpha [\frac{1}{N}, \dots, \frac{1}{N}]^T$ funge da rumore di fondo uniforme, distribuendo la probabilità di un salto casuale equamente su tutti gli $N$ nodi del grafo, garantendo l'irriducibilità della matrice. 
* $\alpha$ agisce come un meccanismo di regolarizzazione, assicurando che il processo di random walk non rimanga intrappolato in componenti fortemente connesse o nodi senza uscite, e garantendo la convergenza a una distribuzione stazionaria unica anche in grafi con topologie complesse.  
