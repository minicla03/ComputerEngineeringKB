# **SERVICE**

Un **service** in Android è un componente applicativo che esegue operazioni a lunga esecuzione, solitamente in background, senza fornire un'interfaccia utente (UI).
Un'applicazione può avviare un service anche se non è in primo piano e un service può continuare a essere eseguito anche dopo che l'attività che lo ha avviato è stata distrutta.

Un service può essere **avviato**, **collegato** (bound), o **entrambi**.

- Un service avviato è quello che un componente applicativo (come un'activity) avvia chiamando startService(). I service avviati vengono utilizzati per eseguire task in background che possono durare a lungo o per eseguire lavoro per processi remoti. Una volta avviato, un service può continuare a funzionare indefinitamente, anche se il componente che lo ha avviato viene distrutto. Solitamente, un service avviato esegue una singola operazione e non restituisce un risultato al chiamante. Quando l'operazione è completata, il service dovrebbe fermarsi da solo chiamando stopSelf(), oppure un altro componente può fermarlo chiamando stopService().
- Un service collegato (bound) è un service a cui un componente applicativo si connette chiamando bindService(). I service collegati forniscono un'interfaccia client-server che permette ai componenti di interagire con il service, inviare richieste e ottenere risultati, a volte utilizzando la comunicazione interprocesso (IPC). Un service collegato è in esecuzione solo finché un altro componente applicativo è collegato ad esso. Più componenti possono collegarsi allo stesso service contemporaneamente, ma quando tutti si disconnettono, il service viene distrutto. Un service collegato generalmente non consente ai componenti di avviarlo chiamando startService().

## **CICLO DI VITA DI UN SERVICE**

Il ciclo di vita di un service è più semplice di quello di un'activity. Tuttavia, è fondamentale prestare attenzione a come un service viene creato e distrutto, poiché un service senza UI può continuare a funzionare in background senza che l'utente ne sia a conoscenza, consumando risorse e batteria.

Come un'activity, un service ha dei **metodi di callback del ciclo di vita** che è possibile implementare per monitorare i cambiamenti nello stato del service ed eseguire operazioni nei momenti appropriati.

**![A simple vertical flowchart of four rounded rectangular boxes connected by downward arrows, showing the sequence of Android Fragment lifecycle callbacks (top to bottom): - onAttach() - onCreate() - onCreateView() - onActivityCreated() Each box has a light gradient background and bold text; arrows point from each callback to the next.](./Android_images/image_015.png)onCreate()**: Questo metodo viene chiamato quando il service viene creato per la prima volta. Viene chiamato una sola volta per la durata del service. Qui è dove si dovrebbero eseguire le inizializzazioni di base, come la creazione di thread o la registrazione di listener.

**onStartCommand(Intent intent, int flags, int startId)**: Questo metodo viene chiamato ogni volta che un componente avvia il service chiamando startService(). Riceve l'Intent fornito dal client (il componente che ha chiamato startService()) e due interi: flags, che forniscono informazioni aggiuntive sulla richiesta di avvio, e startId, un identificatore univoco per questa particolare richiesta di avvio. È in questo metodo che il service esegue il lavoro richiesto dall'Intent. Il valore restituito da onStartCommand() indica al sistema come dovrebbe comportarsi se il service viene interrotto inaspettatamente.

**onBind(Intent intent)**: Questo metodo viene chiamato quando un client desidera collegarsi al service chiamando bindService(). Restituisce un oggetto IBinder che il client utilizza per comunicare con il service. I service che intendono essere collegati devono implementare questo metodo; tuttavia, un service può essere sia avviato che collegato (in tal caso implementerà sia onStartCommand() che onBind()). Un service collegato generalmente non implementa onStartCommand().

- onUnbind(Intent intent): Questo metodo viene chiamato quando tutti i client collegati al service si sono disconnessi (hanno chiamato unbindService()). Il valore booleano restituito indica se onRebind() debba essere chiamato quando un nuovo client si collega al service.
- onRebind(Intent intent): Questo metodo viene chiamato quando un nuovo client si collega al service dopo che onUnbind() è già stato chiamato. Viene chiamato se onUnbind() ha restituito true.
- onDestroy(): Questo metodo viene chiamato quando il service non è più in uso e sta per essere distrutto. Questo può avvenire quando il service si ferma da solo chiamando stopSelf() o quando un altro componente chiama stopService(), oppure quando tutti i client collegati si disconnettono (per i service collegati). È qui che si dovrebbero rilasciare tutte le risorse utilizzate dal service (come thread, listener, ecc.).

È importante notare che i service avviati continuano la loro esecuzione indipendentemente dal componente che li ha avviati e devono essere fermati esplicitamente. I service collegati, invece, esistono solo per servire il componente applicativo che è collegato ad essi e vengono distrutti quando non ci sono più componenti collegati.

Come le activity e altri componenti, **tutti i service devono essere dichiarati nel file manifest** dell'applicazione. Per dichiarare un service, è necessario aggiungere un elemento <service> come figlio dell'elemento <application>.

Comprendere il ciclo di vita e le diverse tipologie di service è fondamentale per sviluppare applicazioni Android efficienti che eseguono operazioni in background in modo appropriato, senza impattare negativamente sull'esperienza utente o sulle risorse del dispositivo.

Quando un servizio è in esecuzione, può notificare gli eventi all'utente utilizzando le **notifiche snackbar** o le **notifiche della barra di stato**.

Una notifica nella barra di app è un messaggio che viene visualizzato sulla superficie della finestra corrente solo per un breve istante prima di scomparire. Una notifica nella barra di stato fornisce un'icona con un messaggio, che l'utente può selezionare per eseguire un'azione (ad esempio avviare un'attività).

In genere, una notifica nella barra di stato è la tecnica migliore da utilizzare quando un'operazione in background, come il download di un file, è stata completata e l'utente può ora intervenire. Quando l'utente seleziona la notifica dalla visualizzazione espansa, la notifica può avviare un'attività (ad esempio per visualizzare il file scaricato).
