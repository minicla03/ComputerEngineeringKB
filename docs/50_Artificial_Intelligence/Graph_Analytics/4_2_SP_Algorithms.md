# Shortest Path Algorithms

Parent: [[4_1_Shortest_Path]]

## Edge Relaxation

Il **rilassamento di un arco** (edge relaxation) è l'operazione fondamentale su cui si basano la maggior parte degli algoritmi di ricerca dei cammini minimi su grafo.Consiste nel verificare se è possibile migliorare il cammino minimo attualmente noto verso un nodo destinazione, passando attraverso un nodo intermedio adiacente.

!!!note Edge Relaxation
    Sia $G = (V, E)$ un grafo pesato, dove $w(u, v)$ rappresenta il costo (o peso) dell'arco diretto dal nodo $u$ al nodo $v$.
    Sia $d(v)$ la stima corrente del costo del cammino minimo dal nodo sorgente $S$ al nodo $v$. All'inizio dell'esplorazione, tipicamente $d(S) = 0$ e per tutti gli altri nodi $d(v) = \infty$. Sia $\pi(v)$ il predecessore del nodo $v$ nell'albero dei cammini minimi.

    L'operazione di rilassamento per l'arco $(u, v)$ si articola nei seguenti due passaggi logici:

    1.  **Test della condizione:** Si verifica se passare per $u$ offre un percorso strettamente migliore verso $v$ rispetto a quello attualmente memorizzato. La condizione è:
        $$d(u) + w(u, v) < d(v)$$

    2.  **Aggiornamento:** Se la disuguaglianza è verificata, la stima per $v$ viene sovrascritta e si traccia la nuova derivazione logica:
        $$d(v) = d(u) + w(u, v) \\ \pi(v) = u$$

Quando questo aggiornamento avviene, diciamo che l'arco $(u, v)$ è stato *rilassato* con successo. Il termine deriva dalla matematica applicata: stiamo "allentando" il limite superiore della stima della distanza, avvicinandolo al suo vero valore minimo ottimale.

Sebbene l'operazione matematica sia identica, la strategia con cui gli algoritmi decidono *quali* archi rilassare e *in che ordine* ne determina l'architettura e la complessità computazionale.

## Algoritmo di Dijkstra

Visita il grafo partendo dal nodo sorgente, espandendo sempre il nodo con il costo cumulativo minore. Utilizza tipicamente una coda di priorità (min-heap) per selezionare in modo efficiente il prossimo vertice da esplorare.

* **Adatto per:** Problemi Single-Source Shortest Path (SSSP) su grafi con pesi non negativi.
* **Problemi:** Fallisce matematicamente se vi sono archi con peso negativo. Esplora lo spazio in modo radiale ("cieco"), il che lo rende inefficiente per ricerche point-to-point su reti ampie.
* **Complessità:** $O((V + E) \log V)$ utilizzando un min-heap standard (dove $V$ sono i vertici ed $E$ gli archi).
* **Applicazioni in Graph Analysis:** Calcolo della *Closeness Centrality* in reti sociali (per capire quanto velocemente le informazioni si propagano da un nodo), protocolli di routing OSPF, o come baseline robusta per metriche di distanza spaziale.

!!!tip Algoritmo
    L'algoritmo si basa su un approccio *greedy* e utilizza una struttura dati a coda di priorità (min-heap) per gestire il fronte di esplorazione.
        1.  **Inizializzazione:** Assegna una distanza provvisoria $d = 0$ al nodo sorgente e $d = \infty$ a tutti gli altri nodi. Inserisce tutti i nodi nella coda di priorità.
        2.  **Estrazione:** Estrae il nodo $u$ con la distanza minima corrente.
        3.  **Relaxation:** Per ogni nodo vicino $v$ di $u$, calcola la distanza potenziale passante per $u$: $d_{new} = d(u) + w(u, v)$, dove $w$ è il peso dell'arco.
        4.  **Aggiornamento:** Se $d_{new} < d(v)$, aggiorna la distanza $d(v) = d_{new}$ e aggiorna la posizione di $v$ nella coda di priorità.
        5.  **Terminazione:** Il processo si ripete finché la coda non è vuota o il nodo destinazione non viene estratto.

Applica il rilassamento in modo *greedy* ed espansivo. Seleziona il nodo $u$ con $d(u)$ globale minimo non ancora processato e rilassa tutti i suoi archi uscenti $(u, v)$ una sola volta. Su grafi con pesi positivi, questo è sufficiente a garantire che una volta estratto $u$, il suo $d(u)$ sia definitivo e invariabile.

## Algoritmo di Bellman-Ford

Invece di affidarsi a una selezione "avida", rilassa iterativamente tutti gli archi del grafo per $V-1$ volte, propagando progressivamente i costi minimi. Una $V$-esima iterazione serve per identificare eventuali miglioramenti, sintomo di un ciclo negativo.

* **Adatto per:** SSSP su grafi dove i pesi degli archi possono essere negativi. Fondamentale per il rilevamento di cicli di costo negativo.
* **Problemi:** Computazionalmente molto più pesante di Dijkstra. Da evitare se si ha la certezza di non avere pesi negativi.
* **Complessità:** $O(V \cdot E)$.
* **Applicazioni in Graph Analysis:** Arbitraggio finanziario in grafi delle valute (dove i tassi di cambio logaritmici negativi formano cicli che indicano un profitto privo di rischio).

!!!tip Algoritmo
    A differenza di Dijkstra, Bellman-Ford non è avido. Esamina iterativamente e sistematicamente l'intero spazio degli archi, garantendo la propagazione corretta anche in presenza di debiti (pesi negativi).
    1.  **Inizializzazione:** Imposta le distanze a $\infty$ tranne la sorgente ($0$).
    2.  **Iterazione di Relaxation:** Per $|V| - 1$ volte (dove $|V|$ è il numero dei vertici), scorre *tutti* gli archi $(u, v)$ del grafo e applica la condizione di relaxation: se $d(u) + w(u, v) < d(v)$, aggiorna $d(v)$. Il limite $|V| - 1$ deriva dal fatto che il cammino minimo in un grafo senza cicli negativi può contenere al massimo $|V| - 1$ archi.
    3.  **Verifica Cicli Negativi:** Esegue una $|V|$-esima iterazione su tutti gli archi. Se è ancora possibile effettuare una relaxation, significa che il grafo contiene un ciclo di costo negativo, rendendo matematicamente indefinita una soluzione di cammino minimo.

Esegue un rilassamento "forzato" e iterativo su tutti gli archi del grafo ripetutamente per $V-1$ volte, senza fare assunzioni di ottimalità locale.

## Algoritmo di Floyd-Warshall

Utilizza la programmazione dinamica tramite una matrice di adiacenza. Per ogni coppia di nodi $(i, j)$, verifica iterativamente se un nodo intermedio $k$ offre un percorso più economico rispetto al cammino diretto o precedentemente calcolato.

* **Adatto per:** Problemi All-Pairs Shortest Path (APSP) su grafi densi o di piccole dimensioni.
* **Problemi:** Ha una complessità spaziale quadratica e temporale cubica. Lanciarlo su un grafo di milioni di nodi equivale a testare i limiti termici del proprio hardware.
* **Complessità:** $O(V^3)$.
* **Applicazioni in Graph Analysis:** Calcolo del diametro della rete, analisi di topologie complete e pre-computazione rapida delle distanze tra tutti i cluster in reti strutturate compatte.

!!!tip
    È un classico algoritmo di programmazione dinamica che costruisce la soluzione iterando sui possibili nodi intermedi.
    1.  **Inizializzazione:** Costruisce una matrice delle distanze $D$ di dimensione $|V| \times |V|$, inizializzata con i pesi degli archi (o $\infty$ se i nodi non sono adiacenti, e $0$ sulla diagonale).
    2.  **Costruzione (Tre cicli annidati):** Utilizza un ciclo esterno per un nodo intermedio $k$, e due cicli interni per le coppie di nodi sorgente $i$ e destinazione $j$.
    3.  **Aggiornamento DP:** Per ogni terna, applica l'equazione di Bellman: 
        $$D[i][j] = \min(D[i][j], D[i][k] + D[k][j])$$ Sostanzialmente, si chiede: "Il percorso da $i$ a $j$ è più economico se passo attraverso $k$?". Alla fine dei cicli, la matrice contiene i cammini minimi tra ogni coppia di nodi.

Non rilassa i singoli archi nel senso stretto del termine, ma esegue un "rilassamento generalizzato dei cammini" tramite programmazione dinamica. L'equazione di aggiornamento $D[i][j] = \min(D[i][j], D[i][k] + D[k][j])$ valuta se l'inserimento di un nodo intermedio $k$ "rilassa" (ovvero abbassa) il costo totale dell'intero percorso tra $i$ e $j$. La logica di base è identica, ma applicata a matrici di adiacenza multi-arco.

## Algoritmo di A* (A-Star)

Una specializzazione di Dijkstra che introduce un'euristica. Valuta i nodi minimizzando la funzione $f(n) = g(n) + h(n)$, dove $g(n)$ è il costo esatto dal nodo di partenza e $h(n)$ è una stima (euristica ammissibile) del costo dal nodo $n$ alla destinazione.

* **Adatto per:** Ricerca del percorso ottimale point-to-point quando si ha conoscenza del dominio spaziale o logico del grafo.
* **Problemi:** L'efficienza dipende interamente dalla bontà della funzione euristica. Un'euristica non ammissibile sacrifica la garanzia del percorso minimo; un'euristica debole lo fa degenerare in Dijkstra. Spazio di memoria elevato.
* **Complessità:** Varia fortemente. Nel caso pessimo $O(b^d)$ ($b$ è il branching factor, $d$ la profondità), ma all'atto pratico taglia drasticamente lo spazio di ricerca.
* **Applicazioni in Graph Analysis:** Pathfinding e navigazione spaziale per robotica autonoma e droni, analisi di reti stradali basata su coordinate spaziali (distanza euclidea o di Manhattan come euristica).

!!!tip Algoritmo
    L'estensione euristica di Dijkstra, progettata per dirigere l'esplorazione spaziale verso l'obiettivo, riducendo i nodi visitati.
    1.  **Funzione di Costo:** Per ogni nodo $n$, valuta una funzione $f(n) = g(n) + h(n)$, dove $g(n)$ è il costo esatto dal nodo di partenza a $n$, e $h(n)$ è un'euristica che stima il costo da $n$ al target.
    2.  **Vincolo Euristico:** Affinché A* garantisca l'ottimalità, $h(n)$ deve essere *ammissibile* (non deve mai sovrastimare il costo reale per raggiungere la meta).
    3.  **Esecuzione:** Mantiene due insiemi: *Open Set* (nodi da valutare, ordinati per $f(n)$ crescente) e *Closed Set* (nodi già valutati). Estrae il nodo con il minor $f(n)$, applica la relaxation sui vicini calcolando i nuovi $g(n)$, e li inserisce nell'Open Set se rappresentano un percorso migliore.

Eredita il meccanismo esatto di Dijkstra per aggiornare i costi effettivi ($g(n)$), ma utilizza la funzione euristica ($h(n)$) per alterare in modo intelligente l'ordine con cui i nodi vengono selezionati per il rilassamento.

## Algoritmo di Viterbi

Opera su modelli di Markov nascosti (HMM). Invece di sommare costi, massimizza le probabilità congiunte. Procedendo in avanti nel tempo (o nella sequenza), memorizza in ogni stato la probabilità massima di arrivarci e un puntatore a ritroso per ricostruire il percorso alla fine.

* **Adatto per:** Decodifica in processi stocastici, grafi diretti aciclici (strutturati a "trellis"), ricerca della sequenza di stati nascosti più probabile.
* **Problemi:** Non è generalizzabile a grafi con topologie libere o cicliche. Dipende dalla validità dell'assunzione di Markov.
* **Complessità:** $O(S^2 \cdot T)$, dove $S$ è il numero di stati e $T$ la lunghezza della sequenza osservata.
* **Applicazioni in Graph Analysis:** Bioinformatica (allineamento e decodifica di sequenze genetiche), Natural Language Processing (Part-of-Speech tagging), signal processing per riconoscimento vocale.
  
!!!tip Algoritmo
    Lavora nel dominio stocastico dei Modelli di Markov Nascosti (HMM). Invece di sommare i pesi degli archi, moltiplica le probabilità.
    1.  **Struttura Dati:** Costruisce un diagramma a traliccio (trellis) in cui le righe sono gli stati del sistema e le colonne sono i passi temporali $t$.
    2.  **Forward Pass:** Per ogni passo $t$ e ogni stato $k$, calcola la probabilità massima $V_{t,k}$ che una sequenza di stati termini in $k$ al tempo $t$, date le osservazioni fino a quel momento.
        $$V_{t,k} = \max_{x \in X} \left( V_{t-1,x} \cdot A_{x,k} \cdot B_{k,y_t} \right)$$ Dove $A_{x,k}$ è la probabilità di transizione dallo stato $x$ a $k$, e $B_{k,y_t}$ è la probabilità di emissione dell'osservazione $y_t$ nello stato $k$.
    3.  **Backtracking:** Insieme a $V_{t,k}$, memorizza un puntatore (backpointer) allo stato precedente $x$ che ha massimizzato l'equazione. Al termine della sequenza, si sceglie lo stato finale con probabilità massima e si seguono i backpointer a ritroso per decodificare il percorso ottimale.

Opera in un dominio stocastico e si distacca completamente da questa meccanica. Invece di minimizzare la somma di costi additivi rilassando un limite superiore, l'algoritmo massimizza il prodotto di probabilità (transizione ed emissione) per trovare la sequenza di stati nascosti più verosimile.

## Algoritmo di Johnson

È una combinazione elegante per il calcolo APSP su grafi sparsi. Usa Bellman-Ford per creare una funzione di "potenziale" per ogni nodo, ricalcolando i pesi degli archi in modo che siano tutti non negativi ma conservino i percorsi ottimali. Poi, lancia Dijkstra da ogni nodo con i nuovi pesi.

* **Adatto per:** APSP su grafi sparsi, dove è significativamente più veloce di Floyd-Warshall, specialmente in presenza di possibili pesi negativi.
* **Problemi:** Overhead iniziale per l'esecuzione di Bellman-Ford e la trasformazione dei pesi. Inutile su grafi molto densi.
* **Complessità:** $O(V^2 \log V + V \cdot E)$.
* **Applicazioni in Graph Analysis:** Analisi di enormi reti sparse di telecomunicazioni, logistica su scala globale o studio dei colli di bottiglia (betweenness centrality) in reti elettriche estese.

!!!tip Algoritmo
    Una soluzione ibrida per calcolare l'APSP su grafi sparsi, superando il problema dei pesi negativi per poter utilizzare la velocità di Dijkstra.

    1.  **Nodo Fittizio:** Aggiunge un nuovo nodo fittizio $q$ al grafo, connesso a tutti i nodi esistenti con archi diretti di peso $0$.
    2.  **Calcolo dei Potenziali:** Esegue Bellman-Ford partendo da $q$. Questo calcola la distanza minima $h(v)$ da $q$ a ogni nodo $v$. Se Bellman-Ford rileva un ciclo negativo, l'algoritmo termina.
    3.  **Reweighting:** Modifica i pesi di tutti gli archi originali $(u, v)$ per eliminare le negatività usando i potenziali appena calcolati: 
        $$\hat{w}(u, v) = w(u, v) + h(u) - h(v)$$ Per le proprietà della disuguaglianza triangolare, si garantisce che $\hat{w}(u, v) \geq 0$ per ogni arco.
    4.  **Esecuzione di Dijkstra:** Ora che non ci sono pesi negativi, esegue l'algoritmo di Dijkstra da *ogni* nodo del grafo originale usando i nuovi pesi $\hat{w}$.
    5.  **Ripristino:** Calcola le distanze reali finali invertendo il bilanciamento:
        $$d_{reale}(u, v) = d_{Dijkstra}(u, v) - h(u) + h(v)$$

Essendo una pipeline che utilizza Bellman-Ford per il reweighting e Dijkstra per la ricerca, basa interamente il suo funzionamento sull'operazione di rilassamento degli archi.


