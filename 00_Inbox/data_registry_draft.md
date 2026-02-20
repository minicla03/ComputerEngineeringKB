Il Concetto di Data Registry

Parent: [[DVC]], [[Machine_Learning_MOC]]

Cos'è un Data Registry?

In ambito software, siamo abituati a utilizzare i gestori di pacchetti (come Maven Central per Java, npm per Node.js o PyPI per Python) per pubblicare, versionare e riutilizzare librerie di codice.

Un Data Registry è l'esatto equivalente di questi sistemi, ma progettato specificamente per dataset, pesi dei modelli di Machine Learning e feature estratte. Funge da catalogo centralizzato e indicizzato dove gli asset di dati vengono pubblicati come se fossero artefatti software.

In assenza di un Data Registry, lo scambio di dati tra team aziendali regredisce spesso all'uso di script non documentati, link a bucket S3 condivisi via chat, o—nel peggiore dei casi—lo scambio di dataset via chiavetta USB.

A cosa serve? (Funzionalità Core)

L'introduzione di un Data Registry in un'architettura dati risolve quattro criticità fondamentali:

1. Single Source of Truth (Singola Fonte di Verità)

Fornisce un punto di accesso unico e autorevole. Se il team di Data Engineering pulisce e normalizza un dataset sulle transazioni dei clienti, lo pubblica nel Registry. Tutti i team di Data Science attingeranno a quella specifica versione certificata, evitando la proliferazione di copie locali divergenti sui vari laptop aziendali.

2. Versionamento e Provenienza (Lineage)

I dati, come il codice, mutano nel tempo. Un Data Registry associa a ogni dataset un identificatore univoco (hash) e una versione semantica. Questo garantisce la riproducibilità: se un modello di fraud detection degrada in produzione, è possibile risalire matematicamente alla versione esatta del dataset su cui è stato addestrato settimane prima.

3. Disaccoppiamento tra Produttori e Consumatori

Permette di separare i cicli di vita dei progetti. Il "Progetto A" (pipeline di pulizia dati) e il "Progetto B" (addestramento del modello) possono esistere in repository completamente separati. Il Progetto B dichiara semplicemente una dipendenza verso un artefatto del Progetto A, scaricandolo dal Registry solo quando necessario.

4. Riduzione della Duplicazione

I moderni Data Registry non duplicano i file fisici per ogni utente che li scarica, ma utilizzano meccanismi di cache (symlink o hardlink). Se dieci progetti importano lo stesso modello linguistico da 40 GB, il disco rigido locale memorizzerà il file una sola volta.

L'Approccio di DVC ai Data Registry

Esistono piattaforme aziendali complesse (e costose) nate appositamente come Data Registry (es. MLflow Model Registry, Pachyderm, Amundsen).

Il colpo di genio di DVC risiede nella sua natura distribuita: non richiede un'infrastruttura separata. Qualsiasi repository Git configurato con DVC diventa automaticamente un Data Registry.

Sfruttando il comando dvc import, DVC legge i metadati da un repository Git remoto e scarica i file pesanti dal cloud storage associato, registrando la dipendenza in un file di lock (dvc.lock). In questo modo, il repository Git aziendale funge sia da gestore del codice sorgente che da sofisticato catalogo per i dati.
