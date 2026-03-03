# **NOTIFICHE**

Una **notifica** è un messaggio che un'app visualizza all'utente al di fuori interfaccia utente dell'applicazione. Quando si indica al sistema di emettere una notifica, questa appare per la prima volta all'utente come un'icona nell'area di notifica, sul lato sinistro della barra di stato. Per vedere i dettagli della notifica, l'utente apre il **drawer** di notifica o visualizza la notifica sulla schermata di blocco se il dispositivo è bloccato. L'area di notifica, la schermata di blocco e il drawer di notifica sono aree controllate dal sistema che l'utente può visualizzare in qualsiasi momento.

Le notifiche sono il modo in cui Android consente di visualizzare informazioni al di fuori della propria applicazione. Consentono all'utente di essere avvisato delle informazioni dalle applicazioni installate, anche se non le sta utilizzando al momento. Questo è particolarmente utile quando nuove informazioni, come email o messaggi, arrivano sul dispositivo in modo **asincrono**. Quando progettiamo le notifiche dobbiamo evitare di disturbare l’utente per notizie inutile, perché l’utente distraendosi può decidere di cancellare l’applicazione.

Quando si progettano le notifiche, è fondamentale ricordare che **interrompono sempre l'utente**. Pertanto, devono essere,:

# 1. Brevi: Utilizza il minor numero possibile di parole. Sii conciso. Evita di irritare gli utenti inviando troppe notifiche o notifiche con contenuti inutili o fastidiosi.

# 2. Tempestive: Le notifiche devono apparire quando sono utili, altrimenti se arrivano i ritardo potremmo non servire più.

# 3. Pertinenti: l'informazione deve essere utile per l'utente. Notifiche che disturbino inutilmente l’utente o che lo possono trarre in inganno posso partare la cancellazione dell’applicazione.

La classe NotificationCompat.Builder permette di creare le notifiche ed è costruita secondo il pattern Builder. La notifica deve avere:

- Un ID che la identifica;
- Il contesto;
- Icona piccola da mostrare nella barra di stato. Questa è impostata con setSmallIcon().
- Titolo mostrato sopra il testo dettagliato. È impostato con setContentTitle().
- Testo dettagliato cioè il messaggio della notifica, un breve testo che descrive alcuni aspetti importanti È impostato con setContentText().

Questi metodi setter fanno parte della classe Builder e sono costruiti usando l’**interfaccia fluent** un **modello di progettazione** che permette di scrivere il codice in modo più leggibile e "fluente", simile a un linguaggio naturale, concatenando più metodi attraverso il **method chaining\***.\* Quindi tutti i metodi di settaggio della notifica, in questo caso, restituiscono l’oggetto Builder in modo da apportare più modifiche. Poi alla fine del settaggio si dovrà invocare un metodo di chiusura per ottenere l’oggetto.

La notifica può essere estesa mostrando più informazioni. Si usano le **viste espanse** nel drawer di notifica

# 1. NotificationCompat.BigTextStyle: Utilizzata per notifiche di grande formato che includono molto testo.

# 2. NotificationCompat.InboxStyle: Utilizzata per notifiche di grande formato che includono una lista di fino a cinque stringhe.

# 3. NotificationCompat.BigPictureStyle: Utilizzata per notifiche di grande formato che includono un grande allegato immagine. Puoi impostare l'immagine grande con bigPicture() e anche un titolo per il contenuto grande con setBigContentTitle().

# 4. Notification.MediaStyle: Utilizzata per notifiche di riproduzione multimediale.

Per applicare uno di questi stili a una notifica, utilizzi il metodo setStyle() sull'oggetto NotificationCompat.Builder. Quindi oltre ad implementare un pattern Builder, ne implementa anche una decorator.

Oltre al contenuto testuale o multimediale aggiuntivo, puoi mostrare più informazioni aggiungendo **azioni** alla notifica che l'utente può eseguire sulla notifica stessa, resa disponibile tramite un pulsante di azione. Queste azioni aggiungono funzionalità e permettono all'utente di interagire direttamente con la notifica per accedere o manipolare le informazioni.

**Pending Intent**

Quando usiamo delle notifiche modifichiamo il pattern navigazionale dell’applicazione, perché per evitare di far percorrere tutta la strada per arrivare al punto di interesse, possiamo permettere all’utente di cliccare sulla notifica e di essere indirizzato direttamente li. Quindi aggiungiamo dei deep link per arrivare direttamente nelle zone di interesse.

Questo è realizzato tramite PendingIntent un oggetto che **incapsula un Intent**. Il suo scopo è permettere a un'altra applicazione o al sistema Android di eseguire un Intent per conto della tua applicazione, in un momento futuro. Questo è particolarmente utile perché garantisce che il sistema possa consegnare l'Intent anche se la tua app non è in esecuzione nel momento in cui l'utente interagisce con esso.

Quando si crea un PendingIntent si ottiene un **token** che non è l'Intent stesso, ma una **riferimento o un permesso** mantenuto dal sistema operativo. Quando consegni questo PendingIntent (token) a un altro componente, quel componente può utilizzare il token per chiedere al sistema di eseguire l'Intent originale come se fosse stato avviato dalla app che l’ha creato.

I PendingIntent sono comunemente utilizzati in vari scenari in cui un'azione deve essere posticipata o eseguita da un altro componente di sistema o un'altra app per conto della tua:

- Notifiche: Quando l'utente tocca una notifica, solitamente si vuole che venga avviata un'Activity della tua app. Per fare ciò, si incapsula l'Intent che avvia l'Activity in un PendingIntent e lo si imposta sulla notifica usando setContentIntent().
- Allarmi: L'AlarmManager può attivare un PendingIntent dopo un certo periodo di tempo o a intervalli regolari.
- Broadcast: Un PendingIntent può incapsulare un Intent da inviare come broadcast,

Per creare un'istanza di un PendingIntent, si utilizzano metodi statici appropriati a seconda di come si desidera che l'Intent contenuto venga consegnato:

- PendingIntent.getActivity(): Per un Intent che dovrebbe essere consegnato usando startActivity(). Si passa un Intent esplicito per l'Activity che si desidera avviare.
- PendingIntent.getService(): Per un Intent che dovrebbe essere passato a startService()
- PendingIntent.getBroadcast(): Per un Intent broadcast consegnato con sendBroadcast().

Ciascuno di questi metodi per creare PendingIntent richiede solitamente i seguenti argomenti:

# 1. Il contesto dell'applicazione.

# 2. Un codice di richiesta (un ID per distinguere i PendingIntent).

# 3. L'Intent da consegnare.

# 4. Un flag PendingIntent che determina come il sistema gestisce più oggetti PendingIntent dalla stessa applicazione.

Se richiedi un PendingIntent due volte con gli stessi parametri si ottiene lo stesso oggetto PendingIntent.

**Notification Channel**

Un altro principio di progettazione è quello di **dare agli utenti la possibilità di scegliere** tramite le impostazioni dell’app i tipi di notifiche che desiderano ricevere e come desiderano riceverle. Questo è possibile realizzarlo a partire dall’API26 che permette di creare dei **NotificationChannel** per offrire all'utente un maggiore controllo sui tipi di notifiche che riceve dall'applicazione. Quando si crea un canale, si definiscono alcune impostazioni iniziali, ma l'utente può personalizzare ciascun canale e decidere come si comporta.

- Azioni: Un'azione che l'utente può intraprendere sulla notifica. L'azione è resa disponibile tramite un pulsante adiacente al contenuto della notifica. Un'azione utilizza un PendingIntent per completare l'azione. Si aggiunge un'azione usando il metodo addAction() passando l'icona, la stringa del titolo e il PendingIntent da attivare.
- Importance
- Priorità: Influenzano il modo in cui il sistema Android consegnerà la notifica. Le notifiche hanno una priorità tra MIN (-2) e MAX (2). Le priorità disponibili includono PRIORITY_MAX (critiche/urgenti), PRIORITY_HIGH (comunicazioni importanti come messaggi), PRIORITY_DEFAULT (quelle che non rientrano nelle altre categorie), PRIORITY_LOW (informazioni non urgenti) e PRIORITY_MIN (informazioni di sfondo "nice-to-know"). La priorità è impostata con setPriority(). Sono rimaste più per un fatto di compatibilità con le versioni precedenti.
- Notifiche continue/Servizi in foreground (setOngoing(), startForeground()): Le notifiche continue non possono essere eliminate dall'utente e devono essere esplicitamente cancellate dall'app. Vengono utilizzate per indicare attività in background con cui l'utente interagisce attivamente (come la riproduzione di musica) o attività che occupano il dispositivo (come download). Per rendere una notifica continua, si imposta setOngoing() su true. Un servizio in foreground richiede che visualizzi una notifica visibile all'utente. Per avviare un servizio in modalità foreground e visualizzare la notifica, si utilizza startForegroundService() e startForeground(), passando un ID di notifica univoco e l'oggetto notifica. L'ID intero passato a startForeground() non deve essere 0. Per rimuovere un servizio dal foreground, si chiama stopForeground(), specificando se rimuovere la notifica.

**Gestione delle notifiche**

Il **NotificationManager** è un **servizio di sistema** utilizzato per **consegnare** o attivare le notifiche. Per ottenere un'istanza del NotificationManager, devi chiamare il metodo getSystemService(), passando la costante NOTIFICATION_SERVICE. Non si dovrebbe mai chiamare questo direttamente, ma usare il NotificationMangerCompact che garantisce anche la retrocomatibilità con le versioni precedenti.

La funzione principale del NotificationManager è quella di **mostrare la notifica all'utente**. Ciò si fa chiamando il metodo notify(). Il metodo notify() richiede due parametri:

# 1. Un ID di notifica (un numero intero), utilizzato per aggiornare o annullare la notifica in seguito. Dovrebbe essere unico all'interno della tua applicazione. Se chiami notify() più volte con lo stesso tag e ID, sostituirà qualsiasi notifica esistente con lo stesso tag e ID. Questo è il modo in cui puoi implementare, ad esempio, una barra di avanzamento o altre visualizzazioni dinamiche in una notifica.

# 2. L'oggetto Notification stesso. Questo oggetto viene tipicamente costruito utilizzando la classe NotificationCompat.Builder.

A partire dall'API 26 , il NotificationManager è anche responsabile della gestione dei **canali di notifica**, infatti è obbligatorio associare la notifica ad un canale. Puoi utilizzare il NotificationManager per controllare se un canale esiste già e, in caso contrario, creare un nuovo oggetto. Questo dà all'utente un maggiore controllo sui tipi di notifiche che riceve dall'applicazione, poiché può personalizzare le impostazioni per ciascun canale.

Le notifiche rimangono visibili fino a quando non si verifica una delle seguenti condizioni:

- L'utente le ignora individualmente o tramite "Cancella tutto"
- Chiami setAutoCancel(true) sul builder della notifica, in tal caso la notifica scompare quando l'utente ci clicca sopra.
- Chiami cancel() per un ID di notifica specifico.
- Chiami cancelAll() per far sparire tutte le notifiche che hai emesso.

![- Diagram: a simple sequence diagram for the MVC pattern. - Top row: three labeled boxes — Controller (orange), Model (purple), View (blue). - Each box has a vertical dashed lifeline descending beneath it. - Message flow (top to bottom): 1. Controller: handleEvent (internal/starting action). 2. Controller → Model: updateModel (synchronous message). 3. Model → View: update (notifies view). 4. View → Model: getData (view requests data). - Arrows connect lifelines to show the call/notification sequence; colors match the participant boxes.](./Android_images/image_041.png)**APP SETTING**

Le app settings si riferiscono alle **preferenze dell'utente** che consentono di **modificare le caratteristiche e i comportamenti dell'applicazione**. Sono controlli che catturano le preferenze degli utenti che influiscono sulla maggior parte di essi o forniscono supporto critico a una minoranza. Esempi includono l'abilitazione delle notifiche o la frequenza di sincronizzazione dei dati con il cloud. In iOS, concetti simili ("user defaults") sono usati per preferenze come lingua, stile UI o unità di misura.

Gli utenti dovrebbero poter navigare alle impostazioni dell'app toccando un'opzione **Settings**. Questa opzione è solitamente collocata nella **navigazione lateral** o nel **menu opzioni**. Secondo le linee guida di design, l'opzione "Settings" dovrebbe trovarsi al di sotto di tutti gli altri elementi (eccetto Help e Send Feedback) sia nella navigazione laterale che nel menu opzioni.

Le impostazioni sono solitamente accessibili **infrequentemente**, poiché una volta che l'utente cambia un'impostazione, raramente ha bisogno di modificarla di nuovo. Se un controllo o una preferenza necessita di accesso frequente, è meglio spostarlo nel menu opzioni della app bar o in un menu di navigazione laterale. È importante impostare dei **valori di default** per le impostazioni che siano familiari agli utenti e migliorino l'esperienza dell'app. I default dovrebbero rappresentare la scelta più comune, usare meno batteria, comportare il minor rischio per la sicurezza/perdita di dati, e interrompere solo quando importante. Informazioni sull'app come numero di versione o licenze dovrebbero essere spostate in una schermata di Help separata.
