# ReAct: Reason & Act

> Stato: #active
> Concetto Chiave: **Ragionamento Dinamico e Azione**
> Parent: [[2_Reasoning]]

Le tecniche di ragionamento come **Chain-of-Thought (CoT)** sono efficaci per problemi che richiedono più passaggi logici, ma non sono progettate per task che necessitano di interazione con l'ambiente o azioni dinamiche. **ReAct** è un framework di prompting che integra il ragionamento testuale con l'azione nel mondo reale, consentendo ai modelli di eseguire ragionamenti dinamici e interagire con l'ambiente per incorporare informazioni aggiuntive nel processo decisionale.

L'unione di **"acting"** (azione) e **"reasoning"** (ragionamento) permette agli esseri umani di apprendere nuovi task rapidamente e di prendere decisioni robuste, anche in circostanze mai viste o di fronte a incertezze informative.

### Come funziona ReAct

ReAct spinge i Large Language Models (LLM) a generare sia **tracce di ragionamento verbale** che **azioni** relative a un compito in modo alternato (*interleaved*). Questo permette al modello di:

1. **Reason to Act:** Eseguire un ragionamento dinamico per creare, mantenere e adattare piani d'azione di alto livello.
2. **Act to Reason:** Interagire con ambienti esterni (es. Wikipedia) per incorporare informazioni aggiuntive nel ragionamento.

Considerare il task come un processo decisionale sequenziale in un ambiente parzialmente osservabile.

Sia $x$ il problema o la domanda iniziale posta dall'utente. L'interazione dell'agente con l'ambiente avviene attraverso una sequenza di step temporali $t = 1, \dots, T$.

A ogni step $t$, l'agente ha accesso a una cronologia o "contesto" $h_t$, che include l'input iniziale e tutte le interazioni precedenti:
$$h_t = (x, r_1, a_1, o_1, \dots, r_{t-1}, a_{t-1}, o_{t-1})$$
Dove:

* $r_i$: Il ragionamento (*Thought*) generato allo step $i$.
* $a_i$: L'azione (*Action*) intrapresa allo step $i$.
* $o_i$: L'osservazione (*Observation*) ricevuta dall'ambiente esterno dopo l'azione $a_i$.

Il modello (LLM) agisce come una politica $\pi$ che genera la coppia $(\text{pensiero, azione})$ condizionata alla storia attuale:

$$(r_t, a_t) \sim P_{\theta}(r, a | h_t)$$

In ReAct, la generazione di $r_t$ e $a_t$ è interlacciata. Il pensiero $r_t$ non porta direttamente alla risposta, ma serve a determinare quale azione $a_t$ sia più opportuna.

L'azione $a_t$ viene eseguita in un ambiente esterno (es. Wikipedia API, calcolatrice, DB), restituendo un'osservazione $o_t$:

$$o_t = \text{Env}(a_t)$$

Questa osservazione viene poi aggiunta alla storia $h_{t+1}$, influenzando il ragionamento successivo $r_{t+1}$.


Dal punto di vista teorico, ReAct risolve il problema dell'**aggiornamento della conoscenza**. Se chiedi a un modello CoT chi è il vincitore di un premio assegnato ieri, il modello fallirà perché i suoi pesi sono statici. Un modello ReAct:

1. **Ragiona:** "Non conosco questa informazione nei miei dati di addestramento."
2. **Agisce:** Esegue una ricerca web.
3. **Osserva:** Legge il risultato.
4. **Conclude:** Fornisce la risposta corretta.

Grazie all'integrazione di capacità decisionali e di ragionamento, ReAct offre diversi vantaggi:

* **Intuitivo e facile da progettare:** Creare prompt ReAct è semplice; i formatori umani devono solo scrivere i propri pensieri in linguaggio naturale insieme alle azioni intraprese.
* **Generale e flessibile:** Funziona per task diversi con spazi di azione e necessità di ragionamento differenti, tra cui QA (domanda/risposta), verifica dei fatti, giochi testuali e navigazione web.
* **Performante e robusto:** Mostra una forte capacità di generalizzazione su nuovi casi apprendendo da pochissimi esempi (da 1 a 6), superando costantemente i modelli basati solo sul ragionamento o solo sull'azione.
* **Allineato all'uomo e controllabile:** Offre un processo decisionale interpretabile dove gli umani possono ispezionare la correttezza fattuale. Inoltre, è possibile correggere il comportamento dell'agente in tempo reale modificandone i pensieri.

ReAct è particolarmente efficace per task di ragionamento ad alta densità di conoscenza, come il **Multi-hop Question Answering** (domande complesse che richiedono più passaggi) e la **verifica dei fatti** (fact verification).

!!!quote Reference
    [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
