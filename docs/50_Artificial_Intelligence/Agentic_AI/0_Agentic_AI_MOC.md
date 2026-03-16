---
area: 🤖 artificial-intelligence
tags: [ai-agents, agentic-workflows, llm-reasoning]
created: 2026-03-12
---

# 🤖 AI Agents & Agentic Workflows (MOC)

> Stato: #growing
> MOC Genitore: [[50_Artificial_Intelligence]]

## 📑 Introduzione all'Agenticità

L'agenticità rappresenta l'evoluzione dei modelli linguistici da semplici generatori di testo a entità capaci di strutturare processi decisionali autonomi.

   [[1_Agente]] - _Componenti chiave di un agente AI: percezione, ragionamento, apprendimento, azione, memoria, comunicazione, pianificazione e controllo._

## 🧠 Architettura Cognitiva e Ragionamento

Fondamenti teorici che permettono al modello di simulare processi di pensiero complessi.

- [[2_Reasoning]] - _Chain of Thought (CoT) e scomposizione logica._
- [[2_1_CoT]] - _Scomposizione logica step-by-step per problemi complessi._
- - [[2_2_ReAct]] - _Integrazione tra Reason (ragionamento) e Act (azione)._
- [[2_3_Reflection]] - _Cicli iterativi di auto-correzione dell'output._


## 💾 Gestione della Memoria (Agent Memory)

Sistemi di archiviazione per la persistenza del contesto e della conoscenza.

- [[3_Short_Term_Memory]] - *Gestione della context window e cronologia della sessione.*
- [[3_1_Long_Term_Memory]] - *Utilizzo di Vector Database e RAG per richiamo a lungo termine.*
- [[3_2_Episodic_Semantic_Memory]] - *Archiviazione di esperienze passate e generalizzazione dei concetti.*

## 🛠️ Design dei Workflow e Tipologie di Agenti

Strategie di orchestrazione per l'esecuzione dei task.

### AI Workflows

- [[4_1_Prompt_Chaining]] - *Concatenazione sequenziale di istruzioni.*
- [[4_2_Routing_Parallelization]] - *Smistamento dei task e computazione parallela.*

### Agent Configurations

- [[5_1_Single_Agent_Systems]] - *Modelli singoli per la gestione end-to-end.*
- [[5_2_Multi_Agent_Systems]] - *Collaborazione tra agenti specializzati (Manager-Worker).*
- [[5_3_Communication_Models]] - *Protocolli gerarchici vs. Peer-to-Peer (Broadcast).*
- [[5_4_MCP]] - *Model Context Protocol per l'interazione standardizzata.*

## 🛡️ Valutazione, Sicurezza e Vincoli

Protocolli di controllo per sistemi autonomi.

- [[6_1_Agentic_Benchmarking]] - *Metriche di successo basate sull'azione (Task Success Rate).*
- [[6_2_Safety_Guardrails]] - *Prevenzione di loop infiniti, bias e factuality drift.*
- [[6_3_Adversarial_Defense]] - *Protezione da Prompt Injection e Jailbreak.*
- [[6_4_Human_In_The_Loop]] - *Integrazione della validazione umana nei processi critici.*

- adversarial prompt

- loop infinito

- factuality drift

- bias

- prompt injection/jailbreak

- permissioning