# **COMPUTAZIONE PERVASIVA**

Con lo sviluppo delle nuove tecnologie che ha portato alla nascita dei dispositivi di compilazione portabili è nata una nuova forma di computazione, quella **pervasiva**.

Essendo i dispositivo mobili e non più fissi si è dovuto cercare un nuovo modo di far comunicare i vari dispositivi per via delle connessioni precarie e in continuo cambiamento. Si cerca di progettare anche un software che sia in grado di utilizzare meno risorse possibili e che abbiano una potenza di calcolo minore per evitare di esaurire le risorse del dispositivo punto di tutto questo si occupa l'anno mobile computing. Questi dispositivi pervasivi sono sistemi distribuiti e quindi questi problemi dei sistemi distribuiti e mobile fanno parte del pervasive computing a cui si aggiungono altri problemi come la scalabilità invisibilità la comunicazione remota ecc.

Non tutti gli obiettivi del pervasive computer sono stati realizzati infatti creare uno **smartplace**, uno spazio in cui ci sono dispositivi di calcoli in modo da calcolare il mondo fisico e cyber fisico è ancora difficile da realizzare, ma non perché non possediamo le tecnologie adeguate ma perché dobbiamo migliorare i collegamenti.

È necessario rendere questi dispositivi **invisibili**, l'uomo non si deve accorgere che ci sono in modo che il mondo fisico e il cyber fisico si fondono in un solo spazio. Un altro problema è dovuto al numero sempre crescendo i dispositivi che si connettono tra loro quindi si cerca di realizzare la **scalabilità localizzata** cioè di mantenere le stesse qualità di servizi ma man mano che aumentano i nuovi dispositivi.

Sì cerca di mascherare le **condizioni di non uniformità** dovute diversi dispositivi presenti che possono impedire di collaborare fra loro cercando di creare un sistema per nascondere alle domande e questi problemi.

La computazione pervasiva ha modificato anche il modo in cui ci interfacciamo col software perché prima era necessario l'intervento umano per far svolgere qualcosa la macchina mentre oggi il computer è in grado di comunicare con tende anche in maniera asincrona.

Questo è stato reso possibile grazie al fatto che prendono informazioni nel mondo reale tramite i sensori sono in grado di elaborarli e notificare all'uomo qualcosa.

Oggi sia una architettura ed Edge cloudcentrica in cui tutti i dispositivi sono connessi tra loro tramite il cloud in cui le risorse informatiche sono regate attraverso la rete internet ospitate e gestite da server remoti.

Si provvede di avere un architettura ed internet centrica con cui internet il centro delle connessioni fra i dispositivi e i server. In questo modo l'elaborazione avviene in modo distribuita ai margini della rete contrariamente a come accade in quelle precedenti in cui le elaborazione avviene in economia i server.

Nell'architettura di calcolo distribuita ci sono tre segmenti che rappresentano muri diversi di elaborare e archiviare dati a seconda delle distanze dal punto di generazione

**📍 Edge Computing** Alla base di tutto troviamo l’**Edge**, ovvero il bordo della rete. I dati vengono elaborati **il più vicino possibile alla fonte che li genera**, spesso direttamente all’interno del dispositivo stesso. I dati vengono elaborati in tempo reale, senza dover prima inviare i dati a un server esterno.

Questo approccio è ideale per situazioni in cui la velocità è fondamentale, come nelle auto a guida autonoma o nei dispositivi medici. Riduce la latenza, cioè il tempo che passa tra l’input e la risposta, e limita il traffico di rete.

**🌫️ Fog Computing** Salendo di un livello, troviamo il **Fog Computing**, un modello pensato per distribuire l’elaborazione più vicino alla rete, ma non necessariamente sul dispositivo.

Nel fog computing, i dati vengono inviati a **nodi** local, un router o un server che li elaborano e, solo se necessario, li inoltrano al cloud. Questo modello è utile quando bisogna elaborare rapidamente grandi quantità di dati provenienti da più dispositivi, ma non si ha la necessità di farlo in tempo reale estremo.

**☁️ Cloud Computing** Infine, abbiamo il **Cloud**, che rappresenta l’approccio centralizzato. I dati vengono inviati a server remoti, spesso situati in data center geograficamente lontani. Qui possono essere elaborati con grande potenza computazionale, salvati per lungo tempo o usati per addestrare algoritmi complessi di intelligenza artificiale.

Il cloud è perfetto per elaborazioni intensive. Tuttavia, presenta limiti in termini di latenza e dipendenza dalla connessione internet.

Edge, Fog e Cloud non si escludono a vicenda: **collaborano**. In un sistema moderno ed efficiente, i dati vengono prima processati localmente (edge), poi aggregati e raffinati in una rete vicina (fog), e infine archiviati o ulteriormente analizzati nel cloud.

<div class="page-break"></div>
<div class="page-break"></div>
# **HCI**

La **Human computer interaction HCI** Eh lo studio dell’interazione uomo computer per la progettazione di sistemi informatici che siano usabili e affidabili. Il loro scopo è quello di semplificare l’attività umane e non di ostacolarle. Se hai il computer che le persone offrono diversi modi di interagire fra loro e l’interazione può essere

- diretta cioè tramite l’uso del dispositivo e di risposte da parte del calcolatore ;
- indiretta tramite sensori se analizzano il mondo esterno e danno dei feedback per svolgere azioni

La HCI è una materia multidisciplinare che coinvolge

![An infographic showing "HCI" (Human–Computer Interaction) in a large central circle surrounded by overlapping colored circles, each naming a related discipline: - Computer science - Ergonomics & human factors - Engineering - Design - Sociology & social psychology - Ethnography - Cognitive science - Psychology - Information security - Speech‑language pathology](./Android_images/image_002.png)

Il principio base della disciplina è

**usabilità** cioè la facilità con il quale l'utente può interagire con la macchina per raggiungere obiettivi con efficacia, efficienza e soddisfazione per un certo contesto

≠

**accessibilità** che indica se un sistema informatico può essere usato da tutti compreso chi ha disabilità

**Interazione umana**

L'uomo è colui che usa i calcolatori e devono essere progettati per assisterlo. Qui entrano in gioco le scienze cognitive che devono capire le capacità e le limitazioni per progettare in modo corretto un sistema informatico

Interazione processo con il quale l'utente fornisce la macchina in un input e la macchina lo processa restituendo un output o viceversa

Per la macchina si sono molte forme di IO, ma per l'essere umano sono principalmente i cinque sensi e più in particolare la vista l'udito e il tatto. Interagiamo con la macchina principalmente con il tatto, le dita fungono da cursore. Solo recentemente siamo in grado di interagire anche con la voce per fornire un input.

![- Photo of an older person with short white hair (face blurred). - Wearing a light blue patterned sweater over a white collared shirt. - Seated against a warm yellow background, with one hand up near the face. - A dark object (likely a laptop or book) is visible in the lower right.](./Android_images/image_003.png)
**Vista** La vista è il principale mezzo con il quale otteniamo informazioni. La percezione visiva si può dividere in due fasi

1.  ricezione fisica dello stimolo
2.  elaborazione e un'interpretazione dello stimolo

Dobbiamo capire come funziona l'occhio e come la mente interpreta gli stimoli per progettare sistemi informatici. La prima cosa da capire è cosa l'utente vede punto la vista umana tende ad avere una visione centrale dove l’utente di attento e nota le cose; è una visione centrale che trascura le cose che sono fuori da quella centrale.

Capire questo ci permette di realizzare un design utile all’utente

🡪 le info importanti devono essere al centro del campo

🡪 le info meno importanti devono essere più all'esterno

Importante è capire anche come percepiamo i colori, dimensioni, e profondità per una buona progettazione delle interfaccia visive.
Bisogna definire il contesto in cui gli oggetti si trovano perché diamo sulla base di esso o un'interpretazione diversa dovuta al fatto che possiamo già conoscere il contesto e le info relative da conoscenze passate.
Definiamo correttamente il contesto permette all'utente di capire subito di cosa si tratta ed evita le illusioni ottiche che lo portano in disabilità quindi bisogna definire correttamente le dimensioni degli oggetti dove posizionarli e così via per poter sviluppare una buona interfaccia utente.

**Udito** Un altro canale di output per l'uomo può essere il canale uditivo grazie al quale siamo in grado di riconoscere i suoni in quanto il nostro sistema filtro i suoni che ascoltiamo per concentrarci sulle informazioni importanti il suono è spesso usato nelle interfacce grafiche ad esempio per dare informazioni sullo stato di qualcosa, focalizzare l'attenzione ecc.. quindi per notificare/rafforzare l'idea dell'utente.

**Tatto** Il tatto ci dà informazioni sull'ambiente circostante e specialmente nei sistemi informatici è la fonte di input ma anche di output. In questo modo siamo in grado di interagire con gli aggettivi fuori dagli smartphone in modo da svolgere determinati compiti. Anche i movimenti importanti perché comporta un elaborazione di informazioni in seguito a uno stimolo ricevuto toccando qualcosa. Ogni movimento richiede tempo che dipende dalle persone dall'età eccetera eccetera. In movimento si valuta con accuratezza cioè la precisione del movimento che dipende anche dalla velocità con il quale si reagisce. Quanto si progetta un’interfaccia e bisogna considerare queste caratteristiche del movimento per progettare i bottoni che siano facilmente raggiungibili e premibili. (Pubblicità ingannevole)

Il tempo impiegato per colpire un bersaglio è una funzione della dimensione del bersaglio della distanza da percorrere

**Legge di Fitts**

**Dispositivi** Il progettista dell'interfaccia deve essere a conoscenza delle proprietà del dispositivo e di tutti i fattori che influenzano il comportamento dell'interfaccia perché influenzano la natura dell’interazione.

Donald Norman da una definizione di interazione HC stabilimento che si tratta di un ciclo che si compone di due fasi

1. Esecuzione
2. Valutazione
   |
   V

L'utente stabilisce l'obiettivo, formula l'intenzione c'è l'obiettivo che deve realizzare, esegue le azioni sul dispositivo e percepisce lo stato del sistema e lo interpreta per capire il posto suggestivo per raggiungere l'obiettivo

È importante che l'utente capisca cosa fare per completare le loro azioni e le interfacce non devono essere di un tralcio anzi devono semplificare il raggiungimento dell'obiettivo.

**DESIGN SBAGLIATO** 🡪**lapsus** cioè quando comprendiamo il sistema ma si fanno

| errori di distrazione
V

**errori** quando si sbaglia perché non si è capito il sistema e quindi cosa deve fare per raggiungere l’obiettivo

**Ergonomia** L’ergonomia è lo studio delle caratteristiche fisiche dell’interazione quindi come progettare i controlli layout dei dispositivi ecc.

L'obiettivo è di migliorare come l’utente usi dispositivi per dare migliori prestazioni sull'uso di questi punto questo si riflette anche sul design, su come posizionare gli elementi sulla base dell'utilità del contesto ecc.

Quando progettiamo l'interfaccia dobbiamo tenere conto anche di come gli utenti usano i dispositivi infatti secondo studi la maggior parte delle persone usano il dispositivo con una mano sola e usano il pollice per toccare lo schermo, oppure con la seconda mano lo fissiamo oppure usano entrambe le mani quindi in base a come viene utilizzato progettiamo il design mettendo gli elementi importanti nelle parti dello schermo più facilmente raggiungibili in base alle modalità di uso mentre gli elementi meno utili o di uso frequente nelle parti più esterne un design corretto porta ad avere una pessima esperienza d'uso per l'utente finale

# **ARCHITECTURAL UI AND DATA MANAGEMENT PATTERNS**

Prima ancora di scrivere codice, è importante **definire l’architettura del sistema**. Progettare l’architettura in anticipo permette di avere una visionechiara di come sarà strutturata l’applicazione, come interagiranno i diversi componenti tra loro e quali saranno le dipendenze principali.

Questo ha un impatto diretto sulla qualità del progetto nel lungo periodo. Se in futuro sarà necessario apportare modifiche, aggiungere funzionalità, sostituire una tecnologia, risolvere bug o adattarsi a nuove esigenze… avere un’architettura solida e ben pensata renderà tutto più semplice, veloce e sicuro.

È necessario strutturare il sistema in modo che sia indipendente dai framework, librerie e linguaggi che usiamo perché cambiano nel tempo: nuove versioni, nuove API, a volte addirittura vengono abbandonati o sostituiti da soluzioni migliori. Se il nostro sistema dipende troppo da queste tecnologie, ogni cambiamento porta ad errori o riscritture pesanti del codice.

a **modularità** è uno dei concetti più importanti. Significa **suddividere un sistema in parti indipendenti e riutilizzabili**, chiamate moduli o componenti, ognuno dei quali ha una responsabilità chiara e ben definita.

Conviene pensare alla **modularità** cioè dividere il codice in moduli in modo che sia più semplice da capire, da testare, da manutenere e da evolvere. Ogni modulo può essere sviluppato (e perfino sostituito) senza dover riscrivere tutto il resto. Dobbiamo fare attenzione alle **dipendenze circolari** che si verificano quando due (o più) moduli dipendono l’uno dall’altro direttamente o indirettamente. Questo crea una **situazione di interdipendenza**, dove nessuno dei moduli può essere isolato, testato o riutilizzato in modo indipendente.

Il principio che si trova alla base di ogni pattern architetturale è la **separazione dei problemi** in livelli in modo da avere le dipendenze verso un’unica direzione ed evitare le dipendenze circolari. I vari livelli non devono avere riferimenti ai livelli più esterni di loro, questo violerebbe la modularità e renderebbe quindi i livelli dipendenti fra loro.

## **CLEAN ARCHICTURE**

La **Clean Architecture** mira a creare sistemi **intercambiabili** con una forte **separazione delle preoccupazioni** e un **accoppiamento debole** tra i livelli.

L'idea fondamentale di Clean Architecture, concepita da Robert Martin (Uncle Bob), è rendere **intercambiabile** ogni elemento all'interno di un certo confine architetturale, senza richiedere modifiche nei livelli sottostanti.

Le dipendenze del codice sorgente possono puntare solo verso l'interno. Questo significa che i livelli interni non devono dipendere da livelli. Questa direzione delle dipendenze è fondamentale per ottenere un basso accoppiamento e facilitare il test e la manutenzione.

La Clean Architecture divide un'applicazione in diversi livelli con responsabilità distinte:

1. Domain/Application Core: Contiene le entità e la logica di business dell'applicazione. Questo livello è indipendente da qualsiasi framework o dettaglio di implementazione esterna.
2. Use Cases: Il software in questo livello contiene regole aziendali specifiche dell'applicazione ed incapsula e implementa tutti i casi d'uso del sistema. Questi casi d'uso orchestrano il flusso di dati da e verso le entità e indirizzano tali entità per raggiungere gli obiettivi del caso d'uso. I cambiamenti in questo livello non devono influenzare le entità e questo livello non è influenzato da modifiche alle componenti esterne come il database, l'interfaccia utente o qualsiasi framework utilizzato. Questo strato è isolato da tali problematiche. Tuttavia, modifiche alle funzioni di dominio dell'applicazione influenzeranno i casi d'uso e quindi il software in questo livello.
3. Infrastructure/Frameworks: Contiene i dettagli di implementazione dei sistemi esterni, come database, framework UI, librerie esterne e API. Le implementazioni delle interfacce definite nel livello Application risiedono qui.
4. Interface Adapters: Questo livello funge da ponte tra i livelli Application e Infrastructure. Contiene adapter, presentatori e controller che convertono i dati da un formato all'altro per soddisfare le esigenze dei diversi livelli.
5. API/UI: Il livello più esterno che presenta l'applicazione all'utente (tramite un'API web o un'interfaccia utente grafica).

**![A simple diagram of a "hub-and-spoke" architecture: - A dark central rectangle (the hub) in the middle. - Five lighter rectangles arranged around it (the spokes): top, top-left, top-right, bottom-left, bottom-right. - Arrows between each outer rectangle and the central rectangle indicating connections/communication. - Caption beneath: "Figure 3‑1. Hub and spoke architecture."](./Android_images/image_034.png)**

Per attraversare i confini (cerchi concentrici) si usano i controller e i Presenter che comunicano con i casi d'uso nel livello successivo.

1. l'esecuzione inizia nel controller
2. si sposta attraverso il caso d'uso
3. finisce per essere eseguito nel presenter.

Per implementare questa logica si utilizza il **principio di inversione delle dipendenze** che consente ad A di chiamare metodi su un'astrazione implementata da B, rendendo possibile per A chiamare B in fase di esecuzione, ma per B di dipendere da un'interfaccia controllata da A in fase di compilazione (invertendo così la tipica dipendenza in fase di compilazione). In fase di esecuzione, il flusso di esecuzione del programma rimane invariato, ma l'introduzione di interfacce significa che diverse implementazioni di queste interfacce possono essere facilmente collegate. La stessa tecnica viene utilizzata per attraversare tutti i confini nelle architetture.

Sfruttiamo il polimorfismo dinamico per creare dipendenze del codice sorgente che si oppongono al flusso di controllo in modo che possiamo rispettare la regola delle dipendenze indipendentemente dalla direzione in cui sta andando il flusso di controllo.

![A simple cartoon/clipart of a smiling man wearing an orange hard hat, brown suit, white shirt and blue tie. He holds a laptop in one hand and waves with the other; the style is flat, friendly, on a plain white background.](./Android_images/image_035.png)

Il **Repository Pattern** è spesso integrato in Clean Architecture come un meccanismo per **astrarre l'accesso ai dati**. L'interfaccia del repository è definita nel livello Application, mentre l'implementazione concreta che interagisce con il database si trova nel livello Infrastructure. Questo rispetta la regola della dipendenza, poiché il livello Application dipende solo dall'interfaccia del repository, non dalla specifica implementazione del database.

La separazione dei livelli e la regola della dipendenza rendono le applicazioni Clean Architecture più **facili da testare**. I casi d'uso e la logica di business nel livello Application possono essere testati unitariamente senza dipendere da database o UI. Le interfacce nel livello Application facilitano il **mocking** delle dipendenze esterne durante i test. L'accoppiamento debole tra i livelli rende le applicazioni Clean Architecture più **scalabili e manutenibili**. Le modifiche a un livello hanno meno probabilità di influenzare altri livelli, facilitando l'aggiornamento e l'aggiunta di nuove funzionalità.

I ViewModel spesso interagiscono con un **Repository** per l'accesso ai dati. Questa struttura (UI - ViewModel - Repository - Data Source) in Android può essere vista come un'implementazione pratica di alcuni principi di Clean Architecture, in particolare la separazione delle preoccupazioni e l'astrazione dell'accesso ai dati.

Una potenziale violazione della regola della dipendenza in Clean Architecture quando si implementa il Repository pattern utilizzando direttamente un ORM (come Entity Framework Core) nel livello Infrastructure. Questo introduce una dipendenza del livello Interface Adapters (dove si troverebbe l'implementazione del repository) verso un framework esterno e verso l'I/O diretto, violando la dipendenza verso l'interno. Per risolvere questo, si suggerisce di spostare l'implementazione del repository nel livello Frameworks/Infrastructure e di definire le interfacce nel livello Application.

## **LIVEDATA**

LiveData è una classe di dati **osservabile** che è legata al ciclo di vita dei componenti UI, come **Activity** o **Fragment**. Questo significa che **LiveData** permette di aggiornare la UI automaticamente quando i dati cambiano, ma solo quando la UI è in uno stato attivo, evitando aggiornamenti inutili o errori quando la UI non è visibile (ad esempio, se l'**Activity** è in background). Implementa il pattern Observer.

## **ROOM**

Room è una libreria di persistenza fornita da Google che si colloca all'interno dei componenti dell'architettura Android, con l'obiettivo di semplificare l'interazione con il database **SQLite** del sistema operativo, fornendo un **livello di astrazione**.

Room è descritta come un modo efficace per creare database e salvare dati. Fornisce un accesso al database SQLite **mappando oggetto-relazionale (ORM)** basato su annotazioni.

L'utilizzo di Room si articola principalmente su tre tipi di classi:

- Entità: Sono Plain Old Java Objects (POJO) che modellano i dati da trasferire verso e dal database. Sono annotate con @Entity, specificando la tabella del database a cui corrispondono. Almeno una proprietà deve essere designata come chiave primaria usando l'annotazione @PrimaryKey. Room crea una tabella nel database per ogni entità.
- DAOs - Data Access Objects: Definiscono l'API per interagire con i dati, contenendo metodi per operazioni come query, inserimenti, aggiornamenti ed eliminazioni. I DAOs sono interfacce o classi astratte annotate con @Dao. Le operazioni sul database sono definite all'interno dei metodi del DAO tramite annotazioni come @Query, @Insert, @Update e @Delete. Room genera l'implementazione concreta di queste interfacce o classi astratte in fase di compilazione.
- Database: Rappresenta l'interfaccia principale al database SQLite sottostante. È una classe astratta che estende RoomDatabase ed è annotata con @Database, elencando tutte le entità utilizzate dal database e la sua versione. Contiene metodi astratti che restituiscono istanze dei DAO. Si ottiene un'istanza del database tramite un RoomDatabase.Builder.
- Relazioni tra Entità: Sebbene Room supporti relazioni tramite chiavi esterne definite con l'annotazione @ForeignKey, non supporta riferimenti diretti tra entità. Per rappresentare relazioni uno-a-molti o molti-a-molti e accedere agli oggetti correlati, si utilizza l'annotazione @Relation all'interno di una classe POJO separata che contiene i campi per le entità correlate. Per le relazioni molti-a-molti è necessario implementare una "join entity" che crea la tabella di join associata.

![Image: a diagram of "The Clean Architecture." - Four concentric colored rings with inward dependency rule: - Center (yellow): "Entities" — Enterprise business rules. - Next (red): "Use Cases" — Application business rules. - Next (green): "Controllers / Presenters / Gateways" — Interface adapters. - Outer (blue): "Devices / Web / UI / DB / External Interfaces" — Frameworks & drivers. - Arrows pointing inward showing that outer layers depend on inner layers, not vice versa. - Legend mapping colors to layer types. - Small flow diagram at right: Controller → Use Case Input Port → Use Case Interactor → Use Case Output Port → Presenter, with a "Flow of control" arrow indicated.](./Android_images/image_036.png)

In Room, le **entità sono pensate più come Data Transfer Objects (DTO)** oggetti concepiti come un **mezzo per trasferire dati** tra diversi punti di un'applicazione. Modellano una risposta o sono ottimizzati per la creazione e la persistenza dei dati. Le Entity in Room rappresentano i dati che si desidera memorizzare nel database e sono anche l'unità tipica di un set di risultati recuperato dal database

![The diagram shows two views of the same design: "Compile Time" (left) and "Run Time" (right). - Compile Time (left): a dashed box containing Class A (blue) that holds references to Interface B (gray). Interface B points to Class B (green) as its implementation/reference. Similarly, Interface C (gray) points to Class C (purple). Labels "References" mark the connections — the code compiles against interfaces, and concrete classes are referenced indirectly. - Run Time (right): a dashed box showing control flow. Class A (blue) calls into Interface B which at runtime is bound to Class B (gray/green stacked). Control flow continues from Class B into Interface C bound to Class C (gray/purple stacked). Labels "Control Flow" indicate actual runtime linking of interface to implementation.](./Android_images/image_037.png)

Room può essere integrato con **LiveData** per **osservare i cambiamenti nel database**. Un DAO può restituire un oggetto **LiveData** da una query, consentendo all'interfaccia utente di aggiornarsi automaticamente quando i dati sottostanti cambiano.

Room si integra bene con **ViewModel**, che gestisce i dati relativi alla View in modo indipendente dai cambiamenti di configurazione. Il ViewModel può interagire con il database tramite un repository che utilizza Room.

È una buona pratica utilizzare il **pattern Repository** come livello intermedio tra Room e il resto dell'applicazione. Questo permette di **astrarre l'accesso ai dati** e, se in futuro vorrai cambiare il tipo di persistenza (ad esempio passare da Room a una sorgente di rete o cache), potrai farlo **senza modificare** i ViewModel o altri componenti della business logic.

## **MVC**

Il **[[MVC]] Model View Controller** è un modo per organizzare le funzionalità di un'applicazione separando gli oggetti in tre ruoli distinti:

![Diagram of how a Room database is used in an app: - Top: "Room Database" (blue rounded box). - Middle left: "Data Access Objects" (DAOs, green). - Arrow to/from Room Database: DAOs fetch entities from the DB and persist changes back to it. - Arrow from the app into DAOs: "Get DAO". - Middle right: "Entities" (red). - DAOs return Entities to the app; the app reads/writes entity fields ("get / set field values"). - Bottom: "Rest of The App" (gray). - The app obtains DAOs, receives Entities, and manipulates entity fields; persistence flows through DAOs to the Room Database.](./Android_images/image_038.png)

![- A layered architecture diagram showing how data flows from client DTOs through service and DAO layers into the database. - Left: blue "DTO" circles feed into a blue "Service Implementation" box that exposes operations like "findBy..." and "create". - Middle: orange "Bean" nodes connect the service layer to a red "DAO Implementation" box that provides "findByCriteria", "create", "update", "delete". - Right: a cylindrical "Database" with a "Table" receives CRUD requests from the DAO. - Arrows illustrate call flow: DTO → Service → Bean → DAO → Database (and results flow back the same path).](./Android_images/image_039.png)Gli oggetti del modello non hanno alcuna conoscenza dell'interfaccia utente (UI). Il loro unico scopo è la gestione e la detenzione dei dati.

**Model** Il modello contiene i dati dell'applicazione e la logica di business.Le classi del modello sono progettate per rappresentare le entità con cui l'app lavora, come una domanda vero/falso. In Android, il livello del modello è generalmente costituito da classi personalizzate create dallo sviluppatore. Il modello può anche specificare la struttura dei dati dell'app e il codice per accedervi e manipolarli.

**View** La vista è responsabile della visualizzazione dei dati all'utente e della risposta alle azioni dell'utente. Ogni elemento visibile sullo schermo è una vista. Android fornisce molteplici tipi di viste. Le viste sanno come disegnarsi sullo schermo e come rispondere all'input dell'utente, come i tocchi.

**Controller** Il controllore agisce come un intermediario tra il modello e la vista. Contiene la logica dell'applicazione .I controllori rispondono agli eventi innescati dalle viste e gestiscono il flusso di dati da e verso il modello e la vista. In Android, un controllore è tipicamente una sottoclasse di Activity, Fragment o Service.

È importante notare che il modello e la vista non comunicano direttamente. Il controllore si trova al centro, ricevendo messaggi da un lato e inviando istruzioni all'altro.

### **Benefici dell'MVC**

- Separazione delle responsabilità: Aiuta a progettare e comprendere l'applicazione come un insieme di classi distinte.
- Migliore organizzazione del codice: La separazione in livelli (modello, vista, controllore) facilita la progettazione e la comprensione dell'applicazione a un livello superiore.
- Riutilizzabilità del codice: Le classi con responsabilità limitate sono più riutilizzabili.

### **Observer Synchronization**

Questo approccio, strettamente associato all'MVC, si basa sul concetto che **le viste e i controllori osservano il modello**.

Quando il **modello subisce una modifica**, viene notificato a tutti i suoi osservatori (le viste e potenzialmente i controllori).

Le **viste reagiscono a queste notifiche** aggiornando la propria visualizzazione in base ai nuovi dati del modello.

Il **controllore**, in questo modello, è **relativamente "ignorante"** di quali altre viste potrebbero aver bisogno di essere aggiornate quando l'utente interagisce con una specifica vista. Il controllore si limita a modificare il modello, lasciando che il meccanismo di osservazione si occupi di propagare i cambiamenti alle viste interessate.

### **Flow Synchronization**

Nella sincronizzazione tramite flusso, è l'applicazione (spesso il controllore) che manipola direttamente le viste per riflettere i cambiamenti nel modello. Ad esempio, quando si apre una schermata o si preme un pulsante di salvataggio, il codice dell'applicazione si occupa di aggiornare esplicitamente i vari controlli (viste) con i dati del modello. In questo caso, il form (o l'attività/il fragment in Android) deve tenere traccia di quali controlli devono essere aggiornati in seguito a un cambiamento, il che può diventare complesso in schermate elaborate.

## **MVVM**

![- A schematic of the Model–View–Controller (MVC) design pattern. - Three main boxes: - Controller (blue, top) — labeled “Mediator”. - View (green, left) — inside a dotted “UI” oval. - Model (orange, right) — inside a dotted “Data” oval. - Labeled interactions (arrows): - “User action” from View → Controller. - “Update” from Controller → Model. - “Notify” from Model → Controller. - “Update” from Model → View. - Overall: the controller mediates user actions, updates the model; the model notifies the controller and/or pushes updates to the view, and the view renders the UI.](./Android_images/image_040.png)Il pattern **MVVM Model-View-ViewModel** permette una gestione più fluida della UI e una separazione più chiara tra la logica di business e l'interfaccia utente.

Il pattern MVVM è composto da tre componenti principali:

1. Model
2. View
3. ViewModel che da intermediario tra la View e il Model. È responsabile della gestione dei dati da visualizzare nella UI e dell'elaborazione della logica necessaria per presentarli. La ViewModel fornisce i dati alla View tramite LiveData, che consente di osservare i cambiamenti dei dati e aggiornare automaticamente la UI quando necessario. La ViewModel non ha conoscenza diretta della View. Comunica con il Model per recuperare i dati e li prepara in una forma che la View può facilmente consumare.

### **Interazione tra i componenti nel pattern MVVM**

1. L'utente interagisce con la View (ad esempio, tocca un pulsante).
2. La View invia un'azione al ViewModel (ad esempio, invoca un metodo che cambia i dati).
3. Il ViewModel interagisce con il Model per recuperare o modificare i dati. In caso di operazioni asincrone, il ViewModel gestisce il flusso di lavoro.
4. Quando il Model restituisce i dati (ad esempio tramite una chiamata API), il ViewModel li prepara (ad esempio, li converte in un formato adatto alla visualizzazione).
5. Il ViewModel aggiorna un LiveData, che è osservato dalla View.
6. La View riceve i nuovi dati tramite LiveData e aggiorna automaticamente l'interfaccia utente.

In questo modo, ogni componente ha un compito preciso:

- la UI si concentra solo sulla presentazione e l’interazione,
- il ViewModel gestisce la logica di visualizzazione,
- il Repository coordina l’accesso ai dati,
- e il livello Model (Room + Retrofit) fornisce le sorgenti dati reali.
