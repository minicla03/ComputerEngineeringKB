# Graph Analytics Intro

Parent: [[Graph_Analytics_MOC]]

La **Graph Analytics** (o analisi dei grafi) è un insieme di strumenti e tecniche analitiche utilizzate per determinare la forza e la direzione delle relazioni tra oggetti in un grafo. A differenza dell'analisi dati tradizionale, che spesso tratta i dati come entità isolate (ad esempio, righe in un foglio di calcolo), la graph analytics si concentra sulle relazioni a coppie tra due oggetti e sulle caratteristiche strutturali della rete nel suo complesso.

I database tradizionali (relazionali/SQL) sono progettati per organizzare i dati in righe e colonne rigide. Sebbene efficienti per archiviare transazioni semplici, questi sistemi "spezzano" le relazioni tra i dati, costringendo gli analisti a ricostruirle tramite operazioni di JOIN costose e lente, subendo un calo delle prestazioni. La graph analytics, invece, mantiene le relazioni come elementi nativi (nodi ed archi), permettendo di attraversare milioni di connessioni in tempo reale senza i costi computazionali delle JOIN, rendendo possibile l'analisi di grandi reti complesse in modo efficiente.

Il modello relazionale fatica ad adattarsi a strutture dati che cambiano rapidamente o che non seguono uno schema predefinito, mentre i grafi offrono la flessibilità necessaria per aggiungere nuovi tipi di dati e relazioni senza interrompere le applicazioni esistenti.

La graph analytics consente di scoprire modelli nascosti, tendenze e relazioni nei dati connessi, cosa che con gli approcci relazioni sarebbe difficile o impossibile da identificare perchè non riescono a vedere forme complesse come anelli, cicli o cluster isolati. Ad esempio, nel rilevamento delle frodi, un approccio tradizionale potrebbe analizzare le singole transazioni e trovarle legittime, fallendo nel rilevare un "anello di frode" (fraud ring) in cui un gruppo di criminali sposta denaro circolarmente tra conti per eludere i controlli. Ad esempio, nel rilevamento delle frodi, un approccio tradizionale potrebbe analizzare le singole transazioni e trovarle legittime, fallendo nel rilevare un "anello di frode" (fraud ring) in cui un gruppo di criminali sposta denaro circolarmente tra conti per eludere i controlli.

## Applicazioni della Graph Analytics

La graph analytics viene utilizzata in una vasta gamma di settori e applicazioni, tra cui:

- **Social Network Analysis**: Per analizzare le relazioni tra utenti, identificare influencer e comprendere la diffusione delle informazioni.
- **Raccomandazione di Prodotti**: Per suggerire prodotti o servizi basati sulle relazioni tra utenti e prodotti.
- **Rilevamento di Frodi**: Per identificare schemi sospetti nelle transazioni finanziarie o nelle reti di comunicazione.
- **Analisi delle Reti di Comunicazione**: Per comprendere le dinamiche delle reti di comunicazione e identificare punti di vulnerabilità.
- **Biologia Computazionale**: Per analizzare le reti di interazione tra proteine o geni.
- **Analisi del Traffico**: Per ottimizzare i percorsi di traffico e identificare colli di bottiglia nelle reti di trasporto.

## Tecniche di Graph Analytics

Le tecniche di graph analytics includono:

- **Centralità**: Misura l'importanza di un nodo all'interno del grafo. Esempi includono la centralità di grado, la centralità di vicinanza e la centralità di intermediazione.
- **Community Detection**: Identifica gruppi di nodi che sono più densamente connessi tra loro rispetto al resto del grafo.
- **Path Analysis**: Analizza i percorsi tra nodi per comprendere le relazioni e le influenze tra di essi.
- **Graph Clustering**: Raggruppa i nodi in cluster basati sulla loro similarità o connettività.
- **Graph Embedding**: Trasforma i nodi del grafo in vettori in uno spazio continuo, facilitando l'applicazione di tecniche di machine learning.

### Graph Algorithms

I graph algorithms forniscono degli approcci per analizzare i dati connessi perché i loro calcoli matematici sono specificamente costruiti per operare sulle relazioni.
Questi algoritmi vengono usati per fare graph analytics, e sono progettati per identificare modelli, tendenze e relazioni nei dati connessi.

## Strumenti per la Graph Analytics

Esistono diversi strumenti e librerie per eseguire la graph analytics, tra cui:

- **Neo4j**: Un database a grafo che consente di archiviare e analizzare dati connessi.
- **GraphX**: Una libreria di Apache Spark per l'elaborazione di grafi su larga scala.
- **NetworkX**: Una libreria Python per la creazione, manipolazione e studio della struttura, dinamica e funzioni dei grafi complessi.
- **Gephi**: Un software open-source per la visualizzazione e l'analisi di grafi.
- **Graph-tool**: Una libreria Python per l'analisi statistica e la visualizzazione di grafi.

## Graph-based Machine Learning

Il **Graph-based Machine Learning** rappresenta l'intersezione tra la teoria dei grafi e l'intelligenza artificiale. Mentre il machine learning tradizionale opera tipicamente su dati euclidei (come immagini o testo strutturato a griglia), il Graph-based ML è progettato per gestire dati non euclidei rappresentati come grafi, dove le relazioni e l'interdipendenza tra gli oggetti sono fondamentali.

I modelli di machine learning tradizionali assumono che le istanze dei dati siano indipendenti l'una dall'altra. In molti scenari (social network, biologia, citazioni accademiche), le istanze sono collegate da relazioni complesse. Il Graph-based ML supera i limiti dei metodi tradizionali incorporando la struttura **topologica del grafo** (come sono collegati i nodi) insieme alle **features** dei nodi stessi. Questo permette di fare previsioni non solo basandosi su cosa è un oggetto, ma anche su chi è connesso e come.

Per modellare problemi del genere seguiamo la classica pipeline di machine learning, ma con alcune differenze chiave:

1. **Rappresentazione del Grafo**: I dati vengono rappresentati come un grafo, con nodi che rappresentano entità (ad esempio, persone, prodotti) e archi che rappresentano relazioni (ad esempio, amicizie, acquisti).
2. **Feature Extraction**: Oltre alle caratteristiche dei nodi, vengono estratte caratteristiche basate sulla struttura del grafo (ad esempio, grado del nodo, centralità).
3. **Modellazione**: Vengono utilizzati modelli di machine learning specifici per grafi, come Graph Neural Networks (GNNs), che possono apprendere rappresentazioni dei nodi e delle relazioni.
4. **Valutazione**: I modelli vengono valutati utilizzando metriche appropriate per i dati connessi, come l'accuratezza delle previsioni sui nodi o sugli archi.

Le capacità predittive della Graph Analytics, supportate prevalentemente dai Graph Neural Networks (GNN), si articolano su diversi livelli di granularità: dai singoli componenti alla struttura globale, fino alla dimensione temporale.

1. **Predizioni a Livello di Nodo (Node-level)**: Questa categoria si focalizza sulle proprietà delle singole entità all'interno del sistema.
   - **Node Classification**: L'obiettivo è assegnare un'etichetta discreta a un nodo. Il modello non analizza il nodo isolatamente, ma sfrutta il "messaggio" dei vicini (neighborhood aggregation).
     Esempio: Classificare un utente in una rete sociale come "bot" o "utente reale".
   - **Node Regression**: Si predice un valore numerico continuo associato a un nodo.
     Esempio: Stimare il potenziale valore di acquisto (Life Time Value) di un cliente in base alla sua posizione nella rete di influenza.
2. **Predizioni a Livello di Arco (Link Prediction)**: Questa tipologia mira a inferire l'esistenza di connessioni mancanti o future tra coppie di nodi. È il "cuore pulsante" dei motori di raccomandazione, capace di suggerire connessioni che l'utente non sapeva nemmeno di desiderare (fino a quando non le ha acquistate).
   Applicazione: Suggerimento di amicizie nei social media, previsione di interazioni proteina-proteina in ambito farmaceutico o identificazione di transazioni nascoste nel riciclaggio di denaro.
3. **Predizioni a Livello di Grafo (Graph-level)**: In questo caso, l'input è l'intera struttura topologica e l'output è una proprietà globale del sistema.
   - **Graph Classification**: Si assegna una categoria all'intero grafo. Esempio: In bioinformatica, analizzare una molecola (rappresentata come grafo di atomi e legami) per classificarla come "solubile" o "insolubile".
   - **Graph Regression**: Si predice un valore continuo per l'intero sistema. Esempio: Stimare l'energia di legame di un nuovo composto chimico.

4. **Predizioni Spazio-Temporali (Spatial-Temporal Forecasting)**: Modelli avanzati come gli STGNN (Spatial-Temporal Graph Neural Networks) gestiscono dati dove sia la struttura che gli attributi evolvono nel tempo. È l'equivalente di analizzare un organismo vivo che cambia forma e comportamento simultaneamente. Esempio: Previsione del Traffico. I sensori stradali (nodi) e le arterie (archi) formano una rete dove la congestione si propaga fisicamente. Il modello predice lo stato futuro del sistema basandosi su flussi passati e topologia.
5. **Modelli Generativi (Graph Generation)** A differenza delle categorie precedenti (discriminative), i modelli generativi, come i Graph Autoencoders (GAE) o i Graph GANs, creano nuove strutture dati partendo da una distribuzione appresa. Esempio: Drug Discovery. Generare strutture molecolari completamente nuove che possiedano specifiche proprietà terapeutiche, riducendo anni di test in laboratorio a poche ore di simulazione computazionale.
