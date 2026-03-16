# Reasoning

Parent: [[0_Agentic_AI_MOC]]

Il **ragionamento** è il processo interno dell'agente che consente di elaborare le informazioni e pianificare le azioni per risolvere una task. Con questo processo l'agente può scomporre un problema complesso in più problemi semplici, riflettere sulle esperienze passate, e pianificare le azioni future.
L'idea centrale è trasformare un processo di previsione statistica (prossimo token) in un processo di pianificazione ed esecuzione.

Il reasoning si basa sulla teoria della psicologia cognitiva chaiamata **Dual Process Theory** (**Daniel Kahneman**, *"Pensieri lenti e veloci"*). in cui viene postulo che il cervello umano utilizzi due modalità di pensiero distinte per elaborare le informazioni e prendere decisioni.
La teoria sostiene che ci siano due sistemi o menti in un unico cervello. Questi sistemi sono spesso definiti "impliciti" ed "espliciti" o **Sistema 1** e **Sistema 2**.

- **Sistema 1** - è il processo di pensiero più veloce, intuitivo e automatico. È coinvolto quando prendiamo decisioni rapide, facciamo associazioni o rispondiamo a stimoli in modo istintivo. Il Sistema 1 è spesso associato a processi mentali che avvengono senza sforzo consapevole, come il riconoscimento di volti, la comprensione del linguaggio naturale o la valutazione di situazioni sociali. Il Sistema 1 (intuizione) è più accurato nelle aree in cui abbiamo raccolto molti dati con feedback affidabili e rapidi.
- **Sistema 2** - è il processo di pensiero più lento, deliberato e logico. È coinvolto quando affrontiamo problemi complessi, prendiamo decisioni importanti o quando il Sistema 1 non è in grado di fornire una risposta adeguata. Il Sistema 2 richiede più sforzo cognitivo e attenzione, ed è spesso associato alla capacità di pianificare, ragionare e risolvere problemi in modo più analitico.

!!!quote Reference
    [Dual process theory](https://en.wikipedia.org/wiki/Dual_process_theory)

Gli LLM, nella loro forma base, operano quasi esclusivamente come un **Sistema 1 ipertrofico**. Generano parole basandosi su pattern statistici appresi, muovendosi alla velocità della luce ma senza una reale "riflessione" interna.

L'obiettivo dei framework di ragionamento è **forzare l'AI a ingaggiare un Sistema 2 artificiale**.

1. **Rallentamento:** Invece di rispondere subito, il modello scrive i passaggi intermedi.
2. **Allocazione di Risorse:** Generando più token di ragionamento, il modello "occupa" più spazio di calcolo per analizzare il problema.
3. **Verifica:** Proprio come noi ricontrolliamo un calcolo, il modello usa la traccia testuale prodotta per correggere eventuali derive logiche.

Un agente che opera solo in "Sistema 1" è pericoloso: agisce d'impulso, allucina strumenti inesistenti e cade in loop infiniti. L'implementazione del Sistema 2 permette:

- **Pianificazione Strategica:** Valutare diverse azioni prima di eseguirne una (Tree of Thoughts).
- **Gestione dell'Incertezza:** Riconoscere quando una risposta intuitiva è insufficiente e occorre consultare un tool esterno (ReAct).
- **Etica e Sicurezza:** I "Guardrails" agiscono come un supervisore di Sistema 2 che blocca le risposte inappropriate generate d'istinto dal Sistema 1.

Esistono diversi framework di ragionamento che sono stati sviluppati per consentire agli agenti di eseguire questo processo in modo efficace, come il:

- **Reason & Act (ReAct)**, [[2_2_ReAct]], 
- **Chain-of-Thought (CoT)**, [[2_1_CoT]],
- **Reflection**, [[2_3_Reflection]].