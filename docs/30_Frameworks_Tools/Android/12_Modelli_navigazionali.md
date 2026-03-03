## **MODELLI NAVIGAZIONALI**

![A small light-gray rounded-square icon containing three black chevrons (right-pointing arrows) arranged horizontally and evenly spaced.](./Android_images/image_026.png)Quando progettiamo l'interfaccia grafica e dobbiamo pensare all’UX perché svolto in azioni troppo complesse tutte in una schermata può portare l'utente a compiere errori.

Può essere utile dividere una task complessa in più task semplici e per questo è possibile raggruppare task simili in N schermate diverse in modo che l’utente si focalizzi meglio di una singola parte.

È necessario progettare come l'utente nave di chi e promuovere il **way finding** cioè dare alle persone la possibilità di orientarsi e di muoversi all'interno delle schermate.

La navigazione si era voluta anche a capire le informazioni, cosa può fare, dov'è ora, dove può andare e come tornare indietro.

Per aiutare gli utenti a navigare necessario usare **elementi di segnaletica** per aiutare l'utente a orientarsi.

- Indicatori di avanzamento
- Barre di stato
- Breadsceumbs

La navigazione è un overhead perché richiede tempo e risorse per realizzarle in quanto si potrebbe realizzare tutto in una singola schermata ma il motivo per cui si venne a realizzare è di ridurre il carico cognitivo, lo sforzo mentale è caduta anni fa per elaborare le informazioni. Dobbiamo raggruppare task simili perché troppe task che svolgono operazioni diverse ma anche troppe che ne svolgono simili portano all'utente a compiere errori e lapsus perché secondo le scienze cognitive l'uomo non riesce a concentrarsi più su più di sette oggetti alla volta.

![A small square image with a light gray background showing five short, thick vertical black bars evenly spaced. A single slanted zigzag line connects the tops of the bars, creating a sawtooth/waveform-like shape.](./Android_images/image_027.png)**Fully Connected Navigation** Ogni sezione dell’interfaccia può portare direttamente a qualsiasi altra. Questo tipo di navigazione è utile quando si vuole offrire **massima libertà** all’utente. Tuttavia, c’è un rischio che se tutto è collegato a tutto, può diventare difficile capire dove si è e dove si sta andando. Serve dunque una forte coerenza visiva, una buona architettura dell’informazione e magari qualche aiuto visivo come breadcrumb o menu ben organizzati.

![A simple 3D gray humanoid figure stands on an orange path, scratching its head in a puzzled pose. The path splits into several orange arrows pointing in different directions against a white background, visually representing indecision, choices, or multiple possible directions.](./Android_images/image_028.png)**Multilevel NavigationS**i basa su una struttura gerarchica dei contenuti, dividendolo in categorie

Aiuta l’utente a **orientarsi** e a trovare ciò che cerca seguendo un percorso logico però troppi livelli possono diventare dispersivi, quindi è bene non esagerare con la profondità della struttura.

**Step-by-Step Flows** Utilizzati per guidare l’utente in un processo lineare, come una registrazione, un acquisto online, o la configurazione di un profilo. Semplifica l’interazione perché ogni passo è chiaro, focalizzato, e l’utente sa sempre cosa deve fare. L'importante è rendere visibile il progresso, con indicatori e consentire di tornare indietro senza perdere i dati inseriti.

![A schematic labeled "The fully connected model" showing six rectangular nodes (one at the top is shaded darker) arranged roughly in a hexagon. Directed arrows connect every pair of nodes (including bidirectional arrows on adjacent nodes and crisscross/star-shaped arrows between nonadjacent nodes), illustrating a fully connected directed network.](./Android_images/image_029.png)

![A grayscale diagram of a multilevel navigation hierarchy: a single dark top node centered at the top connects horizontally to four lighter second-level nodes. Each second-level node has one or more subordinate nodes stacked beneath it with arrows showing downward navigation (one column has three levels). Caption reads "Figure 3-3. Multilevel navigation."](./Android_images/image_030.png)**Pyramidal Model** SI parte da un’informazione generale e consente all’utente di esplorare via via contenuti sempre più specifici. Funziona bene quando si vuole **gestire l’attenzione** dell’utente e accompagnarlo in una lettura a livelli, senza sommergerlo subito di dettagli.

![- Horizontal row of five rounded rectangles (four light gray, the rightmost one dark gray). - Solid right-pointing arrows connect each rectangle to the next, indicating forward progression. - Dashed (dotted) left-pointing arrows under the solid arrows show return/review flows to earlier steps. - Caption below reads: "Figure 3–4. Step-by-step flows."](./Android_images/image_031.png)**Deep Link** A volte non si parte dalla cima ma ci si ritrova direttamente “all’interno” dell’app, grazie a un **deep link**, cioè un collegamento diretto a una pagina interna. Devono essere progettati con cura, perché l’utente che ci arriva potrebbe **non avere il contesto**: è quindi importante che la pagina sia autonoma, comprensibile da sola.

![A simple diagram labeled "Figure 3–5. Pyramid": - One dark rectangle at the top (a single apex node). - Five lighter rectangles in a horizontal row beneath it (a lower tier). - Single-headed arrows from the top rectangle pointing down to each of the five lower rectangles (one-to-many/top-down relationships). - Double-headed arrows between each adjacent pair of lower rectangles (peer-to-peer lateral connections).](./Android_images/image_032.png)**Clear Entry Point** Cioè una porta d’ingresso ben visibile e comprensibile per l’utente. Appena apre l’app o il sito, l’utente deve capire cosa può fare, dove può andare e quali sono le opzioni principali.Questo vale soprattutto per esperienze nuove o complesse, dove una schermata iniziale troppo carica o confusa rischia di scoraggiare. Meglio semplificare, dare una direzione e lasciare che il resto venga scoperto poco alla volta.

**Hub and Spoke** L’utente parte da un **hub** e da lì può accedere a diverse **spoke**, sezioni o attività isolate. Una volta completata un’attività, torna all’hub per decidere cosa fare dopo.

Questo approccio è utile quando si vuole **mantenere un senso di controllo** e di orientamento.
