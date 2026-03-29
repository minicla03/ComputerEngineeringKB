# Graph Storage

Parent: [[Graph_Analytics_MOC]]

## Densità del grafo

La **densità di un grafo** è definita come il rapporto tra il numero di archi presenti nel grafo e il numero massimo di archi che potrebbero essere presenti in un grafo completo con lo stesso numero di nodi. La formula per calcolare la densità di un grafo dipende dal tipo di grafo:

Per un grafo non orientato: $D_U = \frac{E}{max_U(V)} = \frac{2E}{V(V-1)}$
Per un grafo orientato: $D_D = \frac{E}{max_D(V)} = \frac{E}{V(V-1)} = \frac{1}{2} \cdot D_U(V)$

dove il massimo numero di archi in un grafo completo con $V$ nodi è dato da:

- Per un grafo non orientato: $max_U(V) = \binom{V}{2}= \frac{V(V-1)}{2}$
- Per un grafo orientato: $max_D(V) = 2 \binom{V}{2}= V(V-1) = 2 max_U(V)$

La misura di densità è compresa tra 0 e 1, dove 0 indica un grafo **grafo completamente sparso** e 1 indica un **grafo completo**. Se la densità è 0.5, significa che il grafo ha la metà degli archi possibili rispetto a un grafo completo con lo stesso numero di nodi e quindi è considerato un grafo **moderatamente denso**.

Nell'analisi spettrale, la densità si definise dall'analisi dell'**autovalore dominante** ($\lambda_1$) della matrice di adiacenza $A$.

L'autovalore massimo $\lambda_1(A)$, detto **raggio spettrale**, è il principale indicatore della densità. Esiste una relazione fondamentale tra $\lambda_1$ e il grado dei nodi:

$$d_{media} \leq \lambda_1 \leq d_{max}$$

All'aumentare del numero di archi, il valore di $\lambda_1$ cresce. Se il grafo è $k$-regolare (ogni nodo ha esattamente $k$ vicini), allora $\lambda_1 = k$.
Un $\lambda_1$ elevato indica che il grafo non è solo denso globalmente, ma possiede un "core" di nodi fortemente interconnessi. In pratica, la matrice "pesa" di più perché ci sono più connessioni che contribuiscono alla sua intensità trasformativa.

L'autovalore principale è direttamente proporzionale alla densità dei collegamenti. $\lambda_1 \approx \frac{2|E|}{|V|}$, corrisponde al grado medio del grafo. Più archi aggiungi al sistema, più alto sarà il valore di $\lambda_1$.
Se il grafo è regolare, questa approssimazione diventa un'uguaglianza esatta.
($\lambda_1 \approx |V|-1$). Quando l'autovalore massimo si avvicina al numero totale di nodi meno uno ($n-1$)- Il grafo è estremamente denso. Si sta approssimando un "grafo completo" (o clique), in cui ogni singolo nodo è connesso a tutti gli altri.
($\lambda_1 \approx 2$). Se $\lambda_1$ ha un valore molto basso, vicino a 2 (specialmente per grafi con molti nodi $n$). Il grafo è molto sparso. È probabile che il grafo sia un semplice ciclo o un cammino lineare. In queste strutture, ogni nodo ha solo 2 vicini (o meno), rendendo la rete estremamente "sottile" e fragile.

La densità del grafo è una misura importante per comprendere la struttura del grafo e può influenzare le prestazioni degli algoritmi di analisi dei grafi. Ci guida in sulla scelta della rappresentazione del grafo sul calcolatore.

## Rappresentazione dei grafi

![alt text](IMG_20260228_154123.jpg)

Abbiamo due requisiti fondamentali:

- avere lo spazio necessario per ospitare i tipi di grafici che incontreremo nelle applicazioni.
- sviluppare implementazioni efficienti in termini di tempo dei metodi di istanza dei grafici, i metodi di base di cui abbiamo bisogno per sviluppare client di elaborazione dei grafici.

Una **matrice di adiacenza**, una matrice booleana $V \times V$ dove l'elemento $A[v][w]$ è $1$ se esiste un arco tra $v$ e $w$, $0$ altrimenti.  L'accesso avvienenin tempo costante $O(1)$ per verificare l'esistenza di un arco specifico, o aggiungere un arco, ma tichiede spazio $\Theta(V^2)$. Anche per iterare sui vicini di un nodo richiede $O(V)$, indipendentemente dal numero effettivo di archi incidenti.

Un **array di archi**, utilizzando una classe `Edge`,ognuno dei quali contiene una coppia di interi $(u, v)$. Lo spazio utilizzato è esattamente proporzionale al numero di archi ($O(E)$). Quando dobbiamo sapere chi sono i vicini del nodo $v$ è necessatio scansionare l'intero array degli archi dall'inizio alla fine, con complessità nel caso peggiore di $O(E)$. 

Un **array di liste di adiacenza**, dmanteniamo un array di dimensione $V$, dove ogni cella $i$ punta a una lista concatenata contenente solo i vicini effettivi del nodo $i$.
Occupiamo solo $O(V + E)$, memorizzando solo ciò che esiste realmente e iterare sui vicini di un nodo in tempo proporzionale al suo grado, $O(d)$, dove $d$ è il numero di vicini del nodo.
Viene usata principalmente per la rappresentazione di grafi non densi.

Per aggiungere un arco che connette $v$ e $w$, aggiungiamo $w$ alla lista di adiacenza di $v$ e $v$ alla lista di adiacenza di $w$. Pertanto, ogni arco appare due volte nella struttura dati. Questa implementazione del grafo raggiunge le seguenti caratteristiche prestazionali:

![alt text](image-19.png){width=70% height=70%}

Anche per i grafi diretti, si usa la rappresentazione delle liste di adiacenza, in cui un arco $v \rightarrow w$ è rappresentato come un nodo di lista contenente $w$ nell'elenco concatenato corrispondente a $v$. Questa rappresentazione è essenzialmente la stessa dei grafi non orientati, ma è ancora più semplice perché ogni arco si verifica solo una volta.

![alt text](IMG_20260228_154053.jpg)

Un'altra rappresentazione di un grafo può avvenire tramite la modellazione degli edge, invece dei vertici.

![alt text](IMG_20260228_155713.jpg)

Quindi andiamo a modellare un grafo come una collezione di oggetti `Edge`, dove ogni Edge contiene informazioni sui vertici che collega e, eventualmente, altri attributi come il peso dell'arco. In questo modo, possiamo rappresentare anche grafi pesati.

Potremmo anche con la rappresentazione a matrice di adiacenza, in cui, invece di usare valori booleani per gli edge, mettiamo il peso di quell'edge. Invece, nella rappresentazione a liste di adiacenza, possiamo definire un nodo che contiene sia un vertice che un peso da inserire nelle liste di adiacenza.

![alt text](IMG_20260228_155741.jpg)

![alt text](IMG_20260228_155821.jpg){width=60% height=60%}

Lo stesso vale per i grafi diretti, dove ogni arco $v \rightarrow w$ è rappresentato come un nodo di lista contenente $w$ e il peso dell'arco nell'elenco concatenato corrispondente a $v$.

![alt text](IMG_20260228_155909.jpg)

![alt text](IMG_20260228_155930.jpg)

![alt text](IMG_20260228_155955.jpg){width=60% height=60%}

Lo svantaggio di questa rappresentazione è che, se il grafo è molto denso, potremmo finire con molte voci nella lista di adiacenza, rendendo l'iterazione attraverso i vertici adiacenti più costosa. Tuttavia, per grafi più sparsi, questa rappresentazione è efficiente in termini di spazio e tempo.
