# Maven

Parent: [[Building_Tools_MOC]]

![maven_logo](assets/maven_logo.png)

**Maven** è un progetto open source sviluppato da **Apache** che facilita l'organizzazione efficiente di un progetto Java. Rende più facile gestire e mantenere grandi progetti fornendo una struttura coerente e una serie di convenzioni su come organizzare il progetto, aiutando gli sviluppatori ad automatizzare il processo di **build**, test e distribuzione del software.

Una delle caratteristiche principali di Maven è la sua capacità di gestire le dipendenze. Maven tiene traccia di tutte le librerie e altre dipendenze necessarie per un progetto e le scarica automaticamente quando sono richieste. Questo rende facile per gli sviluppatori utilizzare librerie esterne nei loro progetti senza doverle scaricare e gestire manualmente.

Maven **obbliga** ad avere una **struttura fissa** delle directory

- Il POM è alla radice del progetto
- Poi ci sono due directory:
  - **src**: contiene il sorgente
  - **target**: contiene i file generati alla fine del processo di compilazione

Avendo a disposizione il **POM** e la directory **src**, chiunque può essere in grado di ricostruire la directory **target**

## POM (Project Object Model)

Maven utilizza un approccio dichiarativo per specificare la build e le dipendenze del progetto. Il file centrale che Maven utilizza è il **pom.xml** (**Project Object Model**). Questo file gestisce le dipendenze del progetto, i plugin e la configurazione della build. Inoltre, Maven offre una serie di plugin integrati per attività comuni e può essere esteso con plugin personalizzati.

## Repository Maven

Un **repository Maven** è una directory che contiene i file compilati insieme ai relativi metadati. I metadati si riferiscono ai file POM associati a ciascun progetto. Questi metadati consentono a Maven di scaricare le dipendenze necessarie per il progetto.

Maven dispone di tre tipi di repository:

1. **Repository Locale**: Il repository locale si trova sulla macchina dello sviluppatore e contiene tutte le dipendenze, come i file JAR. Ogni sviluppatore ha il proprio repository locale.
2. **Repository Remoto**: Il repository remoto è situato su un server web e viene utilizzato quando Maven deve scaricare le dipendenze. Quando un artefatto non è presente nel repository locale, Maven lo scarica dal repository remoto e lo memorizza nel repository locale.
3. **Repository Centrale**: Il repository centrale è gestito dalla comunità Maven ed è la fonte principale da cui Maven scarica le dipendenze, qualora non siano presenti nei repository locali o remoti.

### Le Coordinate Maven

Il file **pom.xml** definisce le coordinate Maven per ciascun artefatto. Le coordinate sono composte da tre parti obbligatorie: **groupId**, **artifactId** e **version**. Questi elementi identificano in modo univoco un artefatto all'interno del repository Maven, agendo come un sistema di coordinate per i progetti.

1. **groupId**: Questo identificatore è generalmente univoco all'interno di un'organizzazione o di un progetto. Non è necessario che il groupId corrisponda alla struttura del pacchetto del progetto, ma è una buona pratica seguire la convenzione.
2. **artifactId**: L'artifactId è generalmente il nome del progetto. Insieme al groupId, definisce univocamente un progetto nel repository. È raro che venga menzionato separatamente, poiché il groupId è spesso condiviso tra più progetti all'interno della stessa organizzazione.
3. **version**: La version specifica la versione dell'artefatto. Questo campo è fondamentale per mantenere il versionamento del progetto e gestire modifiche e aggiornamenti.

### SNAPSHOT vs Release

La gestione delle versioni in Maven segue una logica rigorosa per garantire la riproducibilità della build. Le versioni possono essere classificate in due categorie principali:

- **SNAPSHOT**: Una versione contrassegnata dal suffisso -SNAPSHOT (es. 1.2.0-SNAPSHOT) indica un artefatto in fase di evoluzione.
  Quando un progetto dipende da uno SNAPSHOT, Maven controlla periodicamente (solitamente ogni 24 ore o forzando con -u, **Aggiornamento Dinamico**) se esiste una versione più recente nel repository remoto.
- **Release**: Una versione senza suffissi o con suffissi puramente numerici (es. 1.2.0) è considerata finale. Una volta pubblicata in un repository di release, una versione non deve mai essere sovrascritta. Se il codice cambia, deve necessariamente cambiare la versione (es. 1.2.1). Garantisce che una build eseguita oggi produca lo stesso identico risultato tra dieci anni, poiché le dipendenze di release sono statiche.

## Build Lifecycle

Il **Build Lifecycle** di Maven è un concetto centrale che definisce il flusso di esecuzione delle fasi di costruzione di un progetto, dal momento in cui avvii la build fino alla sua conclusione. Il ciclo di vita di Maven è suddiviso in una serie di fasi, e ogni fase rappresenta una parte specifica del processo di compilazione, test e distribuzione del progetto.

Maven prevede tre cicli di vita principali:

1. **default**: gestisce il processo di build del progetto.
2. **clean**: gestisce la rimozione dei file generati durante la build.
3. **site**: gestisce la creazione del sito web del progetto (documentazione e altre risorse).

### Default Build Lifecycle (Ciclo di Vita Predefinito)

Il ciclo di vita predefinito è il più importante e definisce le fasi che vengono eseguite durante la costruzione del progetto. Esso include fasi come la compilazione, l'esecuzione dei test, la creazione del pacchetto e il deploy.

Le fasi principali del ciclo di vita **default** sono:

1. **validate**: Verifica che il progetto sia corretto e che tutte le informazioni necessarie siano disponibili.
2. **compile**: Compila il codice sorgente del progetto.
3. **test**: Esegue i test unitari sul codice compilato per verificare che funzioni correttamente.
4. **package**: Crea il pacchetto del progetto (ad esempio, un file JAR, WAR o EAR) a partire dal codice compilato e dai file di configurazione.
5. **verify**: Verifica che il pacchetto sia valido e che i test siano passati.
6. **install**: Installa il pacchetto nel repository locale di Maven, rendendolo disponibile per altri progetti.
7. deploy: Distribuisce il pacchetto nel repository remoto per renderlo accessibile ad altri sviluppatori o progetti.

### GOAL

Un **goal** appresenta un'azione specifica da eseguire durante un ciclo di vita di build. I goal sono l'unità più piccola e specifica di un processo Maven e sono generalmente associati ai **plugin**. Ogni plugin può avere uno o più goal, e ogni goal è progettato per eseguire una particolare attività, come la compilazione del codice, l'esecuzione dei test, la creazione del pacchetto o la distribuzione.

Questi goal possono essere eseguiti direttamente dalla linea di comando o come parte di un ciclo di vita di Maven.

### Maven Profiles

I profili consentono di adattare il processo di build a contesti specifici (sviluppo locale, ambiente di test, produzione) senza modificare il codice sorgente. Essi permettono di sovrascrivere o integrare le configurazioni standard del pom.xml.

Un profilo può essere attivato in diversi modi:

- **Esplicito**: Tramite riga di comando usando il flag -P (es. mvn clean install -Pproduction).
- **Impostazioni di Sistema**: Basato sulla versione del JDK, sul sistema operativo o sulla presenza/assenza di un file specifico.
- **Default**: Dichiarando \<activeByDefault>true</activeByDefault> nella configurazione del profilo.

## Plugin e Mojo

I **plugin** sono la funzionalità centrale di Maven che consentono il riutilizzo della logica di build comune tra più progetti. Questo avviene eseguendo un'**azione** (ad esempio, creare un file WAR o compilare i test unitari) nel contesto del POM.
Il comportamento dei plugin può essere personalizzato tramite un set di parametri unici che vengono esposti nella descrizione di ciascun **goal** del plugin (o **Mojo**).

Un **Mojo** è un goal in Maven, e i plugin consistono in uno o più goal (Mojos).
I Mojos possono essere definiti come classi Java annotate. Un Mojo specifica i metadati su un goal: il nome del goal, a quale fase del ciclo di vita appartiene, e i parametri che si aspetta.

I goal dei plugin sono legati a fasi specifiche del ciclo di vita.

## Archetipi

Gli **archetipi** in Maven sono modelli predefiniti utilizzati per creare nuovi progetti cioè è un template che fornisce una struttura base per un progetto, compreso il file pom.xml, la struttura delle directory, e talvolta anche codice di esempio. Gli archetipi semplificano la creazione di nuovi progetti, standardizzando la configurazione iniziale e riducendo il tempo necessario per configurare un nuovo progetto Maven.

Quando crei un progetto utilizzando un archetipo, Maven esegue una serie di operazioni:

1. Creazione di una struttura di directory predefinita: Ogni archetipo contiene una struttura di directory predefinita
2. Generazione di un pom.xml di base: Ogni archetipo fornisce un file pom.xml preconfigurato che definisce le dipendenze, i plugin, e le configurazioni di base per il progetto.
3. Codice di esempio (facoltativo): Alcuni archetipi possono includere codice di esempio per un tipo di applicazione specifico.

mvn archetype:generate -DgroupId=com.example -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

- -DgroupId=com.example definisce l'ID del gruppo del progetto.
- -DartifactId=my-app definisce l'ID dell'artefatto (nome del progetto).
- -DarchetypeArtifactId=maven-archetype-quickstart specifica l'archetipo da usare (in questo caso, un archetipo di base per un'applicazione Java).
- -DinteractiveMode=false evita di dover rispondere a delle domande durante la creazione del progetto.

## Dipendenze

Le **dipendenze** sono librerie o altri progetti di cui il tuo progetto ha bisogno per essere compilato e funzionare correttamente. Maven gestisce le dipendenze in modo centralizzato, scaricando automaticamente le librerie richieste da repository remoti o locali.

Le dipendenze in Maven sono definite nel file pom.xml del progetto, utilizzando l'elemento **\<dependencies>**. Ogni dipendenza è identificata da tre informazioni principali:

1. **groupId**: Identifica il gruppo o l'organizzazione che mantiene la libreria.
2. **artifactId**: Il nome della libreria o dell'artefatto.
3. **version**: La versione specifica della libreria.
4. Dipendenze di compilazione (Compile Dependencies):

Sono necessarie per compilare il codice. Queste dipendenze vengono incluse automaticamente in fase di compilazione e in fase di esecuzione. Sono definite nel blocco \<dependencies> nel pom.xml.

### Dipendenze di test (Test Dependencies)

Sono necessarie solo durante la fase di test e non vengono incluse nel pacchetto finale. Queste dipendenze sono definite utilizzando l'elemento \<scope>test</scope>.

### Dipendenze runtime (Runtime Dependencies)

Sono necessarie per l'esecuzione del programma, ma non per la compilazione. Vengono incluse solo in fase di esecuzione.

### Dipendenze di sistema (System Dependencies)

Sono librerie che devono essere fornite manualmente, ad esempio librerie che non sono disponibili in un repository pubblico. Queste dipendenze sono identificate con un percorso locale.

### Dipendenze di provided (Provided Dependencies)

Sono necessarie solo durante la fase di compilazione e test, ma sono fornite in fase di esecuzione dall'ambiente in cui il progetto verrà eseguito.

### Scope delle dipendenze

Lo **scope** di una dipendenza definisce in quale fase del ciclo di vita del progetto la dipendenza è necessaria.

1. compile: È il default e indica che la dipendenza è necessaria per la compilazione, il test, l'esecuzione e la distribuzione.
2. provided: Indica che la dipendenza è necessaria per la compilazione e i test, ma sarà fornita dal contenitore o dall'ambiente di esecuzione (ad esempio, un server web come Tomcat).
3. runtime: La dipendenza è necessaria solo durante l'esecuzione del programma, ma non durante la compilazione.
4. test: La dipendenza è necessaria solo durante la fase di test e non per la compilazione o l'esecuzione.
5. system: La dipendenza è necessaria per la compilazione e l'esecuzione, ma deve essere fornita manualmente con un percorso specificato nel pom.xml.

Le dipendenze in Maven possono essere **transitive**, cioè che se il tuo progetto dipende da una libreria A e la libreria A dipende a sua volta da una libreria B, Maven gestirà automaticamente anche la dipendenza di B. Questo ti evita di dover gestire manualmente ogni dipendenza indiretta.

## Multi-module projects

Un **progetto multi-modulo** è un progetto che contiene più moduli (o sotto-progetti) gestiti sotto un'unica configurazione. Ogni modulo può essere un progetto Maven indipendente, ma sono tutti gestiti insieme in modo centralizzato da un **progetto padre**.

Maven esegue la build dei moduli nell'ordine in cui sono elencati nel pom.xml del progetto padre. Ogni modulo dipende dalle configurazioni definite nel progetto padre, ma può anche avere configurazioni specifiche se necessario.

In progetti complessi, si usa \<dependencyManagement> nel POM padre per definire le versioni delle librerie in un unico punto. I moduli figli erediteranno la versione senza doverla specificare, evitando conflitti di versione (il cosiddetto "Dependency Hell").

### Ereditarietà vs Aggregazione

- **Ereditarietà** (Parent POM): I moduli figli ereditano configurazioni e dipendenze dal padre.
- **Aggregazione** (Multi-module): Un progetto "contenitore" che permette di compilare più moduli con un unico comando.

## Maven Properties

Permettono di centralizzare valori costanti (es. versioni delle librerie o encoding dei file):

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <spring.version>6.1.0</spring.version>
</properties>
```

## Il file `settings.xml`

Situato in `~/.m2/settings.xml`, non riguarda il progetto ma l'utente/ambiente. Contiene:

-Credenziali per i repository remoti (\<servers>).
-Configurazione di Proxy aziendali.
-Mirror dei repository centrali.

## Guida ai Comandi Utili (CLI)

| Comando                         | Descrizione                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------- |
| `mvn clean`                     | Rimuove la directory `target`. Utile per forzare una ricompilazione totale.  |
| `mvn clean install`             | Pulisce e installa il pacchetto nel repository locale.                       |
| `mvn clean install -U`          | Pulisce, installa e forza l'aggiornamento delle dipendenze SNAPSHOT.         |
| `mvn compile`                   | Compila solo il codice sorgente in `src/main/java`.                          |
| `mvn test`                      | Esegue i test unitari definiti nel progetto.                                 |
| `mvn package`                   | Compila e crea l'archivio (JAR/WAR) nella cartella `target`.                 |
| `mvn install`                   | Copia il pacchetto nel repository locale per usarlo in altri progetti.       |
| `mvn deploy`                    | Carica l'artefatto finale in un repository remoto (es. Nexus o Artifactory). |
| `mvn dependency:tree`           | Mostra l'albero gerarchico di tutte le dipendenze.                           |
| `mvn help:effective-pom`        | Mostra il POM finale con parent e profili attivi.                            |
| `mvn archetype:generate`        | Avvia il wizard per creare un nuovo progetto da template.                    |
| `mvn archetype:catalog`         | Mostra la lista di tutti gli archetipi disponibili.                          |
| `mvn clean install -DskipTests` | Build completa saltando l'esecuzione dei test.                               |
| `mvn release:prepare`           | Prepara il rilascio di una nuova versione del progetto.                      |
| `mvn release:perform`           | Esegue il rilascio effettivo del progetto.                                   |
| `maven-release-plugin`          | Plugin Maven per automatizzare il processo di rilascio.                      |
