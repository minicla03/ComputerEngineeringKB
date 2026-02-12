# **COMPILAZIONE APP ANDROID**

Per quanto riguarda la compilazione di un app android prima di generare il bytecode, le risorse usate nel processo vengono analizzate indicizzate e compilate in bytecode, ottimizzato per la piattaforma punto la componente. La componente che si occupa di fare questo è **AAPT2** che opera il modo **incrementale** cioè compila le risorse e linka tutti i file intermedi generati dalla compilazione. Produce la classe **R.java** che contiene tutte le risorse compilate a cui sono associate un ID con il quale si può far riferimento alla risorsa.

Viene generato il bytecode del codice Java/Kotlin.

La componente **AIDL** definisce l’interfaccia di programmazione concordata dal client e server per comunicare fra loro usando IPC. Il motivo di ciò è che ogni app, anche se viene eseguita sullo stesso dispositivo, e un processo separato e quindi può accedere solo alle zone di memoria che le sono state riservate.

Android usa un meccanismo nativo chiamato **Binder** per gestire la comunicazione tra processi. È una tecnologia di basso livello, integrata nel kernel di Linux, che permette a un processo di:

- Fare richieste a un altro processo
- Ricevere risposte come se fossero normali chiamate di funzione

Con tutte queste parti si viene a creare il .class cioè il file bytecode Java che però non può essere ancora utilizzato ma deve essere ottimizzato dalla componente **DEX/ART** creando un file .dex eseguibile su ART VM.

Una volta pronti i file .dex e le risorse, lo strumento **apkbuilder** li unisce per creare il file .apk, cioè il pacchetto installabile dell’app Android. Dentro questo .apk troviamo:

- I file .dex
- Le risorse compilate (.arsc)
- I file non compilati (come asset, immagini, XML di layout)
- Il file AndroidManifest.xml

Prima che un'app venga installata su un dispositivo, **deve essere firmata digitalmente**. Questo garantisce due cose fondamentali:

- Autenticità: conferma che l’app è stata creata da chi dice di averla creata.
- Integrità: assicura che il file non sia stato modificato dopo la firma.

**a) Firma con jarsigner**

La firma avviene usando uno **keystore**, ovvero un contenitore sicuro di chiavi crittografiche. Con jarsigner, il pacchetto .apk viene firmato utilizzando una **chiave privata**.

- Si calcola un hash del contenuto dell’app.
- Questo hash viene poi cifrato con la chiave privata → questo è ciò che chiamiamo firma digitale.
- La firma viene allegata all’app.

**b) Allineamento con zipalign**

Dopo la firma, si utilizza lo strumento zipalign per **ottimizzare l’accesso alle risorse** del pacchetto. Questo è un passo importante, soprattutto per app in produzione, perché migliora le prestazioni e riduce il consumo di memoria.

Quando un dispositivo Android riceve un’app firmata, esegue la **verifica della firma**:

- Estrae l’hash dal file firmato.
- Ricalcola l’hash con il contenuto dell’app.
- Usa la chiave pubblica per verificare che la firma corrisponda all’hash originale.

Se i due hash corrispondono, l’app è autentica e non è stata manomessa → viene installata. Se **non combaciano**, il sistema rifiuta l’installazione.

- Durante lo sviluppo, Android Studio firma automaticamente l’app con una chiave debug.
- Per pubblicare l’app sul Play Store, devi firmarla con una chiave di release generata da te. È fondamentale non perdere questa chiave, perché ti servirà per aggiornare l’app in futuro.

![compilazione_app_schema](assets/compilazione_app_schema.png)

# **AVVIO DI UN APPLICAZIONE ANDROID**

Il processo di avvio di un'applicazione Android inizia quando l'utente o un altro componente di sistema richiede l'esecuzione di un componente dell’app. Se l'applicazione non è già in esecuzione, il sistema Android avvia un nuovo processo per essa.

Ogni app Android viene eseguita nel proprio processo Android, che è un processo Linux con un thread di esecuzione iniziale.

Il processo di avvio del sistema include l'avvio dell'**init process**, che a sua volta genera processi Linux di basso livello chiamati **daemon**. L'init process avvia un processo chiamato **Zygote** che inizializza la prima istanza della Dalvik Virtual Machine e precarica tutte le classi comuni utilizzate dal framework Android e dalle varie app installate.
In questo modo, si prepara a essere replicato e inizia ad ascoltare su un'interfaccia socket per richieste future di generare nuove macchine virtuali per i processi delle nuove applicazioni. Quando riceve una nuova richiesta, Zygote effettua un fork di se stesso per creare un nuovo processo che ottiene un'istanza VM pre-inizializzata. Dopo Zygote, l'init avvia il **runtime process,** e Zygote esegue un fork per avviare un processo ben gestito chiamato **system server**. Il system server avvia tutti i servizi principali della piattaforma, come l'Activity Manager Service e i servizi hardware, nel proprio contesto.

A questo punto, lo stack completo è pronto per avviare il primo processo dell'app: l'app Home, nota anche come **Launcher**.

Quando un utente fa clic sull'icona di un'app nel Launcher, l'evento di clic viene tradotto in _startActivity(intent)_ e viene indirizzato all'**ActivityManagerService** tramite Binder IPC. L'ActivityManagerService esegue diverse operazioni:

1. Raccoglie informazioni sul target dell'oggetto intent utilizzando il metodo resolveIntent() sull'oggetto PackageManager, con i flag PackageManager.MATCH_DEFAULT_ONLY e PackageManager.GET_SHARED_LIBRARY_FILES utilizzati per impostazione predefinita.
2. Salva le informazioni sul target nell'oggetto intent per evitare di ripetere questo passaggio.
3. Verifica se l'utente ha privilegi sufficienti per richiamare il componente target dell'intent chiamando il metodo grantUriPermissionLocked().
4. Se l'utente ha le autorizzazioni necessarie, l'ActivityManagerService verifica se l'attività target richiede di essere avviata in un nuovo task, in base ai flag dell'Intent come FLAG_ACTIVITY_NEW_TASK e FLAG_ACTIVITY_CLEAR_TOP.
5. Verifica se esiste già un ProcessRecord per il processo. Se il ProcessRecord è null, l'ActivityManager deve creare un nuovo processo per istanziare il componente target.

L’ASM crea un nuovo processo invocando il metodo startProcessLocked(), che invia argomenti al processo Zygote tramite la connessione socket. Zygote esegue un fork di se stesso e chiama ZygoteInit.main(), che a sua volta istanzia un oggetto ActivityThread e restituisce l'ID del processo appena creato. Ogni processo ottiene un thread per impostazione predefinita. Il thread principale ha un'istanza **Looper** per gestire i messaggi da una coda di messaggi e chiama Looper.loop() in ogni iterazione del suo metodo run(). Il Looper estrae i messaggi dalla coda e richiama i metodi corrispondenti per gestirli. ActivityThread avvia quindi il message loop chiamando Looper.prepareLoop() e successivamente Looper.loop().

Il passo successivo consiste nell'associare questo processo appena creato a un'applicazione specifica. Ciò avviene chiamando bindApplication() sull'oggetto thread. Questo metodo invia un messaggio BIND_APPLICATION alla coda dei messaggi. Questo messaggio viene recuperato dall'oggetto **Handler**, che quindi invoca il metodo handleMessage() per attivare l'azione specifica del messaggio: handleBindApplication(). Questo metodo invoca makeApplication(), che carica le classi specifiche dell'app in memoria.

![app_launch_schema](assets/app_launch_schema.png)

Dopo il binding, il sistema contiene il processo responsabile dell'applicazione con le classi dell'applicazione caricate nella memoria privata del processo. Il processo effettivo di avvio inizia nel metodo realStartActivity(), che chiama scheduleLaunchActivity() sull'oggetto thread dell'applicazione. Questo metodo invia un messaggio LAUNCH_ACTIVITY alla coda dei messaggi. Il messaggio viene gestito dal metodo handleLaunchActivity(). L'**Activity** inizia il suo ciclo di vita .

![Zygote](assets/zygote.png)
