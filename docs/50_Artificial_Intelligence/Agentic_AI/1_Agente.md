# Agente

Parent: [[0_Agentic_AI_MOC]]

Un **agente AI**, differentemente da un LLM, è un sistema **proattivo**, cioè, in grado di prendere decisioni e di agire in completa autonomia, interagendo con l'ambiente per raggiungere degli **obiettivi**.

Gli agenti AI sono progettati per essere **autonomi** e **intelligenti**, in grado di apprendere dall'esperienza, adattarsi a nuove situazioni e migliorare le proprie prestazioni nel tempo. Possono essere utilizzati in una vasta gamma di applicazioni, come assistenti virtuali, robotica, automazione industriale, giochi e molto altro.

Sono basati su algoritmi di AI, e in particolare sul **Reinforcement Learning**, che consente loro di imparare attraverso l'interazione con l'ambiente, ricevendo feedback sotto forma di ricompense o penalità in base alle azioni intraprese. Questo processo di apprendimento permette agli agenti di sviluppare strategie efficaci per raggiungere i loro obiettivi.

Gli agenti AI possono essere classificati in diverse categorie, come:

- **Agenti reattivi**: Rispondono direttamente agli stimoli dell'ambiente senza mantenere una memoria delle esperienze passate.
- **Agenti basati su modelli**: Utilizzano un modello dell'ambiente per prevedere le conseguenze delle loro azioni e prendere decisioni informate.
- **Agenti basati su obiettivi**: Lavorano per raggiungere specifici obiettivi, pianificando le azioni necessarie per raggiungerli.
- **Agenti multi-agente**: Interagiscono con altri agenti, collaborando o competendo per raggiungere i loro obiettivi.

## I Core Componenti di un Agente AI

I core componenti di un agente AI includono:

- **Modello (Brain)**: che rappresenta la conoscenza dell'agente dell'ambiente, e in generale è rappresentato da un LLM, grazie al quale l'agente può comprendere,comunicare e agire con l'ambiente.
- **Tool (Hands)**: che consentono agli agenti di interagire con dati e servizi esterni, ampliando il loro raggio d'azione. Gli strumenti possono assumere varie forme, come estensioni, funzioni e archivi dati.
- **Orchestratore (Nervous system)**: gestisce il modo con cui l'agente elabora le informazioni, esegue il ragionamento e decide la sua azione successiva. Si tratta di un processo ciclico che continua fino al raggiungimento dell'obiettivo o di un punto di arresto da parte dell'agente.

## Come funziona un Agente AI

Le architetture cognitive degli agenti AI sono progettate per consentire loro di apprendere, adattarsi e migliorare le proprie prestazioni nel tempo. Le architetture di questo genere sono spesso ispirate alla struttura e al funzionamento del cervello umano, infatti operano in un **processo ciclico** che permette di raccolgiere informazioni, ragionare e prendere decisioni. Questo ciclo continua fino a quando l'agente non ha raggiunto i suoi obiettivi o ha raggiunto un punto di arresto.

Il livello di orchestrazione è i responsabile della gestione della memoria dell'agente, che consente di mantenere una traccia delle esperienze passate e di utilizzare queste informazioni per informare le decisioni future. La memoria può essere organizzata in diverse forme, come memorie a breve termine, memorie a lungo termine e memorie episodiche, che consentono all'agente di accedere a informazioni rilevanti quando necessario.
La gestione della memoria è ciò che conferisce continuità all'azione:

- **Short-term**: Finestra di contesto della sessione corrente.
- **Long-term**: Database vettoriali o log storici che permettono all'agente di "ricordare" preferenze o fatti da sessioni avvenute giorni prima.

Per potere ragionare e prendere decisioni, l'agente utilizza modelli di conoscenza, logica e algoritmi di apprendimento. Questi modelli consentono all'agente di comprendere il contesto in cui si trova, di prevedere le conseguenze delle sue azioni e di adattare la sua strategia di conseguenza.

I reasoning framework più popolari sono:

- **Reason & Act** (**ReAct**)
- **Chain-of-Thought** (**CoT**)
- **Tree-of-thoughts** (**ToT**)

Queste architetture possono essere suddivise in diverse componenti chiave:

- **Percezione**: L'agente raccoglie informazioni dall'ambiente attraverso sensori o input, come testo, immagini o dati strutturati.
- **Ragionamento**: L'agente elabora le informazioni raccolte, utilizzando modelli di conoscenza, logica e algoritmi di apprendimento per prendere decisioni informate.
- **Apprendimento**: L'agente utilizza tecniche di apprendimento automatico per migliorare le proprie prestazioni nel tempo, adattandosi a nuove situazioni e acquisendo nuove conoscenze.
- **Azione**: L'agente esegue azioni nell'ambiente per raggiungere i suoi obiettivi, interagendo con altri agenti o con l'ambiente stesso.
- **Memoria**: L'agente mantiene una memoria delle esperienze passate, che può essere utilizzata per informare le decisioni future e migliorare le prestazioni nel tempo.
- **Comunicazione**: L'agente può comunicare con altri agenti o con gli esseri umani, scambiando informazioni e collaborando per raggiungere obiettivi comuni.
- **Pianificazione**: L'agente può pianificare le sue azioni future, prevedendo le conseguenze delle sue decisioni e adattando la sua strategia di conseguenza.
- **Controllo**: L'agente monitora e regola le sue azioni per garantire che siano efficaci e coerenti con i suoi obiettivi, apportando modifiche se necessario.

## Tools

I tools peremttono di estendere le capacità di un LLM che si limita al processamento del linguaggio naturale, consentendo di interagire con dati e servizi esterni. Ci sono tre tipi principali di tools:

- **Estensioni**: questi, fungono da bridge standard tra l'agente e le API esterne, consentendo agli agenti di accedere a funzionalità e dati. Insegnano all'agente come usare l'API, tramite esempi di utilizzo, istruendoli anche in quali argomenti passare e come interpretare il risultato.
- **Funzioni**: invece, sono funzioni definite dallo sviluppatore che fanno da supporto alla task che deve essere imparata dall'agente. Quando riceve una richiesta, l'agente decide se è necessario chiamare una funzione per completare la task, e se sì, quale funzione chiamare e con quali argomenti.
- **Data store**: risolvono il limite dei modelli linguistici dotati di conoscenza statica, fornendo accesso a informazioni più dinamiche e aggiornate, garantendo che le risposte del modello rimangano pertinenti. Si può pensare a un archivio dati come a una fonte di informazioni esterna e aggiornabile a cui un agente può attingere.

## Ciclo thinking (Thought) → acting (Act) and observing (Observe)

Il ciclo di pensiero, azione e osservazione è un processo iterativo che consente agli agenti AI di apprendere e adattarsi nel tempo. In questo ciclo, l'agente pensa (thought) per elaborare le informazioni raccolte, agisce (act) per interagire con l'ambiente e osserva (observe) i risultati delle sue azioni per informare le decisioni future. Questo processo continua fino a quando l'agente non ha raggiunto i suoi obiettivi o ha raggiunto un punto di arresto.

Le regole e le guidelines sono embeddadte direttamente nel system promt nel quale viene definto:

- il comportamento desiderato dell'agente
- i tool a cui ha accesso
- Il ciclo Pensiero-Azione-Osservazione , che integriamo nelle istruzioni LLM.

```plaintext
Role: Esperto di Analisi Dati Urbanistici.
Objective: Analizzare l'impatto del traffico a Milano.
Tools: [Web_Search, DB_Access].
Guidelines: 
1. Analizza la query.
2. Pensiero (Thought): Quale dato mi manca?
3. Azione (Action): Usa il tool necessario.
4. Osservazione (Observation): Leggi il risultato.
5. Se il dato è incompleto, torna al punto 2. Non superare i 5 tentativi.
"""
```

### Ciclo Thought → Act → Observe → Reflect



---

Referenze:
- https://medium.com/@aleixlopez/introduction-to-ai-agents-62a790d0bc22
- https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure