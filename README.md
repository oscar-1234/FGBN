# 🎄 Fabbrica Elfi AI - Sistema di Gestione Emergenze 🎅

<img src="https://github.com/user-attachments/assets/24f242fb-7eef-4dc8-a6fa-b1ff103b57b1" align="left" alt="ElfoPizza" width="100" height="100" />

> **"Quando un elfo ha il raffreddore, il Natale non si ferma!"**

Benvenuti nella repository ufficiale di **F-AI** (*Fabbrica Elfi AI*), il progetto presentato per la **Datapizza Christmas AI Challenge 2025**!

Organizzare i turni della fabbrica di giocattoli di Babbo Natale è facile finché gli elfi stanno bene. Ma quando arriva un imprevisto, la gestione diventa complessa e un semplice foglio Excel non basta più.

**F-AI** è un sistema multi-agente intelligente progettato per salvare il Natale gestendo le emergenze di personale nella fabbrica di giocattoli più famosa del mondo.
Sfruttando la potenza del framework `datapizza-ai` e l'esecuzione sicura in sandbox, il sistema capisce le regole in linguaggio naturale e le applica dinamicamente scrivendo codice Python in tempo reale.

Zero hardcoding. Massima trasparenza. Il Natale non si ferma! 🎄

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Datapizza AI](https://img.shields.io/badge/Framework-Datapizza_AI-FF6B6B.svg)
![E2B](https://img.shields.io/badge/Runtime-E2B-FF8800)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🍕 Powered by Datapizza AI Framework

Il cuore pulsante di questa applicazione è costruito interamente su [datapizza-ai](https://docs.datapizza.ai). Abbiamo spinto il framework al limite per creare un'architettura affidabile e "production-ready":

*   **Hub & Spoke Architecture**: Un `Orchestrator Agent` centrale coordina una squadra di specialisti (`Code Generator`, `Explainer`, `Narrator`) per dividere i compiti cognitivi.
*   **Dynamic Code Execution**: Utilizza tool custom per generare ed eseguire codice Python "al volo" all'interno di sandbox sicure **E2B**, garantendo calcoli deterministici su dati non strutturati.
*   **Self-Correcting Agents**: Grazie ai loop di feedback nativi del framework, l'agente programmatore è in grado di leggere gli errori di esecuzione e correggere il proprio codice autonomamente.
*   **Context-Aware Memory**: Sistema ibrido che mantiene sia la memoria conversazionale che lo stato strutturato delle sostituzioni precedenti per evitare conflitti nei turni.

## ✨ Overview & Punti di Forza

L'idea nasce da portare al limite una necessità: **totale dinamicità**. Le regole di sostituzione della fabbrica cambiano spesso e non potevano essere hardcodate.

F-AI risolve il problema con un approccio **AI-First**:

### 🎯 Core Features
1.  **Zero Hardcoding**: Le regole sono definite in **YAML + Natural Language**. L'AI le legge, le comprende e scrive il codice per applicarle dinamicamente.
2.  **Sandbox Dinamico**: Utilizza un **Code Interpreter custom** basato su **E2B**. Il codice Python generato viene eseguito in un ambiente isolato e sicuro, garantendo calcoli deterministici.
3.  **Memoria Ibrida**: Unisce lo storico della chat (conversazionale) al contesto applicativo strutturato (sostituzioni già fatte), eliminando conflitti nei turni.
4.  **Autocorrezione (Self-Healing)**: Il `Code Generator Agent` è in grado di leggere i traceback degli errori di esecuzione e correggere il proprio codice autonomamente.

### 🛡️ Affidabilità & Sicurezza
5.  **Direct Injection**: Regole e strutture dati vengono iniettate direttamente nel System Prompt degli agenti, evitando l'effetto "telefono senza fili".
6.  **Validazione Multi-Layer**: Uso estensivo di **Pydantic models** per garantire la type-safety end-to-end. Nessun dato esce dalla sandbox senza essere validato.
7.  **Trasparenza Cristallina**: Nessuna "Black Box". Un `Explainer Agent` dedicato spiega il "perché" di ogni decisione.

### 🎨 User Experience (UX)
8.  **Setup Wizard Intuitivo**: Carica l'Excel, scegli il template e sei operativo in 3 click. Zero configurazioni manuali complesse.
9.  **Interfaccia Intuitiva**: Modalità Chat per l'uso quotidiano (accessibile a tutti gli elfi) + Modalità Debug per i tecnici che vogliono ispezionare il "pensiero" dell'AI.
10. **Narrativa Magica**: Per tenere alto il morale, il `Narrator Agent` trasforma i freddi log tecnici in epiche storie natalizie.

## 🧠 Architettura

L’applicazione è una web app **Streamlit** che guida l’utente dalla configurazione dell’orario alla gestione delle emergenze, mantenendo tutto lo stato in una sessione tipizzata tramite `SessionManager`. Il file Excel viene caricato, salvato in una cartella dati dedicata e associato alla configurazione corrente insieme a struttura, regole e template selezionato.

La definizione di struttura e regole non è hardcodata nel codice, ma proviene da template validati tramite `TemplateManager`, che legge il file YAML `default_templates.yaml` e li espone all’interfaccia come opzioni preconfigurate. Se necessario, l'utente può scegliere di impostare una nuova configurazione. In questo modo è possibile cambiare completamente schema del file e logica di sostituzione intervenendo solo sui template o scrivendo online le regole, senza toccare la logica applicativa.

## 🤖 Sistema multi‑agente Datapizza

Il cuore intelligente del sistema è costruito con il framework `datapizza-ai`, che istanzia un **sistema multi‑agente** tramite `create_multi_agent_system` nel modulo `src/agents/factory.py`. Un **Orchestrator Agent** centrale riceve il prompt completo e decide come coinvolgere i vari specialisti:

*   **Code Generator**: Traduce le regole in linguaggio naturale in codice Python eseguibile.
*   **Explainer**: Produce spiegazioni tecniche leggibili del processo decisionale.
*   **Narrator**: Converte l’esito dei calcoli in una storia natalizia adatta agli elfi.

Ogni agente ha prompt dedicati nella cartella `src/agents/config`, permettendo di affinare separatamente tono, ruolo e responsabilità.

<img width="498" height="353" alt="Architettura Hub & Spoke" src="https://github.com/user-attachments/assets/47c17bcb-344b-4ad7-bcee-1223d87fc85d" />

## 🧪 Esecuzione sicura & Memoria

Il codice generato dagli agenti non viene eseguito localmente ma attraverso un **tool custom** `execute_code_in_sandbox`. Questo processo:
1.  Apre una sandbox **E2B**.
2.  Carica il file Excel e il modulo dinamico `user_logic.py`.
3.  Invoca in modo controllato la funzione `calcola_sostituzioni(df)`.
L’output viene serializzato in JSON (`success`, `output` o `error` + `traceback`) così che l’orchestratore possa reagire, chiedere correzioni al Code Generator o mostrare gli errori in modalità debug.

La memoria conversazionale è gestita da `ConversationMemoryManager`, che incapsula `datapizza.memory.Memory` e mantiene sia la chat completa (turni user/assistant) sia un contesto applicativo con tutte le sostituzioni effettuate e l’ultima richiesta. Questo consente agli agenti di avere uno **storico strutturato** delle emergenze già gestite (riassunto in testo tramite `get_substitutions_summary`) e alla UI di mostrare statistiche e dettagli tecnici senza perdere consistenza tra una richiesta e l’altra [file:fe106b1f-dff9-4f94-8c85-0975011fa718].

## 🛠️ Tech Stack

### Core AI & Frameworks
*   **[Datapizza AI Framework](https://docs.datapizza.ai/)** (v0.0.9): Backbone dell'architettura agentica.
*   **[E2B Code Interpreter](https://e2b.dev/)** (v1.5.2): Sandbox sicura per l'esecuzione di codice Python generato.
*   **[OpenAI](https://openai.com/)**: Modelli LLM (`gpt-4o` per reasoning, `gpt-4o-mini` per task leggeri).

### Backend & Data Processing
*   **Python 3.10+**: Linguaggio base (testato su 3.12).
*   **Pandas & OpenPyXL**: Manipolazione avanzata dei file Excel dei turni.
*   **Pydantic**: Validazione rigorosa dei dati e dello schema JSON di output.

### Frontend & UI
*   **Streamlit**: Interfaccia utente interattiva e reattiva.
*   **Streamlit Chat**: Componenti per l'interazione conversazionale stile chat.

## 🚀 Installation & Setup

Segui questi passaggi per avviare la fabbrica degli elfi sul tuo computer locale.

### Prerequisiti
*   **Python 3.10** o superiore installato.
*   Una **API Key OpenAI** ([ottienila qui](https://platform.openai.com/api-keys)).
*   Una **API Key E2B** ([ottienila qui](https://e2b.dev/dashboard)).

### 1. Clona il repository
```
git clone https://github.com/oscar-1234/F-AI.git
cd F-AI
```

### 2. Setup Automatico (Windows)
Abbiamo preparato uno script magico per configurare l'ambiente in un colpo solo. Esegui da terminale:
```
setup.bat
```

Questo script creerà il virtual environment (`venv`), installerà tutte le dipendenze da `requirements.txt` e creerà le cartelle necessarie (`app/data`, `src/data`).

### 3. Configurazione Variabili d'Ambiente
1.  Rinomina il file `.env.example` in `.env`.
2.  Aprilo con un editor di testo e inserisci le tue chiavi:
```
OPENAI_API_KEY=sk-proj-xxxxxxxx...
E2B_API_KEY=e2b_xxxxxxxx...
```

### 4. Avvia l'Applicazione 🎅
Una volta configurato tutto, lancia il sistema con:
```
run.bat
```
L'applicazione si aprirà automaticamente nel tuo browser all'indirizzo `http://localhost:8501`.

## 🖥️ Utilizzo

Per prima cosa carica un file **Excel** con l’orario degli elfi (trovi un file di esempio `sample.xlsx` in `app/assets`), scegli un template tra quelli disponibili e personalizza struttura e regole di sostituzione direttamente dall’interfaccia Streamlit. Una volta confermata la configurazione, il sistema passa automaticamente alla modalità chat.

Nella schermata principale puoi:
- Vedere nella sidebar il riepilogo del file caricato, la struttura, le regole attive e – se presenti – le sostituzioni calcolate in precedenza.  
- Interagire via chat con Babbo Natale, descrivendo le emergenze (assenze, reparti, giorni, orari) in linguaggio naturale; il sistema penserà a tutto il resto.

Per chi vuole scavare più a fondo è disponibile una **Modalità Debug**, che mostra stato di sessione, memoria conversazionale e, quando presenti, i dettagli tecnici delle sostituzioni.

## 🎯 Esempio rapido

1. Avvia l’applicazione e, nella schermata di **configurazione**, carica il tuo file `.xlsx` con i turni degli elfi, quindi seleziona uno dei template proposti oppure personalizza manualmente struttura e regole. <img width="1765" height="746" alt="Configurazione" src="https://github.com/user-attachments/assets/fb3d6251-01a2-4065-967c-225a53f04ede" />
 
2. Premi “🚀 Avvia Sistema” per salvare la configurazione e passare alla chat interattiva con Babbo Natale.  
3. Nella casella di input puoi scrivere qualcosa come:  
   `Ciao Babbo Natale! Sfortunatamente c’è stata un’epidemia di Singhiozzo di Pan di Zenzero. Puoi indicarmi le sostituzioni per Martedì?`
4. L’orchestratore multi‑agente analizzerà richiesta, struttura, regole e storico sostituzioni, genererà il codice Python necessario, lo eseguirà in sandbox E2B e restituirà sia la proposta di sostituzione sia una spiegazione leggibile del ragionamento. Se il modello fornisce anche l’output strutturato in JSON, questo verrà validato con Pydantic e mostrato come tabella, insieme a metriche e riepilogo nel pannello laterale.
<img width="1910" height="818" alt="image" src="https://github.com/user-attachments/assets/f8f3e893-721b-4bb2-9e10-82dc99b06da1" />


## 🎄 Conclusione

Fabbrica Elfi AI nasce per togliere stress alle squadre elfiche del Polo Nord, trasformando notti insonni tra fogli Excel e turni scoperti in pochi messaggi di chat con Babbo Natale. Tra sandbox sicure, memoria conversazionale e racconti epici dei turni più difficili, l’obiettivo è uno solo: far sì che ogni regalo arrivi in tempo, anche quando gli elfi hanno bisogno di una giornata di riposo.  

## 📂 Struttura del Progetto
```
F-AI/
├── app/
│ ├── main.py # Entry point Streamlit UI
│ └── assets/ # File statici (sample excel)
├── src/
│ ├── agents/ # Logica agenti (Orchestrator, Narrator, ecc.)
│ ├── templates/ # Template YAML per regole e strutture
│ ├── tools.py # Tool E2B Sandbox
│ ├── config.py # Configurazione
│ ├── models.py # Validazione Pydantic
│ └── memory_manager.py # Gestione memoria ibrida
├── requirements.txt # Dipendenze Python
└── run.bat # Script di avvio rapido
```

## 📄 Licenza
Distribuito sotto licenza **MIT**. Vedi `LICENSE` per maggiori informazioni.

> **Sviluppato con agenti intelligenti 🤖 condividendo una pizza 🍕 per la sfida "Datapizza Christmas AI Challenge 2025 🎄"**
