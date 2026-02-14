# Unit Testing (JUnit)

Il testing è fondamentale per assicurarsi che un'app si comporti come previsto in ogni situazione, specialmente man mano che l'app cresce e cambia.

Aiuta a **identificare i problemi nelle prime fasi dello sviluppo**, quando sono meno costosi da risolvere, e migliora la robustezza del codice. Ci sono vari tipi di test:

- unit test è una verifica che si concentra sul comportamento di una singola unità di codice. Questa "unità" di codice è solitamente una singola funzione o un metodo. L'obiettivo è garantire che quella specifica parte del codice funzioni correttamente in isolamento, senza dipendenze esterne.
- Component test si verifica se le classi fra loro collaborano bene
- integration test si concentrano sull'interazione tra più unità di codice, per verificare che diversi componenti funzionino insieme come previsto. Mentre i unit test testano singole unità in isolamento, gli integration test verificano la corretta integrazione di più unità, come moduli, librerie o servizi, e se queste interazioni producono il comportamento desiderato.

Il testing automatizzato rende più facile eseguire test su diverse configurazioni di dispositivi e stati. Scriverli da tutti sarebbe una follia.🤪

Bisogna individuare i test suite e usare dei framework per poter scrivere test in modo automatico. Lo scopo dei test non è di rimuovere gli errori, ma di capire cosa non funziona per poterli risolvere il problema.

![- Simple clip‑art showing two interlocking gears (cogwheels). - One larger gear on the left and a smaller gear on the right. - Bluish‑gray color with lighter inner rings; plain white background.](./Android_images/image_043.png)

I test suite vengono dati ad un **test runner** che gli esegue e crea delle **test class** con i **method test** eseguendo per ogni metodo delle operazioni:

- Setup: Prima dell'esecuzione dei metodi di test, il test runner può invocare metodi di setup che sono utilizzati per configurare le risorse necessarie per il test
- Esecuzione dei Test: I metodi di test vengono eseguiti uno alla volta.
- Tear Down: Dopo l'esecuzione di un test, possono essere invocati metodi di teardown per liberare risorse, come la chiusura di connessioni al database o la pulizia di dati temporanei.

Una volta che i test sono stati eseguiti, il test runner crea un **report dei risultati**. Questo report mostra:

- I test che sono passati.
- I test che sono falliti.
- I test che hanno generato errori (ad esempio, eccezioni non gestite).

Android supporta diverse tipologie di test e framework di testing.

**JUnit 4** è un framework comune per scrivere unit test in Java per Android.

![The image is a horizontal, numbered workflow diagram (green panels) for building a software/mobile app, with Italian labels. Key elements: - Five main stages, left→right: 1. Requirements Analysis 2. Wireframing 3. Development / Designing 4. Testing 5. Deployment - Stages 3 and 4 are highlighted with a red dashed box and linked to detailed action lists. - Top annotations (Italian): define view navigation, define content structure for each view, verify/validate the app, generate acceptance reports, obtain client approval after changes. - Under each stage are short bullets (Italian/English): - Requirements: understand user needs, identify functions to implement, identify constraints/limits. - Development: application design, application coding, meetings with stakeholders. - Deployment: deploy to app stores, deploy to client server, make app available to users. - Two detailed boxes below: - Development (3.x): 3.1 Definire le risorse 3.2 Progettare ed implementare l'applicazione 3.3 Generare il package dell'applicazione 3.4 Installare & e lanciare l'applicazione - Testing (4.x): 4.1 Verificare il comportamento dell'applicazione 4.2 Identificare i problemi 4.3 Ristrutturare il codice sorgente 4.4 Rigenerare il package dell'applicazione - Visual style: flat green tiles with icons, circular number markers, connector lines from stages to the detailed boxes.](./Android_images/image_044.png)Il framework JUnit implementa il composite, quindi possiede il TestSuite (compose) e i TestCase (leaf).

Per creare gli unit Test si crea una classe test che implementa i metedi:

- setUp()
- tearDown
- TestXXX
- Suite()

Nei metodi di test ci mettiamo le **asserzioni** per verificare che il comportamento del codice corrisponda a quanto previsto.

La libreria Hamcrest è uno strumento utile per scrivere asserzioni nei test, permettendo di creare regole di matching in modo dichiarativo.

**1. Framework di Unit Test di "Prima Generazione"**

Nei framework di unit test di prima generazione, il concetto di base è che un test deve verificare che una condizione sia vera durante l'esecuzione del codice. Questo avviene tramite l'istruzione assert, che verifica una condizione booleana e, se la condizione non è vera, fa fallire il test.

I framework di "prima generazione" forniscono un messaggio di errore generico, come "Assertion failed", che non è particolarmente utile per capire cosa sia andato storto.

**2. Framework di Unit Test di "Seconda Generazione"**

I framework di unit test di seconda generazione migliorano la situazione fornendo una serie di **asserzioni specializzate** che sono in grado di produrre messaggi di errore più chiari e specifici, adattandosi a diversi tipi di confronti (ad esempio, uguaglianza, differenza, ecc.).

Alcuni esempi includono:

- assert_equal(x, y): Verifica che x e y siano uguali.
- assert_not_equal(x, y): Verifica che x e y non siano uguali.

Queste asserzioni specializzate sono più esplicite e forniscono messaggi di errore più significativi. Tuttavia, il problema principale di questo approccio è che il numero di macro di asserzione tende a crescere rapidamente, perché ogni tipo di confronto richiede una macro di asserzione

**3. Framework di Unit Test di "Terza Generazione"**

I framework di unit test di **terza generazione** (come **Hamcrest**, un popolare framework di asserzione in Java) risolvono questo problema introducendo un approccio più **generico e composibile**. In questi framework, l'operatore assert_that viene combinato con **matcher** (oggetti che eseguono verifiche su una condizione).

Un **matcher** è una classe o un oggetto che definisce una condizione che può essere verificata. In questo caso, assert_that viene utilizzato per affermare che un oggetto soddisfi una determinata condizione definita dal matcher.

**![A diagram showing how an automated unit test runs: - Left: a "Test runner" box with an arrow labeled "Executes" pointing to a vertical "Test class" column containing several "Test method" boxes. - From one test method a dashed line leads to a four-step block: Setup → Execute → Verify → Teardown. - Arrows from Setup/Execute/Teardown point into an oval labeled "Fixture" that contains a highlighted rectangle labeled "SUT" (system under test). - Caption: each automated test is a test method in a test class and follows four phases — setup (initialize fixture), execute (invoke SUT), verify (check outcome), teardown (clean up fixture).](./Android_images/image_045.png)MOCKITO (mock a mamm’t) 😵**

**Mockito** è un framework di mocking che può essere utilizzato per isolare le unità di codice durante l'esecuzione di unit test.

Permette di creare oggetti **mock** (fittizi o simulati) che si comportano come le dipendenze di un'unità di codice che stai testando. Questo è utile perché consente di **testare la logica specifica di un componente in isolamento**, senza doversi preoccupare del comportamento reale delle sue dipendenze.

**Mockito** è specificamente menzionato nel contesto della creazione di unit test. Quando si esegue un unit test, l'obiettivo è verificare la logica di una piccola porzione di codice (come un metodo o una classe).

Android permette due tipi di test:

- Local Unit TestQuesti test vengono compilati ed eseguiti interamente sulla tua macchina locale utilizzando la Java Virtual Machine (JVM). Sono utilizzati per testare la logica interna dell'app che non richiede l'accesso all'Android framework o a un dispositivo/emulatore1 .
- Instrumented TestQuesti test vengono eseguiti su un dispositivo o emulatore Android.

![Image: a UML-style diagram titled "JUnit framework". - Center/top: a small box labeled "Test" with arrows from a "Testing client" (left) and a return arrow labeled "fTests". - Left-center: "TestCase" box showing methods: run(TestResult), setUp(), runTest(), tearDown(). - Right-center: "TestSuite" box showing methods: run(TestResult), addTest(Test); a note: "for all test in fTests test.run(TestResult)". - Middle: "TestResult" box linked to TestCase (result collection). - Lower-center: "ConcreteTestCase" (subclass of TestCase) listing setUp(), runTest(), tearDown(), test1(), test2(), fName. - Bottom-left: "TestedClass" with action() method; arrow from ConcreteTestCase to TestedClass (uses the class under test). - Various solid and dashed lines/arrows indicate inheritance, aggregation, and method-calling relationships (TestCase runs tests and reports to TestResult; TestSuite contains Tests and runs them).](./Android_images/image_046.png)
