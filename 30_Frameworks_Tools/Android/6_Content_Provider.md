# **CONTENET PROVIDER**

Un **Content Provider** è un componente di Android che gestisce l'accesso a un repository di dati. L'applicazione non ha bisogno di sapere dove o come i dati sono archiviati, formattati o acceduti.

![The diagram shows how an Android BroadcastReceiver works: - Top: "Android system" (Android robot in a cloud). - Bottom: "Broadcast receiver" (Android robot). - Step 1 (arrow from receiver to system): "Register for Broadcast intent." - Step 2 (arrow from system to receiver): "onReceive()" — the system delivers the broadcast to the receiver. - Dotted lines and radiating signal icon indicate the broadcast flow between the system and the receiver.](./Android_images/image_019.png)

Un Content Provider separa i dati dal codice dell'interfaccia utente dell'app, fornendo un **modo standard** per accedere ai dati. Rende possibile la condivisione di dati tra diverse applicazioni. (Pattern Adapter)

Consente a più applicazioni di accedere, utilizzare e modificare in modo sicuro una singola origine dati fornita dalla tua app.

Per ottenere dati e interagire con un Content Provider, un'app utilizza un **ContentResolver** per inviare richieste al Content Provider.
L'applicazione di un fornitore può specificare le autorizzazioni che altre applicazioni devono avere per accedere ai dati del fornitore. Queste autorizzazioni consentono all'utente di sapere a quali dati un'applicazione tenta di accedere. In base ai requisiti del fornitore, altre applicazioni richiedono le autorizzazioni necessarie per accedere al fornitore. Gli utenti finali vedono le autorizzazioni richieste quando installano l'applicazione.

Se l'applicazione di un provider non specifica alcuna autorizzazione, le altre applicazioni non avranno accesso ai dati del provider, a meno che il provider non venga esportato.

Per rendere disponibile un ContentProvider all'interno di un'app Android, è necessario **dichiararlo esplicitamente** nel file AndroidManifest.xml, all’interno del tag <application> tramite l'elemento <provider>, che contiene una serie di attributi fondamentali.

- android:name, che specifica il nome completo della classe che implementa il ContentProvider.
- android:authorities, che rappresenta un identificatore univoco del provider. Questo valore viene utilizzato dalle app per costruire gli URI di accesso al provider. Per esempio, se l’authority è com.miaapp.provider, l’URI per accedere a una risorsa potrebbe essere content://com.miaapp.provider/risorse.
- android:exported. Questo valore determina se il provider può essere accessibile da altre app. Se impostato su true, il provider potrà essere utilizzato anche da app esterne, mentre se è false, sarà accessibile solo dall’interno dell’applicazione stessa. Questo è un parametro importante per la sicurezza, specialmente se i dati gestiti sono sensibili.

È anche possibile specificare dei **permessi di accesso** per controllare quali app possono leggere o scrivere dati tramite il provider. Questo si fa aggiungendo gli attributi android:readPermission e android:writePermission, dove si indicano i nomi dei permessi richiesti. Le app che vogliono accedere al provider dovranno dichiarare nel proprio manifest questi permessi, e l’utente li vedrà al momento dell’installazione.

L'architettura di un Content Provider include i seguenti componenti:

- Data and Open Helper: Il repository dei dati. Comunemente i dati sono archiviati in un database SQLite, ma possono essere anche file, dati sul web o dati generati dinamicamente. Per i database SQLite, si utilizza spesso un SQLiteOpenHelper per l'accesso ai dati.
- Contract: Una classe pubblica che espone informazioni importanti sul Content Provider ad altre app. Include solitamente gli schemi URI, costanti importanti e la struttura dei dati restituiti. L'uso di un contract separa le informazioni pubbliche da quelle private e fornisce un unico punto di riferimento per le altre app.
- Content Provider: Una classe che estende ContentProvider e implementa i metodi query(), insert(), update() e delete() per accedere ai dati. Fornisce un'interfaccia pubblica e sicura ai dati.
- Content Resolver: Un oggetto utilizzato dalle app per inviare richieste al Content Provider e ottenere i dati. Fornisce i metodi query(), insert(), update() e delete() che rispecchiano quelli del Content Provider.

Per implementare un Content Provider, è necessario:

- Avere i dati e un modo per accedervi
- Dichiarare il Content Provider nel file AndroidManifest.xml per renderlo disponibile. È importante impostare l'attributo android:exported="true" se si desidera che altre app possano accedervi.
- Creare una sottoclasse di ContentProvider che implementi i metodi per l'accesso e la manipolazione dei dati (query(), insert(), delete(), update(), getType()).
- Definire una classe Contract pubblica che esponga l'URI scheme, i nomi delle tabelle, i tipi MIME e altre costanti importanti.

### **URI e tipi MIME**

Le app inviano richieste ai Content Provider utilizzando gli **Uniform Resource Identifier (URI)**. Un content URI ha la forma generale scheme://authority/path/ID, dove lo scheme è sempre content://, l'authority rappresenta il dominio del provider (solitamente il nome del package che termina con .provider), il path è il percorso ai dati e l'ID identifica univocamente un set di dati. Il contract definisce costanti per l'AUTHORITY, il CONTENT_PATH e il CONTENT_URI.

Il **tipo MIME** indica il tipo e il formato dei dati restituiti dal Content Provider. Per i Content URI che puntano a righe di una tabella, si utilizzano tipi MIME specifici del vendor Android, con il formato generale type.subtype/provider-specific-part. Il type è vnd, il subtype è android.cursor.item/ per una singola riga e android.cursor.dir/ per più righe, e la parte specifica del provider include solitamente il nome del package e il nome della tabella. Il metodo getType() del Content Provider restituisce il tipo MIME dei dati per un dato URI.

Il ContentResolver fornisce metodi (query(), insert(), delete(), update()) che corrispondono a quelli implementati nel ContentProvider.

- Il metodo query() viene utilizzato per recuperare dati e restituisce un oggetto Cursor, che è un puntatore a una riga di dati strutturati in formato tabellare, simile a un risultato di una query SQL. La query può includere una proiezione (le colonne da restituire), una clausola di selezione (il WHERE), gli argomenti di selezione e l'ordine di ordinamento (ORDER BY).
- I metodi insert(), delete() e update() vengono utilizzati per modificare i dati. Il metodo insert() riceve i valori da inserire come ContentValues e restituisce l'URI della nuova riga.

È buona pratica utilizzare un UriMatcher per gestire il matching degli URI all'interno del Content Provider, associando ogni URI supportato a un codice intero.
