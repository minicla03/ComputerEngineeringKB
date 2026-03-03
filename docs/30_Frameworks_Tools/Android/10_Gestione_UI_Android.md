# **INTERFACCIA UTENTE**

Quando sviluppiamo un’app Android, dobbiamo pensare all’interfaccia grafica, ovvero a come gli elementi vengono organizzati sullo schermo.

L'**interfaccia utente (UI)** di un'applicazione è costruita attraverso una **gerarchia di oggetti chiamati view**. Ogni elemento visibile sullo schermo è una view.

Tutti i componenti visivi in Android discendono dalla classe Viewe vengono indicati genericamente come Views.

La classe **ViewGroup** è un'estensione di View che supporta **l'aggiunta di visualizzazioni innestate** che hanno la responsabilità di decidere le dimensioni della view di ogni figlio e di determinare la loroposizione.

I ViewGroup che si concentrano principalmente sulla disposizione delle viste contenute sono indicati come **layout**. I ViewGroup sono visti quindi possono anche disegnare la propria interfaccia utente personalizzata e gestire le interazioni degli utenti.

**Layouts** → definiscono la struttura e la disposizione degli elementi sulla schermata

**Views** → Sono gli elementi base dell’interfaccia utente

**Widgets** → Sono particolari tipi di View con funzionalità specifiche

Per creare e disporre le viste all'interno della UI si possono utilizzare risorse di layout XML per creare e costruire lo scheletro statico della UI di un Actvity da fare evolvere dinamicamente in modo programmatico.

Questo approccio consente di specificare diversi layout ottimizzati per diverse configurazioni hardware, in particolare variazioni delle dimensioni dello schermo, potenzialmente anche modificandoli in fase di esecuzione in base a modifiche hardware (come i cambiamenti di orientamento).

L’interfaccia utente è organizzata in una struttura ad **albero gerarchico**, chiamata **albero delle View**

- i nodi interni sono le ViewGroup
- le foglie sono le View effettive

Quando apriamo un’applicazione Android, una delle prime cose che il sistema fa è costruire l’interfaccia grafica dell’Activity in base alla struttura definita nel file XML del layout. Questo processo avviene all’interno del metodo **onCreate()**, dove viene caricato l’albero delle View.

Quando il metodo onCreate() viene eseguito, l’Activity richiama setContentView(R.layout.activity_main), che ha il compito di leggere il file XML e tradurlo in un insieme di oggetti **View** e **ViewGroup** in memoria.

Android calcola la disposizione degli elementi, assegna loro le dimensioni e infine li disegna sullo schermo.

Android dà la possibilità di **modificare l’albero delle View in tempo reale**, aggiungendo, rimuovendo o modificando elementi dell’interfaccia mentre l’utente sta interagendo con l’app, senza dover ricaricare l’intera Activity

## **EVENTI**

Le view permettono di acquisire gli eventi dalla l'oggetto con cui interagisce l'utente. Per un'app Android, l'interazione in genere consiste nel toccare, premere, digitare o parlare e ascoltare.

La View che **ha il focus** sarà la componente che riceve l'input dell'utente.

Il focus può essere avviato dall'utente toccando una View. È possibile definire un ordine di focus in cui l'utente viene guidato da un controllo UI a un altro controllo UI.
Il focus può anche essere controllato a livello di programmazione; un programmatore può richiedereFocus() su qualsiasi View che è focalizzabile.

Un altro attributo di un controllo di input è **cliccabile**. Se questo attributo è true, allora la View può reagire agli eventi di clic. Come per il focus, cliccabile può essere controllato a livello di programmazione.

La differenza tra cliccabile e focalizzabile è che cliccabile significa che la view può essere cliccata o toccata, mentre focalizzabile significa che alla view è consentito ottenere il focus da un dispositivo di input come una tastiera.
I dispositivi di input come le tastiere non possono determinare a quale view inviare i loro eventi di input, quindi li inviano alla view che ha il focus.

per intercettarlo, devi estendere la classe e sostituire il metodo. Tuttavia, l'estensione di ogni oggetto View per gestire un evento del genere non sarebbe pratica. Per questo motivo la classe View contiene anche una raccolta di interfacce nidificate con callback che puoi definire molto più facilmente.
Un **listener di eventi** è un'interfaccia della classe View che contiene un singolo di callback. Questi metodi verranno chiamati dal framework Android quando la view a cui il listener ha registrato viene attivato dall'interazione dell'utente con l'elemento nell'interfaccia utente.

Le interfacce del listener di eventi includono i seguenti metodi di callback:

onClick()da View.OnClickListener. Questo viene chiamato quando l'utente tocca l'elemento. (in modalità touch) o si concentra sull'elemento con i tasti di navigazione o la trackball e preme il tasto "Invio" adatto o premi la trackball.

onLongClick()da View.OnLongClickListener. Questo viene chiamato quando l'utente tocca e tiene premuto l'elemento (in modalità tocco) o si concentra sull'elemento con i tasti di navigazione o la trackball e tiene premuto il pulsante "Invio" o tenere premuto sulla trackball (per un secondo).

onFocusChange()Da View.OnFocusChangeListener. Questo viene chiamato quando l'utente si avvicina o si allontana dall'elemento utilizzando i tasti di navigazione o la trackball.

onKey()da View.OnKeyListener. Viene chiamato quando l'utente si concentra sull'elemento e preme o rilascia un tasto hardware sul dispositivo.

onTouch()da View.OnTouchListener. Questo nome viene chiamato quando l'utente esegue un'azione qualificata come evento touch, ad esempio una stampa, un comunicato stampa o qualsiasi gesto di movimento sullo schermo (entro i limiti dell'elemento).

onCreateContextMenu() da [View.OnCreateContextMenuListener](https://developer.android.com/reference/android/view/View.OnCreateContextMenuListener?hl=it). Questa operazione viene chiamata quando viene creato un menu contestuale (in seguito a un "clic lungo") prolungato.

Un **gesto di tocco** si verifica quando un utente posiziona una o più dita sul il touchscreen e l’app interpreta questa sequenza di tocchi come un gesto.
Il rilevamento dei gesti prevede due fasi:

1.  la raccolta di dati sugli eventi touch
2.  l’interpretazione dei dati per determinare se soddisfano i gesti supportati dall’app.

Quando un utente posiziona una o più dita sullo schermo, viene attivata la **callback**onTouchEvent()sulla visualizzazione che riceve gli eventi touch.
e per ogni sequenza di tocco viene memorizzata la posizione, pressione, dimensione, il numero di dita usate e altre info utili. Queste info vengono memorizzate nell’oggetto MotionEvent.
Il gesto inizia quando l'utente tocca per la prima volta lo schermo, poi continua mentre il sistema tiene traccia della posizione del dito o delle dita dell'utente e termina acquisire l'evento finale dell'ultimo dito dell'utente che lascia lo schermo.

Gli eventi, in particolare gli eventi di input come i tocchi, possono essere propagati attraverso la gerarchia delle view. Una View può consumare un evento o passarlo al suo parent ViewGroup per la gestione. Il sistema Android **distribuisce (dispatch)** questi eventi ai componenti appropriati per la gestione.

![A small UML-style diagram showing the Chain of Responsibility pattern: - Left: an oval labeled "Client". - Top-center: a rectangular abstract/base class labeled "Handler" with a public method `+HandleRequest()`. - Below: two rectangles for concrete handlers (both labeled "ConcreteHandler2" in the image) with `+HandleRequest()` each. - Open-triangle arrows from each concrete handler up to `Handler` indicate inheritance/generalization. - The client is associated with/uses the `Handler` (implied connection).](./Android_images/image_020.png)Quando si verifica un evento di interazione, si propaga dall'activity andando fino alla view.

Quindi a tutti i componenti della gerarchia viene data la possibilità di gestire l'evento, iniziando con la vista in alto e tornando all'attività. Quindi l'activity è la prima a ricevere l'evento e l'ultima a cui viene data la possibilità di gestirlo.

Se qualche ViewGroup vuole gestire immediatamente l'evento touch, può restituire true nel suo **onInterceptTouchEvent()**.

Una Activity non ha onInterceptTouchEvent() ma può sovrascrivere dispatchTouchEvent() per fare la stessa cosa.

Se una vista (o un gruppo di viste) ha un OnTouchListener, l'evento tocco viene gestito da OnTouchListener.onTouch()

Altrimenti è gestito da onTouchEvent(). Se onTouchEvent () restituisce true per qualsiasi evento di tocco, la gestione si interrompe. Nessun altro ne ha la possibilità.

La classe **GestureDetector** può essere utilizzata per interpretare sequenze di MotionEvent e dispatchare eventi di gesto specifici (come tap, swipe, fling) a un listener OnGestureListener

## **VIEW PERSONALIZZATE**

La creazione di nuove visualizzazioni dà la possibilità di modellare l'aspetto e il funzionamento delle applicazioni. Creando i propri controlli, si può creare una interfacce utente che si adatta in modo perfetto ai requisiti.

Per creare nuovi controlli da un'area di disegno vuota, si usa la classe base **View** o **SurfaceView**.

La classe View fornisce un oggetto **Canvas** con una serie di metodi di disegno e classi Paint. Servono per creare un'interfaccia visiva con bitmap e grafica raster. È possibile catturare e sovrascrivere gli eventi utente, inclusi i tocchi dello schermo o la pressione dei tasti per fornire l'interattività.

La classe **SurfaceView** fornisce un oggetto Surface che supporta il disegno da un thread in background e, facoltativamente, l'uso di OpenGL per implementare la grafica.

Per creare una view custom dobbiamo fornire la classe:

1. Costruttori
   a. Uno a cui passiamo solo il contesto
   b. Contesto e attributi
   c. Contesto attributi e stile
2. onMeasure() che viene chiamato quando la view deve essere disegnata. L’incarico di disegnare la view spetta al genitore che chiede al figlio le sue dimensioni: altezza e larghezza, chiamando i metodi della classe del figlio.
   a. Questa funzione viene chiamata ogni volta che la view viene invalidata.
3. onDraw() che serve per fare effettivamente il disegno della view. Questa funzione viene chiamata frequentemente e o in modo sincrono in base alla frequenza di refresh impostata dal dispositivo. Se la frequenza di refresh è minore del tempo con cui questa funzione viene chiamata si hanno dei problemi nel rendering.

## **RENDERING PIPELINE**

Il processo di rendering è sincronizzato con il segnale **VSync** (**vertical synchronization**) generato dall'hardware del display scandendo il ritmo del rendering, sincronizzando ogni frame con il refresh dello schermo. Android sfrutta questo segnale per organizzare il lavoro su tre livelli principali:

1. UI Thread
2. RenderThread
3. Graphics Pipeline.

Il **UI Thread**, è responsabile della gestione degli eventi di input, dell’aggiornamento dell’interfaccia e delle animazioni. Quando il sistema riceve un segnale di **VSync**, il **Choreographer**, un componente di Android che orchestra il rendering, sveglia il UI Thread, che esegue una serie di operazioni:

1. Input Handling → Il primo compito è elaborare gli input dell’utente, come tocchi, scroll o gesti. Se premiamo un pulsante, il sistema deve registrare l’evento e prepararsi a cambiare la UI.
2. Animations → Se ci sono animazioni in corso (ad esempio, un pulsante che si ingrandisce quando viene premuto), vengono aggiornate e interpolate. Android calcola la nuova posizione, opacità o dimensione dell’elemento animato.
3. Measure e Layout → Ora il sistema deve capire quanto spazio occupano le View e dove devono essere posizionate. Questo processo avviene in due fasi:
   **Measure** → Ogni View calcola la propria dimensione basandosi sui suoi genitori e sul contenuto.
   **Layout** → Una volta note le dimensioni, le View vengono posizionate nella finestra dell’app.
4. Draw → Dopo aver determinato le posizioni e le dimensioni delle View, il sistema esegue il disegno vero e proprio. Questo avviene nel metodo onDraw(Canvas canvas), che dipinge gli elementi grafici sullo schermo.
5. Sync → Infine, il UI Thread invia i dati al RenderThread, il quale si occuperà di trasformarli in qualcosa che la GPU può elaborare.

Se una proprietà di una view cambia in modo da influire sul suo aspetto viene chiamato il metodo **invalidate()** sulla vista. Questa chiamata non causa un redraw immediato, ma marca la vista come "sporca" e segnala che deve essere ridisegnata. Una volta chiamato invalidate() su una vista, questa chiamata si propaga **verso l'alto nella gerarchia delle viste**, chiamando una serie di metodi, come **invalidateChild()**, sui suoi parent.

Questo processo continua fino a raggiungere la radice della gerarchia delle viste, in particolare la **ViewRootImpl**.

Quando la dimensione o la posizione di una vista deve cambiare viene chiamato **requestLayout()**. Questo è simile all'invalidazione, ma innesca un processo di misurazione e layout per determinare le nuove dimensioni e posizioni delle viste coinvolte.

Quando la chiamata invalidateChild() raggiunge il **ViewRootImpl**, quest'ultimo non esegue immediatamente il ridisegno ma chiama il metodo **scheduleTraversals()** con cui pianifica l'esecuzione del processo di **traversal** (misurazione, layout e disegno) in un momento successivo, tipicamente in sincronia con il prossimo segnale VSync gestito dal Coreoghaph.

Per ottimizzare questo processo, Android utilizza un meccanismo chiamato **Display List**. Quando viene chiamato draw(), la vista (o i suoi antenati) ottiene (o rigenera) una **display list** tramite il metodo **getDisplayList()**. Una **display list** è una registrazione di tutte le operazioni di disegno (ad esempio, drawBackground(), drawText()) che la vista deve eseguire per rendersi. L'intera gerarchia delle viste è rappresentata da una gerarchia di display list.

Dopo che l'UI thread ha completato il traversal (misura, layout e disegno) e ha generato la gerarchia delle **Display List**, queste informazioni vengono sincronizzate con il **Render Thread**.

Per evitare di sovraccaricare il **UI Thread**, Android introduce il **RenderThread**, un thread separato che gestisce il disegno e l’invio dei comandi alla GPU.

Una volta che il **UI Thread** ha terminato il suo lavoro, il **RenderThread** prende in carico il frame e segue questi passaggi:

1. Sync → Riceve i dati dal UI Thread e li sincronizza con lo stato attuale della grafica.
2. Execute → Processa i comandi di rendering, preparando la scena da inviare alla GPU.
3. Get Buffer → Recupera un buffer di rendering, ovvero un’area di memoria in cui verrà disegnato il frame.
4. Issue → Converte i comandi in istruzioni per la GPU.
5. Swap Buffer → Una volta che tutto è pronto, il RenderThread invia il frame alla GPU e chiede il prossimo buffer per il frame successivo.

Il Render Thread prende queste Display List, che sono una rappresentazione delle operazioni di disegno a livello Java, e le trasforma in qualcosa che può effettivamente elaborare per la GPU. Queste rappresentazioni native delle operazioni di disegno sono chiamate **Display List Operations (DL ops)**.

Le DL ops sono quindi la forma in cui le intenzioni di disegno dell'applicazione, espresse tramite le API Canvas a livello Java, vengono tradotte in operazioni concrete che il Render Thread può ottimizzare e inviare alla GPU.

Un esempio di DL op è una **fill operation** che corrisponde all'operazione di riempire una determinata area con un colore. Altre DL ops rappresenterebbero il disegno di testo, linee, bitmap, ecc..

In sostanza, le DL ops sono un intermediario tra la rappresentazione astratta del disegno (Display List) e i comandi concreti inviati alla GPU.

Le DL ops vengono ottimizzate tramite **riordinamento (reordering)** delle operazioni di disegno.

L'obiettivo del riordinamento è di raggruppare operazioni di disegno simili che non si sovrappongono per minimizzare i **cambi di stato** della GPU, che sono operazioni molto costose in termini di prestazioni.

Attraverso il riordinamento, il Render Thread analizza le DL ops e, se possibile, le raggruppa. Quindi, tutte le operazioni di disegno dei rettangoli verrebbero eseguite insieme, seguite da tutte le operazioni di disegno del testo. In alcuni casi, operazioni simili possono anche essere **batching (raggruppate)** ulteriormente in una singola chiamata alla GPU per maggiore efficienza.

Questa ottimizzazione può portare a **miglioramenti significativi nelle prestazioni del rendering**, specialmente in scenari con molte operazioni di disegno simili, come ad esempio nel rendering di liste complesse.

Il riordinamento non può essere applicato se le operazioni di disegno si sovrappongono, poiché in tal caso l'ordine è cruciale per rispettare il blending e l'alpha blending.

A questo punto, entra in gioco la **Graphics Pipeline**, ovvero la parte hardware responsabile del rendering finale. Il suo compito è prendere i comandi ricevuti dal **RenderThread** e trasformarli in pixel sullo schermo.

1. Get Buffer → La GPU recupera il buffer con i dati da disegnare.
2. Swap Buffer → Il buffer contenente il nuovo frame viene inviato allo schermo.
3. Composite → Infine, la GPU compone il frame con altri layer grafici e lo mostra all’utente.

A questo punto interviene il **SurfaceFlinger** è un servizio di sistema responsabile della composizione di tutti i **window** (finestre) visibili sullo schermo.

Ogni finestra ha associata una **BufferQueue**, una coda di buffer grafici dove risiedono i dati pixel prodotti dall'applicazione (o da altri servizi di sistema). La BufferQueue ha due estremità: un produttore, il **Window Manager** che inserisce i buffer nella coda e un consumatore, l’**Activity** **Manager** che li preleva.

Quando il render thread chiama swapBuffers, accodando nel queue buffer il buffer renderizzato nella BufferQueue. SurfaceFlinger acquisisce questi buffer pronti per essere composti.

SurfaceFlinger comunica con l'**Hardware Composer (HWC)**, che è un'astrazione hardware specifica del dispositivo in grado di comporre più layer (bitmap) in modo molto efficiente, spesso senza utilizzare la GPU, per risparmiare energia. L'HWC decide come gestire ciascun layer:

- Se l'HWC supporta il formato pixel del layer e non ci sono troppe trasformazioni complesse, può gestirlo come un overlay, componendolo direttamente sull'hardware.
- In alcuni casi, l'HWC potrebbe non essere in grado di gestire un layer come overlay, allora il SurfaceFlinger deve utilizzare la GPU per comporre questi layer in un frame buffer (un buffer di rendering temporaneo) tramite comandi OpenGL, un'API utilizzata in Android per il rendering 2D e 3D.

Indipendentemente dal fatto che la composizione avvenga tramite HWC o GPU, SurfaceFlinger combina tutti i layer visibili (le finestre di tutte le applicazioni, la barra di stato, la barra di navigazione) e invia il risultato all'hardware del display per essere visualizzato.
