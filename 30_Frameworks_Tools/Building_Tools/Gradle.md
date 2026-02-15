# Gradle

Parent: [[Building_Tools_MOC]]

![gradle_logo](assets/gradle_logo.png)

**Gradle** è un sistema di automazione della build open source che combina la potenza e la flessibilità di Ant con la gestione delle dipendenze e le convenzioni di Maven. A differenza di Maven (basato su XML), Gradle utilizza un DSL (Domain Specific Language) basato su Groovy o Kotlin, permettendo di scrivere logica di build come vero e proprio codice.

È lo standard de facto per lo sviluppo Android.

> Apache Ant (acronimo di Another Neat Tool) è stato il primo vero standard per l'automazione della build nel mondo Java, rilasciato nel 2000. A differenza dei suoi successori, Ant è nato come strumento puramente imperativo: non impone convenzioni su come il progetto debba essere strutturato, ma richiede allo sviluppatore di descrivere esplicitamente ogni singolo passaggio del processo. Questo approccio offre grande flessibilità, ma può portare a build scripts complessi e difficili da mantenere, soprattutto in progetti di grandi dimensioni. Ant non ha un sistema di gestione delle dipendenze integrato, il che significa che gli sviluppatori devono gestire manualmente le librerie esterne, spesso scaricandole e includendole nel progetto senza un meccanismo centralizzato.

## Architettura e Struttura

Gradle adotta la struttura di directory standard di Maven, ma i file di configurazione sono diversi:

- **build.gradle** (o build.gradle.kts): Lo script di build principale (equivalente al pom.xml).
- **settings.gradle**: Definisce la struttura del progetto e quali moduli includere (multi-module).
- **gradle.properties**: Variabili di configurazione e proprietà della JVM.
- **gradlew** (**Gradle Wrapper**): Uno script shell che scarica e utilizza una versione specifica di Gradle, garantendo che tutti nel team usino la stessa versione.

### Il Gradle Wrapper

Il Wrapper è uno script (`gradlew`) che invoca una versione dichiarata di Gradle, scaricandola se necessario.
Garantisce che ogni sviluppatore e il server di CI (es. Jenkins/GitHub Actions) usino l'esatta stessa versione di Gradle, eliminando problemi di compatibilità.

Per aggiornare il progetto a una nuova versione di Gradle:

```bash
./gradlew wrapper --gradle-version 8.5 --distribution-type all
```

### Script vs Dichiarazione

Mentre Maven è dichiarativo ("Descrivo cosa voglio"), Gradle è imperativo/dichiarativo ("Descrivo cosa voglio, ma posso anche scrivere codice per dire come ottenerlo").

## Gestione delle Dipendenze

Gradle sostituisce il concetto di "Scope" di Maven con le Configurations. Questo offre un controllo più granulare sulla transitività e sulla compilazione.

| Maven Scope | Gradle Configuration | Descrizione                                                                     |
| ----------- | -------------------- | ------------------------------------------------------------------------------- |
| compile     | implementation       | Dipendenza interna, non esposta transitivamente. Migliora la velocità di build. |
| (N/A)       | api                  | Espone la dipendenza transitivamente (plugin `java-library`).                   |
| provided    | compileOnly          | Necessaria per compilare ma non inclusa nel pacchetto finale.                   |
| runtime     | runtimeOnly          | Necessaria solo in esecuzione.                                                  |
| test        | testImplementation   | Disponibile solo nei test.                                                      |

### Version Catalogs (TOML)

Introdotto stabilmente in Gradle 7.4, il Version Catalog è il metodo moderno per centralizzare le dipendenze. Invece di hardcodare versioni nei vari `build.gradle`, si utilizza un file TOML situato in `gradle/libs.versions.toml`.

Il file è diviso in sezioni:

1. `[versions]` - Definisce le versioni in un unico posto.
2. `[libraries]` - Mappa i nomi delle librerie alle coordinate Maven, con riferimento alle versioni.
   - Esteso: `retrofit-core = { group = "...", name = "...", version.ref = "..." }`
   - Compatto: `retrofit-core = { module = "group:name", version.ref = "..." }`
     Gradle trasforma i nomi separati da trattini in notazione punto (**type-safe**). `retrofit-core` nel TOML diventa `libs.retrofit.core` nel file `build.gradle`.
3. `[plugins]` - Definisce i plugin con le loro versioni, anch'essi referenziati da `[versions]`.
4. `[bundles]` - Permette di raggruppare più librerie sotto un unico nome per importarle insieme.
   Nel `build.gradle`, invece di aggiungere 5 righe per ogni libreria di test, ne aggiungi una sola

   ```gradle
   // Senza Bundle:

   testImplementation(libs.junit)
   testImplementation(libs.mockito)
   testImplementation(libs.assertj)

   // Con Bundle:

   testImplementation(libs.bundles.testing)
   ```

#### Struttura del file `libs.versions.toml`

```toml
[versions]
springBoot = "3.2.0"
junit = "5.10.0"
lombok = "1.18.30"

[libraries]
# Definizione singola libreria
lombok = { group = "org.projectlombok", name = "lombok", version.ref = "lombok" }

# Riferimento alla versione definita sopra
junit-jupiter = { module = "org.junit.jupiter:junit-jupiter", version.ref = "junit" }

[plugins]
spring-boot = { id = "org.springframework.boot", version.ref = "springBoot" }

[bundles]
# Raggruppamento di librerie per importarle in un colpo solo
testing = ["junit-jupiter"]
```

Vantaggi:

- **Centralizzazione**: Un solo posto dove aggiornare le versioni per progetti multi-modulo.
- **Type-Safety**: L'IDE suggerisce i nomi delle librerie (libs.nomeLibreria).
- **Standardizzazione**: Formato leggibile e condivisibile tra team diversi.

## Build Lifecycle e Task Graph

Il cuore di Gradle è il **DAG** (**Directed Acyclic Graph**) dei Task.
Il ciclo di vita ha tre fasi distinte:

1. **Initialization**: Gradle determina quali progetti partecipano alla build (legge settings.gradle).
2. **Configuration**: Esegue gli script di build di tutti i progetti, crea il grafo dei task e popola le proprietà. Attenzione: Non mettere codice pesante qui, verrà eseguito ad ogni comando!
3. **Execution**: Esegue i task richiesti (es. build, test) nell'ordine determinato dal grafo.

## Il file `gradle.properties`

Equivalente parziale del `settings.xml` di Maven per le proprietà. Si usa per configurare l'ambiente di build:

```xml
# Aumenta la memoria per la build (Performance)
org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
# Abilita la cache e il demone per velocità
org.gradle.caching=true
org.gradle.daemon=true
# Variabili custom
myVersion=1.0.0
```

## Repository e Credenziali

Definiti nel blocco repositories del `build.gradle` (o globalmente in un init script):

```gradle
repositories {
    mavenCentral()
    maven {
        url "[https://repo.mycompany.com/maven2](https://repo.mycompany.com/maven2)"
        credentials {
            username = property('repoUser')
            password = property('repoPassword')
        }
    }
}
```

## Multi-module projects

Un progetto multi-modulo è definito da un unico file `settings.gradle` (o `.kts`) alla radice, che dichiara quali directory fanno parte della build.

```plaintext
root-project/
├── settings.gradle.kts    // Definisce la topologia
├── build.gradle.kts       // Configurazione condivisa (opzionale)
├── gradle.properties      // Proprietà globali
├── core/                  // Modulo libreria
│   └── build.gradle.kts
├── api/                   // Modulo interfacce
│   └── build.gradle.kts
└── app/                   // Modulo applicazione (eseguibile)
    └── build.gradle.kts
```

Nel file `settings.gradle` (o `settings.gradle.kts`) si dichiarano i moduli:

```gradle
rootProject.name = "my-enterprise-app"

include("core")
include("api")
include("app")

// Strutture nidificate (es. features/login)
include("features:login")
```

Nel modulo `web/build.gradle` si importa il modulo core:

```gradle
dependencies {
    implementation project(':core')
}
```

### Cross-Configuration

Esistono due approcci principali per applicare configurazioni comuni a tutti i moduli (**Cross-Configuration**), che sono:

1. `ubprojects / allprojects` Nel `build.gradle.kts` del progetto root, si inietta la configurazione nei figli.

   ```gradle
   // root/build.gradle.kts

   // Applica a TUTTI i progetti (root + figli)
   allprojects {
       group = "com.azienda"
       version = "1.0.0"
   }

   // Applica solo ai figli (esclusa la root)
   subprojects {
       apply(plugin = "java-library")

       repositories {
           mavenCentral()
       }

       dependencies {
           testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
       }
   }
   ```

   Crea Accoppiamento. Modificare la root invalida la cache di tutti i figli. Inoltre, rende la configurazione meno leggibile nei singoli moduli.

2. **Convention Plugins (buildSrc)** con il quale si crea un **Convention Plugins** all’interno della directory `buildSrc`. Questo permette di definire logica di configurazione in codice Kotlin o Groovy, mantenendo i singoli `build.gradle` puliti e focalizzati sulle dipendenze specifiche del modulo.
   1. Creare `buildSrc/src/main/kotlin/my-java-conventions.gradle.kts`.
   2. Definire lì la logica comune.
   3. Applicare il plugin nei singoli moduli: `plugins { id("my-java-conventions") }`.
      Questo favorisce la Composizione sull'Ereditarietà, riduce l’accoppiamento e migliora la manutenibilità.

Un modulo può dipendere da un altro usando la sintassi `project()`.

Nel file `app/build.gradle.kts`:

```gradle
dependencies {
    // Dipendenza diretta da un altro modulo
    implementation(project(":core"))

    // Dipendenza da un modulo nidificato
    implementation(project(":features:login"))
}
```

In un progetto multi-modulo, Gradle costruisce il **Task Graph**.

Se esegui `./gradlew :app:build:` Gradle vede che `:app` dipende da `:core`. Verifica se `:core` è aggiornato (UP-TO-DATE).

Se necessario, ricompila `:core` prima di `:app`.

## Comandi (CLI)

È buona norma usare sempre il Wrapper (`./gradlew` su Linux/Mac, `gradlew.bat` su Windows).

| Comando                            | Descrizione                            |
| ---------------------------------- | -------------------------------------- |
| `./gradlew build`                  | Compila ed esegue i test.              |
| `./gradlew clean`                  | Cancella la directory `build`.         |
| `./gradlew test`                   | Esegue i test.                         |
| `./gradlew dependencies`           | Mostra l’albero delle dipendenze.      |
| `./gradlew tasks`                  | Elenca i task disponibili.             |
| `./gradlew assemble`               | Compila senza eseguire i test.         |
| `./gradlew publish`                | Pubblica l’artefatto su un repository. |
| `./gradlew --refresh-dependencies` | Forza il download delle dipendenze.    |
