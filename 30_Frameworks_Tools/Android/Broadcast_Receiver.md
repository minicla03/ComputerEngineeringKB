## **BROADCAST RECEIVER**

Un **Broadcast Receiver** è un componente Android progettato per **rispondere a** messaggi provenienti da altre applicazioni o dal sistema operativo. Per implementare un broadcast receiver si estende la classe BroadcastReceiver e implementare il metodo onReceive(Context context, Intent intent) dal quale estraiamo l’evento di intent, i dati ecc.

Questi messaggi sono incapsulati negli intent per poter attraversare le applicazioni. Le app possono registrarsi per ascoltare specifici tipi di intent broadcast; quando un intent di quel tipo viene inviato, il sistema notifica il receiver in modo che possa eseguire un'azione.

Gli **intent broadcast** non sono indirizzati a destinatari specifici, ma a tutte le app interessate che hanno registrato un receiver per quel tipo di intent lo riceveranno. Le app anche in background possono ricevere messaggi dai broadcast receiver e svolgere delle attività.

Esistono due tipi di intent broadcast: quelli **inviati dal sistema (system broadcast intents)** e quelli **inviati dalla tua app (custom broadcast intents)**.

1. Gli intent broadcast di sistema vengono inviati quando si verifica un evento di sistema che potrebbe interessare la tua app, come l'avvio del dispositivi, la connessione o disconnessione dall'alimentazione ecc.
2. Gli intent broadcast personalizzati vengono utilizzati quando vuoi che la tua app esegua un'azione senza avviare un'attività, ad esempio per informare altre app che sono stati scaricati dei dati.

Ci sono due modi per registrare un broadcast receiver:

1.  staticamente nel file manifest aggiungendo un elemento \<receiver> al file AndroidManifest.xml e usare il percorso della tua sottoclasse BroadcastReceiver come attributo android:name.
    I receiver registrati staticamente possono essere attivati anche se il processo della tua app non è in esecuzione e può accedere ad ogni eventi di sistema.

Infatti Android si accorse che questo causava problemi di sicurezza, visto che potevano essere inseriti dei malware quando si verificavano deteminati eventi di sistema. Allora definirono una registrazione

2.  dinamica sulla base del contesto con cui si chiamava il broadcast receiver. La registrazione avviene chiamando il metodo registerReceiver() e passando un oggetto BroadcastReceiver e un IntentFilter. I receiver registrati dinamicamente sono legati al ciclo di vita del componente in cui sono registrati, infatti è necessario gestire anche la loro cancellazione perché potrebbero contenere dati che sprecherebbero risorse

![This is a flowchart of the Android Fragment lifecycle. Key steps in order: - onAttach - onCreate - onCreateView - onActivityCreated - onStart - onResume (Visible → Active) Then the teardown path (when leaving): - onPause - onStop - onDestroyView - onDestroy - onDetach The diagram also shows a return arrow between onDestroyView and onCreateView labeled "Fragment returns to the layout from the backstack," and a dotted divider indicating the visible/active transition.](./Android_images/image_016.png)![The image is a side-by-side flowchart comparing two Android Service lifecycles: - Left (Started/unbound service): - Call to startService() (blue) - onCreate() (gray) - onStartCommand() (gray) - Service running (green) — active lifetime (yellow background) - The service is stopped by itself or a client - onDestroy() (gray) - Service shut down (orange) — labeled "Unbounded service" - Right (Bound/bound service): - Call to bindService() (blue) - onCreate() (gray) - onBind() (gray) - Clients are bound to service (green) — active lifetime (yellow background) - All clients unbind by calling unbindService() - onUnbind() (gray) - onDestroy() (gray) - Service shut down (orange) — labeled "Bounded service" Shapes are color-coded (blue calls, gray lifecycle callbacks, green running state, orange shutdown) and a yellow region marks the active lifetime.](./Android_images/image_017.png)

Il pattern che viene usato è l’**observer con tassonomia ad eventi**

### **MODALITÀ DI INVIO DEI BROADCAST**

**Broadcast Normali**, con cui il broadcast intente è prodotto da un singolo produce e viene inviato a tutti i receiver contemporaneamente. Essendo che vengono mandati sul thread principale, i receiver non vengono eseguiti in parallelo, quindi non è possibile fare affidamento su un ordine di esecuzione particolare né sapere quando tutti i receiver hanno completato l'esecuzione.

Vengono inviati tramite il metodo sendBroadcast(). I receiver sono indipendenti fra loro e quindi non possono scambiarsi informazioni fra loro.

**Broadcast Ordinati**, sono principalmente eventi di sistema, e questi sono mandati ad una sequenza di broadcast che quandi ricevono l’intent verificano se lo possono risolvere o se ne hanno autorizzazione a risolvelo, altrimenti viene mandato al broadcast successivo fino ad arrivare alla fine della sequenza dove viene lanciata un’eccezione per segnalare che non è stato possibile risolverlo.

E possibile anche assegnare delle priorità, tramite android:priority per modificare l’ordine di esecuzione. Conviene nella catena mettere sempre quelli più specifici per quello che si deve fare. Questo implementa il **pattern di catena di responsabilità**.

![A high-level component/flow diagram for an observer-based MVP-like architecture: - Top-left: "View 1" sends requests (processing/data) to "Presenter 1 - Observer" and receives UI updates back. - Center: "Presenter 1 - Observer" acts as the observer/controller. It calls methods on models and registers a BroadcastReceiver. - Bottom-center (Models box): contains "Model 1", "BroadcastReceiver", and "Model 2". The presenter calls methods on Model 1 and Model 2 and registers the BroadcastReceiver there. - Right: "Observable" receives updated values from the Models layer and exposes updates back to the Presenter. - Arrows show the runtime flow: Models update the Observable -> Observable provides updated value to the Presenter (calls update method / get updated value) -> Presenter updates the View. - The BroadcastReceiver is shown as part of the Models block and connects into the Observable update flow (it receives broadcasts and contributes to model/observable updates).](./Android_images/image_018.png)

**LocalBroadcastManager** Questi rimangono nell’app e quindi non hanno bisogno di intent e né della registrazione nel manifest. Si ottiene un'istanza singleton chiamando getInstance(context), che è thread-safe. Per inviare un broadcast locale si usa il suo metodo sendBroadcast(), e per registrare un receiver si usa registerReceiver(). I receiver locali devono essere registrati dinamicamente nel codice; la registrazione statica nel manifest non è disponibile per LocalBroadcastManager. È importante annullare la registrazione del receiver locale quando non è più necessario per evitare memory leak.

**Custom Broadcast** sia il producer che il receiver devono avere lo stesso nome e devono avere un URI di riferimenti che deve essere univoco, infatti si usa il FQN del package in cui si trova

### **RESTIZIONE DEI BROADCAST**

Bisogna evitare che altre applicazione estraggano dati dei broadcast. Infatti il sistema Android non è multiutente, ma per dare maggiori sicurezza android definisce delle linee guida per evitare minacce alla sicurezza. È necessario creare un sistema di permessi valido, implementando setpackage() per far consumare i messaggi broadcast solo da package specifici. I permessi che devono essere richiesti all’utente devono esser specificati nel manifest e non si possono mandare messaggi non confinati, l’unico che può è Android, che può mandare permessi null, cioè non confinati.

È possibile imporre permessi per il ricevente e lo si fa con registerReceiver() e nel manifest dobbiamo specificare nel BroadcastReceiver android:permission con i permessi di cui ha bisogno. Quando si hanno bisogno dei permessi, si chiede all’utente di darli o meno. Se l’utente accetta, allora il BroadcastReceiver sarà registrato. Non si devono fare operazioni long run perché impegneremmo troppo il sistema, quindi una volta che abbiamo acquisito i dati nella onReceiver(), liberiamo la callback e poi elaboriamo in modo asincrono. (code)
