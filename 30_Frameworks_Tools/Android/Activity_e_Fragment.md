## **ACTIVITY**

Un'**Activity** è una componente visibile di un'applicazione Android che permette agli utenti di interagire con essa. Un'app può essere composta da più Activity, ciascuna delle quali svolge un compito specifico ed è indipendente dalle altre. Ogni Activity è formata da una serie di View, ovvero gli elementi dell'interfaccia utente

### **CICLO DI VITA**

Il sistema operativo Android gestisce il ciclo di vita di un'Activity, determinando quando questa viene creata, avviata, arrestata o distrutta. La classe Activity fornisce diversi metodi di callback che permettono agli sviluppatori di definire il comportamento dell'applicazione nei vari stati dell'Activity.

![A flowchart of the Android Activity lifecycle showing states and callbacks: - Top: "Activity launched" - Sequence: onCreate() → onStart() → onResume() → Activity running (green) - When another activity comes to foreground: onPause() → onStop() (activity no longer visible) - If the activity finishes or is destroyed: onDestroy() → Activity shut down (orange) - Return/navigation paths: - From onPause() user returns → onResume() - From onStop() user navigates back → onRestart() → onStart() → onResume() - If system reclaims memory while stopped: app process killed (orange) - Small annotations explain each callback (e.g., onPause: another activity comes into foreground; onStop: activity is no longer visible; onDestroy: finishing or being destroyed by system).](./Android_images/image_010.png)

L’activity può essere avviata dall’utente che preme sull’icona dell’applicazione, oppure da un’altra activity tramite un intent.

Quando un'app viene avviata Zygote **clona** se stesso per creare un nuovo processo, riducendo il tempo di avvio. Questo nuovo processo eredita le classi e le librerie già caricate, ottimizzando l'esecuzione.

L'**ActivityManagerService (AMS)** è il componente principale che gestisce il ciclo di vita delle **Activity** e coordina le transizioni tra di esse.

- Riceve la richiesta di avvio dell'app.
- Controlla se il processo dell’app è già in esecuzione o se deve essere creato.
- Comunica con il Zygote per avviare un nuovo processo se necessario.

Dopo l’avvio dell’app, vengono chiamate tre metodi per creare un activity.

1. onCreate() in questo momento l’activity viene effetivamente creata e in questa fase si inizializzano tutte le risorse necessarie. Viene carocato in memoria l’albero delle views che formano l’activity.
   La onCreate() di un'Activity non deve essere bloccante perché viene eseguita nel Main Thread, lo UI Thread. Questo thread è responsabile della gestione dell’interfaccia utente e dell’interazione con l’utente. Se il codice in onCreate() è troppo pesante Android termina forzatamente le app che bloccano il Main Thread.
2. Subito dopo, Android chiama il metodo onStart() che permette all’Activity di essere visibile all’utente, ma non è ancora interattiva. L’interfaccia viene renderizzata visualizzando le componenti che formano l’activity.
3. Con l’invocazione di onResume() l’Activity diventa pienamente attiva e interattiva e l’utente può effetti interagire con le componenti dell’appliczione. Gli event generati vengono catturati dal looper e fa cambiare stato all’activity. Durante questa fase, l’Activity è in primo piano e qualsiasi altra Activity aperta in precedenza è stata messa in pausa o nascosta.

Dopo queste tre operazioni l’applicazione si trova nello stato di running e l’utente può interagire. Se l'utente non interagisce l’activity passa in uno stato di **onPause()**, che indica che l’activity non è più in primo piano, ma questo non vuol dire che debba essere distrutta.

Quando la tua attività non è più visibile all'utente, ma è ancora in memoria viene invocata la chiamata **onStop()** e da qui inizia il ciclo di distruzione e rilascio delle risorse dell’activity.

La differenza tra **onStop()** e **onPause()** è che nella **onPause()** il lavoro relativo all'interfaccia utente continua anche se l'utente sta visualizzando la tua attività in modalità multi-finestra.

Con la **onRestart()** tato transitorio si verifica solo se un'Activity fermata viene riavviata. onRestart() viene chiamato tra onStop() e onStart().
**onDestroy()** viene chiamato prima che l'Activity venga distrutta. Questo può avvenire perché l'Activity sta terminando, perché il sistema sta distruggendo l'Activity per risparmiare risorse, o a causa di un cambiamento di configurazione. È importante eseguire qui la pulizia finale delle risorse. Tuttavia, non si dovrebbe fare affidamento su onDestroy() per salvare dati importanti, in quanto potrebbe non essere sempre chiamato.

### **BACK STACK E NAVIGAZIONE FRA LE ACTIVITY**

In Android, le Activity sono gestite attraverso uno stack di Activity, il **back stack**, gestito in modo FIFO.

Il back stack è un insieme di Activity che l'utente ha visitato e a cui può tornare premendo il pulsante Indietro del dispositivo. Una **task** è un insieme di Activity correlate all'applicazione o ad una specifica interazione dell'utente e ha il suo back stack e che possiamo gestire insieme.

Quando si avvia una nuova Activity, essa viene **inserita in cima** al back stack e prende il focus dell'utente. L'Activity precedente viene fermata ma rimane disponibile nel back stack, conservando il suo stato attuale. Quando l'utente preme il pulsante Indietro, l'Activity in cima allo stack viene **rimossa** (e distrutta), e l'Activity precedente riprende.

Alla base dello stack sta il launcher e da questo si iniziano ad impilare le activity. Android non rimuoverà mai le activity tranne se si trova in situazioni critiche del sistema e allora rimuove prima le activity che si trovano in fondo allo stack, evitando di rimuove l’activity attiva.

Il back stack **non è specifico di una singola applicazione**; può contenere Activity di diverse applicazioni lanciate dall'utente in ordine cronologico inverso. Ciò significa che premendo il pulsante Indietro, l'utente potrebbe ritrovarsi in un'Activity di un'altra app se l'ha avviata precedentemente.

![A diagram of an Android task/back-stack flow showing three steps: - Left: a single foreground activity (Activity 1) with Activity 1 on the back stack. - Middle-left: user starts Activity 2 — Activity 2 is pushed on top, Activity 1 remains below in the stack. - Middle-right: user starts Activity 3 — Activity 3 is now on top, with Activity 2 and Activity 1 beneath (stack top → bottom: Activity 3, Activity 2, Activity 1). - Right: user navigates back from Activity 3 — Activity 3 is destroyed and removed, returning to Activity 2 in the foreground with Activity 1 still below.](./Android_images/image_011.png)
Un’activity può spostarsi in**background** quando un utente avvia una nuova attività o passa alla schermata Home. In background, tutte le attività dell'attività vengono arrestate, ma lo stack precedente dell'attività rimane intatto, perde l'attenzione mentre è in corso un'altra attività. R l'attività può tornare in primo piano per consentire agli utenti di riprendere da dove hanno interrotto disattivata.

Le activity nel back-stack non vengono mai riorganizzate, ma è possibili modificare questo andamento lineare dello stack perché in certe situazioni questa gestione non va bene. Esistono cinque modalità di lancio che si possono assegnare all'attributo launchMode:

1. StandardLa modalità predefinita. Il sistema crea una nuova istanza dell'attività nell'attività da cui è stato avviato e instrada l'intent a quest'ultimo. L'attività può essere creata più volte, ogni istanza può appartenere ad attività diverse un'attività può avere più istanze.
2. SingleTopSe nella parte superiore dell'attività corrente esiste già un'istanza dell'attività, il sistema instrada l'intent a quell'istanza tramite una chiamata alla sua onNewIntent() anziché creare una nuova istanza dell'attività. L'attività è creata più volte, ogni istanza può appartenere ad attività diverse e un'attività può avere più istanze (ma solo se l'attività in alto dello stack posteriore non è un'istanza esistente dell'attività).
3. singleTaskIl sistema crea l'attività alla base di una nuova attività o individua la su un'attività esistente con la stessa affinità. Se un'istanza del componente esiste già un'attività, il sistema instrada all'istanza esistente tramite una chiamata alla sua onNewIntent() anziché creare una nuova istanza. Nel frattempo, tutti gli altri vengono distrutte.
4. singleInstanceIl comportamento è lo stesso di "singleTask", ad eccezione del fatto che il sistema non avvia nessun altro delle attività nell'attività che contiene l'istanza. L'attività è sempre l'unico e unico membro della sua attività. Tutte le attività iniziate da questa si aprono tra per un'attività a parte.
5. singleInstancePerTaskL'attività può essere eseguita solo come attività principale dell'attività, la prima all'attività che ha creato l'attività, perciò può esserci una sola istanza di questa attività in un'attività. A differenza della modalità di avvio di singleTask, questa l'attività può essere avviata in più istanze in diverse attività se FLAG_ACTIVITY_MULTIPLE_TASK o FLAG_ACTIVITY_NEW_DOCUMENT è stato impostato.

**SingleTask** e **SingleInstancePerTask** rimuovono tutte le attività superiori all'attività iniziale dell'attività.

I **cambiamenti di configurazione**, come la rotazione dello schermo, comportano la distruzione dell'Activity corrente e la creazione di una nuova Activity per adattarsi alla nuova configurazione. Per evitare la perdita di dati durante questi cambiamenti, è possibile **salvare lo stato dell'istanza dell'Activity.**

1. sovrascrivendo il metodo onSaveInstanceState(Bundle). Lo stato viene salvato come una serie di coppie chiave/valore in un oggetto Bundle che viene passato a onCreate() quando l'Activity viene ricreata. È anche possibile utilizzare il callback onRestoreInstanceState() per ripristinare lo stato.
2. Oppure con il model-view-controller

## **FRAGMENT**

Un **Fragment** è un componente utilizzato per dividere l'interfaccia utente in parti più piccole. Un Fragment rappresenta una porzione di UI o di comportamento che vive all’interno di un’Activity, e può essere riutilizzato o sostituito dinamicamente. Un Fragment riceve i propri eventi di input e ha una propria vista che viene composta da un file di layout apposito. I Fragment possono esistere solo all'interno di un'Activity. Un'attività può **delegare** a un fragment l'esecuzione di compiti.

Le Activity fungono da **host** per i Fragment queste devono conoscere i dettagli di come ospitare i loro Fragment, ma i Fragment non devono conoscere i dettagli delle Activity che le ospitano (**loosely couple**). Come le attività, i fragment sono "attivi" quando appartengono ad una activity focalizzata e in primo piano.

Quando un'attività viene messa in pausa o interrotta, anche i frammenti che contiene vengono messi in pausa e arrestati e anche i frammenti contenuti in un'attività inattiva sono inattivi.

Quando un'attività viene finalmente distrutta, ogni Fragment che contiene viene ugualmente distrutto. Poiché il gestore della memoria Android chiude regolarmente le applicazioni per liberare risorse, anche i frammenti all'interno di tali attività vengono distrutti.

Non dovrebbe esserci alcuna differenza nel passaggio di un frammento da uno stato scollegato, in pausa, interrotto o inattivo allo stato attivo, quindi è importante salvare tutto lo stato dell'interfaccia utente e conservare tutti i dati

quando un frammento viene sospeso o interrotto. Come un'activity, quando un frammento diventa di nuovo attivo, dovrebbe ripristinare lo stato salvato.

![The diagram shows two activity stacks (tasks): - Left (solid box, labeled "Foreground activity"): Task B contains two stacked activities — Activity Z (top, highlighted as the current/foreground) above Activity Y. - Right (dashed box, labeled "Background"): Task A contains Activity Y above Activity X, shown as a background task. Dashed outlines indicate the background task; the highlighted/top activity (Activity Z) is the active foreground.](./Android_images/image_012.png)

**AUF, Always Use Fragments**

**![A blocky, pixelated Minecraft wolf/dog: gray and white voxel-style body with a square muzzle, rectangular ears, a red collar, and cube-like legs and tail, shown in a mid-run pose.](./Android_images/image_013.png)
**I Fragment hanno anche un proprio **ciclo di vita** che è simile a quello di un'attività. Questo è importante perché, visto che un fragment lavora per conto di un'attività, il suo stato dovrebbe riflettere lo stato dell'attività. Pertanto, ha bisogno di metodi del ciclo di vita corrispondenti per gestire il lavoro dell'attività.

I callback del ciclo di vita di un Fragment includono

- onCreateView(): il valore restituito di questo metodo deve essere un'istanza di View affinché il Fragment abbia un'interfaccia utente visibile
- onDestroyView(): Ci sono anche callback per onActivityCreated e callback che vengono attivati quando un Fragment viene aggiunto (onAttached) a o rimosso (onDetached) dall'UI utilizzando i metodi di FragmentTransaction.
- I metodi onAttach(Activity), onCreate(Bundle) e onCreateView(...) vengono chiamati quando si aggiunge il fragment al FragmentManager.
- Il metodo onActivityCreated(...) viene chiamato dopo che il metodo onCreate(...) dell'attività ospitante è stato eseguito.
- Il FragmentManager di un'attività è responsabile della chiamata dei metodi del ciclo di vita dei fragment nella sua lista.

La vista di un fragment viene generalmente inflata nel metodo onCreateView().

Per aggiungere un fragment a un'attività nel codice, si effettuano chiamate esplicite al **FragmentManager** dell'attività che è responsabile della gestione dei fragment e dell'aggiunta delle loro viste alla gerarchia delle viste dell'attività.

Il FragmentManager gestisce due cose:

- un elenco di fragment
- stack di back delle transazioni di fragment.

Per ottenere il FragmentManager, si usa

- getSupportFragmentManager(), se si estende AppCompatActivity o FragmentActivity;
- getFragmentManager(), se si estende Activity e il fragment estende android.app.Fragment o PreferenceFragment).

Le **FragmentTransaction** vengono utilizzate per aggiungere, rimuovere, allegare, staccare o sostituire i fragment nell'elenco dei fragment in fase di runtime. Il FragmentManager mantiene uno stack di back delle transazioni di fragment su cui è possibile navigare.

Il metodo FragmentManager.beginTransaction() crea e restituisce un'istanza di **FragmentTransaction**. La classe FragmentTransaction utilizza una **fluent interface**: i metodi che configurano FragmentTransaction restituiscono un FragmentTransaction invece di void, il che consente di concatenarli.

- Il metodo add() della FragmentTransaction ha due parametri: un ID del container view e il newFragment. L'ID del container view è l'ID risorsa del FrameLayout definito nel layout dell'attività. Un ID del container view ha indica al FragmentManager dove nella vista dell'attività dovrebbe apparire la vista del fragment e viene utilizzato come identificatore univoco per un fragment nell'elenco del FragmentManager.

Quando è necessario recuperare il Fragment dal FragmentManager, lo si richiede tramite l'ID del container view utilizzando fm.findFragmentById(R.id.fragment_container).

È prassi comune aggiungere un **metodo statico newInstance()** alla classe Fragment. Questo metodo crea l'istanza del fragment, raggruppa e imposta i suoi argomenti.

### **Stato di un Fragment**

Ogni istanza di fragment può avere un oggetto Bundle allegato. Questo bundle contiene coppie chiave-valore,

Per creare gli argomenti di un fragment, si crea prima un oggetto Bundle. Quindi, si utilizzano i metodi "put" specifici del tipo di Bundle (simili a quelli di Intent) per aggiungere argomenti al bundle.

Per allegare il bundle degli argomenti a un fragment, si chiama Fragment.setArguments(Bundle). L'allegamento degli argomenti a un fragment deve essere fatto dopo che il fragment è stato creato ma prima che venga aggiunto a un'attività.

Quando un fragment deve accedere ai suoi argomenti, chiama il metodo getArguments() del Fragment e quindi uno dei metodi "get" specifici del tipo di Bundle.

### **Comunicazione tra Activity e Fragment**

Per delegare funzionalità all'attività ospitante, un fragment definisce in genere un'**interfaccia di callback** denominata Callbacks. Questa interfaccia definisce il lavoro che il fragment deve far svolgere all'attività ospitante. Qualsiasi attività che ospiterà il fragment deve implementare questa interfaccia.

Con un'interfaccia di callback, un fragment è in grado di chiamare metodi sulla sua attività ospitante senza dover sapere nulla di quale attività lo stia ospitando.

L'attività viene assegnata nel metodo del ciclo di vita del Fragment: onAttach(Activity activity). Questo metodo viene chiamato quando un fragment viene collegato a un'attività, sia che sia stato conservato o meno.

Allo stesso modo, la variabile viene impostata su null nel corrispondente metodo del ciclo di vita in diminuzione: onDetach(). La variabile viene impostata su null qui perché in seguito non è possibile accedere all'attività o contare sulla sua continua esistenza.

### **Conservazione dei Fragment**

Per impostazione predefinita, la proprietà retainInstance di un fragment è false. Ciò significa che non viene conservato e viene distrutto e ricreato alla rotazione insieme all'attività che lo ospita. La chiamata a setRetainInstance(true) conserva il fragment. Quando un fragment viene conservato, il fragment non viene distrutto con l'attività. Invece, viene preservato e passato intatto alla nuova attività.

Quando si conserva un fragment, si può contare sul fatto che tutte le sue variabili d'istanza mantengano gli stessi valori.

Un fragment conservato non viene distrutto, ma viene **staccato dall'attività morente**. Questo mette il fragment in uno **stato di conservazione**. Il fragment esiste ancora, ma non è ospitato da alcuna attività. Lo stato di conservazione viene raggiunto solo quando si verificano due condizioni:

1.  setRetainInstance(true) è stato chiamato sul fragment
2.  l'attività ospitante viene distrutta per un cambio di configurazione

Riceverà l'evento **onDetach** quando l'attività padre viene distrutta, seguito dagli eventi **onAttach**, **onCreateView** e **onActivityCreated** quando viene creata un'istanza della nuova attività padre.
