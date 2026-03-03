# UI Testing (Espresso)

**ESPRESSO**

Il UI testing si concentra sul test degli aspetti dell'interfaccia utente e delle interazioni con gli utenti.

**Espresso** lavora con il test runner AndroidJUnitRunner e richiede instrumentation.

I test Espresso si basano sulla simulazione delle azioni che un utente potrebbe compiere: **trovare una view**, **eseguire un'azione** (es. clic) e **verificare il risultato** (asserzione sullo stato della view).

![A logo showing a clear drinking glass with water, mint leaves and two black straws, above the lowercase word "mockito" (the "mock" in green and "ito" in black) with a faint reflection beneath the text.](./Android_images/image_047.png)I test Espresso vengono eseguiti su dispositivi Android reali o emulatori. Richiedono l'instrumentazione e funzionano con il test runner AndroidJUnitRunner.

- L'app restituisce l'output UI corretto in risposta a una sequenza di azioni dell'utente.
- I controlli di navigazione e input dell'app aprono le Activity, le View e i campi corretti.
- L'app risponde correttamente con dipendenze "mockate" (false) o può lavorare con metodi backend "stubbed out" (simulati).

Un vantaggio fondamentale di Espresso è l'accesso alle informazioni di strumentazione, come il contesto dell'app. Sincronizza automaticamente le azioni di test con l'UI dell'app, rilevando quando il thread principale è inattivo. Ciò permette ai test di essere eseguiti al momento opportuno, migliorando l'affidabilità ed evitando la necessità di workaround basati sul tempo, come i ritardi (sleep) nel codice di test.

La scrittura dei test Espresso si basa su ciò che farebbe un utente. I passaggi fondamentali sono:

# 1. Trovare una vista (Match a view): Individuare l'elemento UI con cui interagire, spesso usando il metodo onView().

# 2. Eseguire un'azione (Perform an action): Interagire con la vista trovata, ad esempio cliccando (click()).

# 3. Asserire e verificare il risultato (Assert and verify the result): Controllare lo stato della vista o l'output per vedere se corrisponde allo stato o al comportamento atteso.

Espresso ha una sintassi fluida e un paradigma funzionale. Il framework Hamcrest è comunemente usato con Espresso per le asserzioni. Permette di creare **matcher** personalizzati e combinare espressioni per definire regole di corrispondenza in modo dichiarativo. Questo porta a messaggi di errore più utili rispetto alle semplici asserzioni booleane.
