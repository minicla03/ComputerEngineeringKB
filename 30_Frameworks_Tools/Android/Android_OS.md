# Android_OS

Android è un sistema operativo sviluppato da Google basato su Linux e progettato per dispositivi mobile è un sistema operativo open source . Quindi il suo codice sorgente è pubblico e può essere modificato da sviluppatori e produttori di hardware per creare la propria versione di Android e adattarlo a loro dispositivo, Il problema di questo è che ciò porta a una frammentazione eccessiva delle versioni e questo causa problemi quando dobbiamo sviluppare delle applicazioni, perché dobbiamo individuare il numero di dispositivi compatibili con la versione che dovremo sviluppare.
Android cerca di risolvere il problema di compatibilità creando degli appositi librerie che si possono utilizzare con andiamo a sviluppare il codice

Google gestisce il rilascio delle nuove versioni di Android sia per i propri dispositivi, la cui distribuzione avviene in maniera abbastanza rapida sia per gli altri dispositivi di altri produttori. Il sistema operativo di questi seguire. Deve seguire un **processo di qualifica** da parte di Google. Questo vuol dire che ogni qualvolta che Google rilascia un aggiornamento ogni produttore deve adattarlo al proprio hardware del dispositivo e questo richiede molto tempo perché modificano anche l’interfaccia. Una volta che hanno effettuato queste modifiche la versione deve essere approvata da Google per garantire che soddisfi standard di qualità compatibilità e sicurezza se si superano questi test al loro i produttori potranno rilasciare il loro aggiornamento per i loro dispositivi.

Il sistema Android è interamente sviluppato sopra al kernel Linux. Il motivo di questa scelta è dovuto al fatto che non sarebbero mai stati in grado di sviluppare un sistema completamente funzionante in tempi rapidi per poter entrare nel mercato. Linux era già un sistema operativo pienamente funzionante sotto ogni aspetto e che funzionava in modo molto efficiente e quindi l’idea di Google fu quello di estendere il sistema operativo Linux per adattarlo ai dispositivi mobile.

### **Linux Kernel**

Questo livello fornisce i servizi di gestione dell'hardware. A questo livello, viene applicato uno schema di protezione per limitare l'accesso ai dati e alle risorse e consentirlo solo ai processi che posseggono l'adeguato livello di autorizzazione. Vi sono i moduli per la gestione della memoria, dei processi, del sistema di archiviazione e della comunicazione sulla rete. Vi sono i driver per la gestione dell'hardware in dotazione al dispositivo, ad esempio la memoria ausiliaria, la radio, la fotocamera. Oltre ai servizi offerti dal nucleo del sistema operativo, il kernel di Android include alcuni componenti particolari, quali ad esempio il sistema di risparmio energetico, il sistema di gestione e condivisione della memoria, un meccanismo di comunicazione tra processi chiamato **binder**, che permette ai processi di condividere dati e servizi.

![Stack Android OS](assets/stack_android_os.png)

### **Hardware Abstraction Level**

Sopra al kernel troviamo HAL che fornisce interfacce standard per esporre le funzionalità hardware del dispositivo al framework API di livello superiore. HAL è formato da più moduli, ognuno dei quali implementa un’interfaccia per un tipo di componente hardware Linux . quando il framework fa una chiamata per accedere all’hardware del dispositivo Android carica il modulo di libreria di quella componente. I moduli sono scritti dal produttore.

### **Android RunTime**

L’Android Runtime è composto dalla macchina virtuale **ART** (che ha sostituito Dalvik) e dalle librerie principali del sistema. ART è un ambiente di esecuzione in cui ogni app viene eseguita nel proprio processo, con una propria istanza di ART.

ART traduce il codice scritto in Java o Kotlin in bytecode, che viene poi convertito in codice nativo comprensibile dal processore del dispositivo. Utilizza principalmente un approccio di compilazione **Ahead-of-Time (AOT)**: quando si installa una nuova app, questa viene compilata in codice nativo già durante la fase di installazione, migliorando così le performance in fase di esecuzione.

Inoltre, ART può usare la modalità **Just-In-Time (JIT)** per compilare dinamicamente solo alcune parti del codice durante l’esecuzione dell’app, migliorando la reattività e riducendo i tempi di compilazione iniziale.

### **Native C/C++ Library NDK**

Sempre sopra ad HAL troviamo le NDK strumenti per sviluppare app in C/C++. Sono utili per implementare funzionalità che richiedono altre performance o se dobbiamo implementare parte di codice che devono comunicare direttamente con l’hardware.

### **Java API Framework**

Sopra ai livelli di Android Runtime e HAL troviamo il **Java API Framework**, un insieme di librerie, classi e interfacce scritte in Java/Kotlin che permettono di interagire facilmente con le funzionalità hardware e software del dispositivo.

Questo livello è progettato per semplificare lo sviluppo delle app, fornendo un accesso ad alto livello alle componenti del sistema operativo Android

Le API mettono a disposizione implementazioni predefinite delle componenti fondamentali del sistema, che possono essere estese e personalizzate dagli sviluppatori per costruire le funzionalità specifiche dell'app.

### **Applicazioni**

Sopra questo livello troviamo le applicazioni dell’utente.

## **Android SDK**

L’**android software development kit ASDK** è un set di librerie e strumenti per sviluppare un app android. I tool si dividono in;

- SDK platform, tools platform dependent. Una nuova versione di queste è rilasciata ad ogni versione di android e include librerie, codici sorgenti ecc
- SDK tools che sono platform indipendent. Sono strumenti usati per sviluppare , farete bugno a disposizione un emulatore per simulate un dispositivo mobile. Ha un android Debug Brigde che permette di comunicare con il dispositivo per eseguire operazioni varie per fare testing e debug.
