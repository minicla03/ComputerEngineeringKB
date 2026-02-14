# **INTENT**

In Android, un **Intent** è un meccanismo IPC per comunicare con il sistema operativo e fra le applicazioni. Gli Intent sono messaggi che effettuano una richiesta all'Android runtime per avviare un'activity o un altro componente dell'app o di un'altra app. Invece di avviare direttamente le activity, si costruiscono Intent con la classe Intent e si chiama il metodo startActivity() per inviare l'intent.

Un **Intent esplicito** specifica l'activity (o un altro componente) ricevente tramite il suo nome di classe completo. Si utilizzano Intent espliciti per avviare componenti all'interno della propria applicazione. Per creare un Intent esplicito, si utilizza un Context e un oggetto Class. Il metodo newIntent() può essere utilizzato per configurare correttamente un Intent esplicito con gli extra necessari. L'activity ricevente ottiene l'Intent con getIntent() e recupera i dati dagli extra. È anche possibile avviare un'activity aspettandosi un risultato utilizzando startActivityForResult(Intent, requestCode). L'activity chiamata invierà un risultato tramite un altro Intent, e l'activity chiamante riceverà il risultato nel metodo onActivityResult(). Una Activity avviata tramite startActivity è indipendente da quella chiamante e non fornirà alcun dato di risposta alla chiusura.

Laddove è richiesto un feedback, è possibile avviare un'attività come subactivity che può restituire irisultati al suo genitore. Per fare questi si utilizza startActivityForResult(). Quando la sub-activity è pronta per essere restituita, si utilizza setResultprima della fine per restituire un risultato all'attività chiamante.Il metodo setResultaccetta due parametri: **il codice** del risultato e **i dati del risultato stesso**, **rappresentati come un Intent.**

Il codice del risultato indica il successo dell'esecuzione dell'attività secondaria (RESULT_OK) o insuccesso (Activity.RESULT_CANCELED).

Un **Intent implicito** non specifica un'activity o un altro componente specifico per ricevere l'intent. Invece, si dichiara un'azione generica da eseguire nell'intent. Il sistema Android abbina la richiesta a un'activity o a un altro componente in grado di gestire l'azione richiesta (**late binding**). Se più activity corrispondono, all'utente viene presentata una finestra di dialogo di selezione dell'app. Le activity dichiarano la loro capacità di gestire Intent impliciti tramite i **filtri di intent** definiti nel file AndroidManifest.xml. Per inviare un **Intent implicito**, si crea un oggetto Intent specificando l'azione, i dati (se presenti) e il tipo MIME dei dati. Prima di chiamare un Intent implicito, è buona pratica verificare se ci sono activity in grado di gestirlo chiamando resolveActivity(getPackageManager()). Se si desidera mostrare sempre all'utente un chooser di app quando più app possono gestire l'intent, si può utilizzare Intent.createChooser(Intent target, String title).

Il passaggio da un'Activity ad un'altra coinvolge i cicli di vita di entrambe. La prima, quella messa a riposo, dovrà passare almeno per onPause() e onStop() mentre la seconda percorrerà la catena di creazione onCreate-onStart-onResume. La priorità del sistema è **il mantenimento della fluidità della _user-experience_**, quindi:

- La prima Activity passa per onPause e viene fermata in stato Paused;
- La seconda Activity va in Running venendo attivata completamente. In tale maniera l'utente potrà usarla al più presto non subendo tempi di ritardo;
- a questo punto, mentre l'utente sta già usando la seconda Activity, il sistema può invocare onStop sulla prima.

### **FILTRI**

I **filtri di intent** sono dichiarazioni nel file manifest di un componente dell'app (solitamente un'attività, un servizio o un ricevitore di broadcast) che specificano i tipi di intent che il componente può gestire.

I filtri di intent sono fondamentali per il funzionamento degli **intent impliciti**. Quando un'applicazione invia un intent implicito, il sistema Android utilizza i filtri di intent dichiarati da tutte le app installate per determinare quale componente è il più adatto a gestire la richiesta.

I filtri di intent sono dichiarati nel file AndroidManifest.xml all'interno dell'elemento <activity>, <service> o <receiver> usando uno o più elementi <intent-filter> che può contenere tre tipi di elementi che corrispondono alle informazioni contenute in un oggetto Intent:

- <action>: Specifica l'azione generica che il componente può eseguire. Le azioni sono definite come costanti nella classe Intent. Un intent implicito deve contenere un'azione che corrisponda ad almeno una delle azioni dichiarate nel filtro. È possibile specificare più azioni all'interno dello stesso filtro.
- <category>: Fornisce informazioni aggiuntive sulla categoria del componente che dovrebbe gestire l'intent. Le categorie sono definite come costanti nella classe Intent. Un intent deve corrispondere a tutte le categorie specificate in un filtro per passare. È importante notare che tutte le attività che intendono ricevere intent impliciti devono includere la categoria android.intent.category.DEFAULT, in quanto questa categoria viene aggiunta implicitamente a tutti gli oggetti Intent impliciti dal sistema Android.
- <data>: Specifica il tipo di dati che il componente può gestire. Questo include il tipo MIME dei dati o altri attributi di un URI (come lo schema, l'host, la porta e il percorso). Un intent può specificare un URI di dati e/o un tipo MIME. Il filtro può dichiarare quali schemi URI e tipi MIME sono supportati.

Per un intent implicito affinché venga consegnato a un componente, l'intent deve superare i test di **tutti e tre gli elementi (azione, categoria e dati)** definiti in almeno uno dei filtri di intent dichiarati dal componente. Se un componente ha più filtri di intent, un intent che non corrisponde a un filtro potrebbe comunque corrispondere a un altro.

### **GLI EXTRAS**

Gli Intent è che essi, nel recapitare questo messaggio, portano con se dati che possono essere letti dal destinatario. Questi valori condivisi mediante Intent vengono chiamati **Extras** e possono essere di varie tipologie, sia appartenenti a classi più comuni che ad altre purché serializzabili. La gestione degli Extras negli Intent funziona in maniera simile ad una struttura dati HashMap: con dei metodi putviene inserito un valore etichettato con una chiave e con i corrispondenti metodi get viene prelevato il valore, richiedendolo mediante la chiave di riconoscimento.

### **PARAMTRI INTENT**

**Activity class (per Intent espliciti)**: il nome della classe dell'activity o del componente che dovrebbe ricevere l'intent.

**Intent action**: l'azione generica che l'activity ricevente dovrebbe eseguire. Le azioni disponibili sono definite come costanti nella classe Intent e iniziano con ACTION\_. Esempi includono ACTION_VIEW, ACTION_SEND e ACTION_PICK.

**Intent category**: fornisce informazioni aggiuntive sulla categoria del componente che dovrebbe gestire l'intent. Le categorie sono opzionali e possono essere aggiunte con il metodo addCategory(). Esempi includono CATEGORY_LAUNCHER, CATEGORY_DEFAULT e CATEGORY_BROWSABLE. Per rispondere a Intent impliciti, un filtro di intent deve impostare esplicitamente la categoria DEFAULT, che viene aggiunta implicitamente a ogni Intent implicito.

**Intent data**: contiene un riferimento ai dati su cui l'activity ricevente dovrebbe operare, come un oggetto Uri. Può rappresentare un URL web, un numero di telefono o un percorso a un file. Il tipo di dati può anche essere specificato con il metodo setType(), utilizzando un tipo MIME.

**Intent extras**: coppie chiave-valore che trasportano informazioni aggiuntive richieste dall'activity ricevente. I valori possono essere tipi primitivi o oggetti che implementano l'interfaccia Parcelable. I metodi putExtra() vengono utilizzati per aggiungere extra a un Intent, e getIntent().getExtras() o metodi specifici come getStringExtra() o getIntExtra() vengono utilizzati per recuperarli nell'activity ricevente.

**Intent flags**: metadati aggiuntivi che istruiscono il sistema Android su come avviare un'activity o come trattarla dopo l'avvio.

### **TIPI DI INTENT**

Un **broadcast intent** è un tipo di intent che non avvia un'activity specifica, ma viene consegnato a tutti i **broadcast receiver** interessati registrati per tale intent. I broadcast receiver sono componenti che ascoltano specifici broadcast di sistema o personalizzati.

Un **PendingIntent** è un token che si concede a un'altra applicazione per utilizzare le autorizzazioni del proprio processo per eseguire un'azione in un secondo momento. Viene spesso utilizzato per le notifiche.

Un **IntentService** è una sottoclasse di Service che gestisce le richieste intent in background, una alla volta.
