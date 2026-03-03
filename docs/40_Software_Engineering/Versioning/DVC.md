# DVC

Parent: [[Versioning_MOC]]

![dvc_logo](./assets/dvc_logo.png)

DVC (Data Version Control) è uno strumento open-source progettato per estendere le funzionalità di Git, permettendo di tracciare e gestire grandi file di dati, modelli di Machine Learning e pipeline di elaborazione.
Git è stato concepito per tracciare file di testo, non dati binari massivi. Tentare di inviare un dataset da 10 GB su GitHub non solo saturerà la banda, ma risulterà in un blocco del repository.

DVC risolve questo problema introducendo un livello di astrazione: traccia i metadati dei file pesanti tramite Git, ma archivia il contenuto effettivo su un cloud storage a scelta (S3, GCP, Azure, NAS aziendale), mantenendo il repository leggero e flessibile.

È diventato lo standard de facto per le pipeline di Machine Learning (MLOps) e per il data engineering.

## Architettura e Principi di Funzionamento

DVC non sostituisce Git, ma vi si appoggia in totale simbiosi. Il principio architetturale di base è la separazione tra puntatore e dato reale:

> Puntatori leggeri (.dvc): Quando si aggiunge un file pesante a DVC, lo strumento calcola un hash del file e genera un piccolo file di testo (es. `dataset.csv.dvc`). Questo file contiene l'hash e le dimensioni del dato.

Il cuore pulsante di DVC è la sua Cache Locale (situata in `.dvc/cache`). Per evitare di duplicare inutilmente i dati sul disco quando si esegue il versionamento, DVC non copia semplicemente i file, ma utilizza funzionalità avanzate del file system.

Il file `.dvc` viene aggiunto al controllo di versione di Git, mentre il file pesante originale viene automaticamente inserito nel `.gitignore`.

## Storage Remoto

I dati reali salvati nella cache locale gestita da DVC verranno successivamente sincronizzati ("pushati") su uno storage remoto configurabile (AWS S3, Google Cloud Storage, Azure Blob, o un semplice server SSH/NFS).

Questa architettura garantisce che il repository Git rimanga leggero, pur mantenendo un legame indissolubile e versionato con i dati esatti utilizzati per una specifica versione del codice.

## Workflow Operativo Standard

Il flusso di lavoro con DVC è deliberatamente identico a quello di Git per minimizzare la curva di apprendimento.

### Fase 1: Inizializzazione e Configurazione del Remoto

```bash
# Inizializza DVC in un repository Git esistente
dvc init

# Configura uno storage remoto (es. un bucket S3)
dvc remote add -d myremote s3://my-bucket/dvcstore
```

(Nota: la configurazione del remoto viene salvata nel file `.dvc/config`, che va committato in Git).

### Fase 2: Tracciamento dei Dati

```bash
# Aggiunge un dataset pesante a DVC
dvc add data/dataset.csv

# DVC crea data/dataset.csv.dvc e aggiunge dataset.csv al .gitignore
# Ora aggiungiamo il puntatore a Git
git add data/dataset.csv.dvc data/.gitignore
git commit -m "Aggiunto dataset V1"
```

Quando si esegue `dvc add dataset.csv`, DVC sposta il file reale nella sua cache e crea un collegamento nella tua working directory. Le strategie supportate sono:

- **Copy** (Default su Windows): Copia fisica del file. Sicura, ma spreca spazio su disco.
- **Symlink / Hardlink** (Raccomandato): DVC crea un collegamento fisico al file in cache. Le dimensioni su disco restano inalterate.
- **Reflink** (Copy-on-Write): Il massimo dell'efficienza (supportato da file system come Btrfs, XFS o APFS su macOS). Il file appare come indipendente, ma occupa spazio solo se viene modificato.

per impostazione predefinita, non è necessario scegliere manualmente. DVC implementa una strategia di fallback automatica molto intelligente. Quando si aggiunge un file, DVC tenta di utilizzare i metodi nel seguente ordine di efficienza:

1. reflink (Se il file system lo supporta)
2. hardlink (Se supportato e se cache/workspace sono sullo stesso disco)
3. symlink (Se l'OS lo permette senza privilegi elevati)
4. copy (L'ultima risorsa, sempre supportata)

Se si desidera forzare un comportamento specifico per ottimizzare le risorse o risolvere problemi di compatibilità, è possibile intervenire sulla configurazione.

La configurazione si effettua tramite il comando `dvc config`. È possibile definire una lista di preferenze separate da virgola.

```bash
# Esempio: Forza l'uso di hardlink, se fallisce usa la copia
dvc config cache.type hardlink,copy

# Esempio: Imposta symlink come unica opzione consentita
dvc config cache.type symlink

# Per applicare la configurazione globalmente all'utente (non solo al progetto)
dvc config --global cache.type reflink,copy
```

### Fase 3: Condivisione (Push/Pull)

```bash
# Invia i dati pesanti allo storage remoto (S3, GCS, ecc.)
dvc push

# Invia i puntatori e il codice al repository Git (es. GitHub/GitLab)
git push
```

Quando un altro sviluppatore clona il repository, eseguirà:

```bash
git pull
dvc pull
```

## Automazione e Pipeline (DAG)

Oltre al tracciamento dei dati, DVC integra un sistema per orchestrare e versionare le Data Pipeline. Tramite il file `dvc.yaml`, è possibile definire un Grafo Diretto Aciclico (DAG) composto da diversi stage (es. estrazione, preprocessing, training, valutazione).

### Esempio di stage in dvc.yaml

```yaml
stages:
  train_model:
    cmd: python src/train.py
    deps:
      - data/processed_dataset.csv
      - src/train.py
    params:
      - train.learning_rate
      - train.epochs
    outs:
      - models/model.pkl
    metrics:
      - scores.json:
          cache: false
    plots:
      - evaluation/roc_curve.csv
```

Esecuzione:

```bash
dvc repro
```

Se le dipendenze (`deps`) non sono cambiate dall'ultima esecuzione, DVC salta lo step. A differenza di un semplice Makefile, DVC valuta l'hash di dipendenze (`deps`), output (`outs`) e parametri (`params`) per determinare se uno stage necessiti di essere ricalcolato. Se sono cambiati, esegue il comando (`cmd`) e traccia automaticamente i nuovi.

## Il DVC Data Registry

Oltre al tracciamento interno, DVC trasforma qualsiasi repository Git in un **Data Registry** centralizzato. È possibile condividere dati tra progetti software completamente diversi senza duplicarli fisicamente.

Se il "Progetto A" genera un modello di machine learning, il "Progetto B" può importarlo dinamicamente.

- Nel Progetto B: importa un file tracciato nel Progetto A

```bash
dvc import [https://github.com/my-org/progetto-A](https://github.com/my-org/progetto-A) model/model.pkl
```

DVC scarica il file `model.pkl` dal Progetto A, lo traccia nel Progetto B e registra la dipendenza in un file di lock (`dvc.lock`).

Se il modello in Progetto A viene aggiornato, basta eseguire:

```bash
dvc update model.pkl.dvc
```

Questa operazione garantisce la provenienza dei dati: si ha sempre la certezza crittografica di quale specifica versione del modello stia girando in produzione.

## Gestione degli Esperimenti (Experiment Tracking)

Con le versioni recenti (DVC 2.0+), lo strumento si è evoluto oltre il semplice salvataggio dei file, introducendo il tracciamento degli esperimenti senza l'onere di inquinare la cronologia Git con migliaia di commit inutili.

DVC permette di legare l'esecuzione del codice a un file params.yaml (iperparametri del modello) e a file di metriche (metrics.json).

```yaml
# params.yaml
train:
epochs: 100
learning_rate: 0.01
```

Invece di creare un branch per ogni prova, si utilizza dvc exp.

```bash
# Esegue una variante modificando un parametro "on-the-fly"
dvc exp run --set-param train.learning_rate=0.05


# Mostra una tabella comparativa di tutti gli esperimenti
dvc exp show
```

Una volta trovato l'esperimento ottimale, lo si può "promuovere" a branch ufficiale con dvc exp branch, applicando il rigore del versionamento solo al risultato vincente.

```bash
# Crea un branch Git a partire dall'esperimento selezionato
dvc exp branch <nome-esperimento> <nome-branch>
```

In questo modo si applica il versionamento formale solo al risultato vincente, mantenendo gli altri esperimenti come variazioni temporanee.

## Comandi (CLI)

| Comando                        | Descrizione                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------ |
| `dvc init`                     | Inizializza DVC in un progetto Git. Genera la cartella nascosta `.dvc/`.                         |
| `dvc add <file/dir>`           | Inizia a tracciare un file o una directory. Genera il file `.dvc` associato.                     |
| `dvc push`                     | Invia i file tracciati dalla cache locale allo storage remoto configurato.                       |
| `dvc pull`                     | Scarica i file dallo storage remoto in base ai file `.dvc` presenti nel workspace corrente.      |
| `dvc checkout`                 | Allinea i file di dati effettivi nel workspace alla versione definita nei file `.dvc` attuali.   |
| `dvc remote add <name> <url>`  | Configura un nuovo storage remoto (es. `s3://...`, `gdrive://...`).                              |
| `dvc repro`                    | Riproduce la pipeline definita in `dvc.yaml`, rieseguendo solo gli stage necessari.              |
| `dvc metrics show`             | Mostra le metriche associate al progetto (es. accuratezza di un modello).                        |
| `dvc exp run`                  | Esegue un esperimento isolato senza creare un branch Git.                                        |
| `dvc exp show`                 | Mostra una tabella comparativa degli esperimenti eseguiti.                                       |
| `dvc exp branch`               | Promuove un esperimento a branch Git permanente.                                                 |
| `dvc exp apply`                | Applica nel workspace i risultati di un esperimento selezionato.                                 |
| `dvc exp remove`               | Elimina uno o più esperimenti salvati.                                                           |
| `dvc import <repo-url> <path>` | Importa un file o directory da un altro repository DVC mantenendo il collegamento alla sorgente. |
| `dvc update <file>.dvc`        | Aggiorna un file importato alla versione più recente disponibile nel repository sorgente.        |
| `dvc import-url <url>`         | Importa dati da URL esterni (HTTP, S3, GDrive, ecc.) senza collegamento a repository DVC.        |
