# 🧠 Engineering Knowledge Base

Benvenuto nella tua **Knowledge Base (KB)** tecnica. Questo repository è un ecosistema interconnesso progettato per ridurre il debito tecnico mentale e centralizzare tutto ciò che impari nel mondo dell'informatica, della programmazione e dei sistemi.

Basato sulla metodologia **Zettelkasten** e implementato tramite **Foam** in Visual Studio Code.

---

## 📂 Architettura della Conoscenza

La struttura segue una tassonomia numerica per garantire un ordine logico e gerarchico:

```plaintext
EngineeringKB/
├── 00_Inbox/               # Note rapide e bozze da elaborare.
├── 10_Theory/              # Fondamenta: Algoritmi, Strutture Dati, OS, Reti.
├── 20_Languages/           # Sintassi core e Standard Library (Python, Rust, C++).
├── 30_Frameworks_Tools/    # Tool specifici (Android, React, Spring).
├── 40_Design_Patterns/     # Architetture, SOLID, Clean Code.
├── 50_Project_Journal/     # Log delle decisioni tecniche e post-mortem di progetti.
├── 60_Infrastructure/      # Cloud (AWS, GCP), Networking, Sicurezza.
├── 70_DevOps_CICD/         # Pipeline, Docker, Kubernetes, IaC.
└── 99_Meta/                # Template, configurazioni e file di sistema.
```

---

## 🛠️ Comandi di Automazione (CLI)

Per mantenere l'ordine senza sforzo, utilizza i seguenti alias personalizzati dal terminale:

### 1. `new-kb`
Avvia il wizard interattivo per espandere la tua conoscenza.
* **Funzioni:** Crea nuove Macro-Aree (cartelle padre), nuovi Moduli (cartelle figlie) e genera automaticamente le Note Atomiche con i relativi Indici (MOC).
* **Utilizzo:** Digita `new-kb` e segui le istruzioni a schermo.

### 2. `kb-sync`
Sincronizza istantaneamente la tua base di conoscenza con il cloud.
* **Funzioni:** Esegue `git add`, `git commit` (con messaggio automatico o personalizzato) e `git push` in un'unica operazione.
* **Utilizzo:** * `kb-sync` (per un backup rapido con timestamp).
    * `kb-sync "Aggiunti appunti su K8s"` (per un commit descrittivo).

---

## 🚀 Workflow e Best Practices

* **Note Atomiche:** Ogni nota deve trattare un solo concetto. Se è troppo lunga, dividila (**Atomic Notes**).
* **Wiki-Links:** Collega le note tra loro usando la sintassi `[[Nome_Nota]]`. Se una nota non esiste, Foam la creerà per te.
* **MOC (Map of Content):** Ogni modulo ha un file `_MOC.md` che funge da indice. Usalo per avere una visione d'insieme.
* **Assets:** Inserisci sempre le immagini e i diagrammi nella sottocartella `/assets` specifica del modulo per mantenere i path relativi puliti.

---

## 🔧 Stack Tecnologico

| Componente | Strumento |
| :--- | :--- |
| **Editor** | Visual Studio Code |
| **Estensioni Core** | Foam, Mermaid Support, Markdown All in One |
| **Versionamento** | Git (GitHub come storage remoto) |
| **Automazione** | Python 3.10+ |


## 📊 Statistiche KB
