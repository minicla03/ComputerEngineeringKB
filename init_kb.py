import os

def create_kb_structure():
    # Definizione della struttura: { "percorso/cartella": ["file1.md", "file2.md"] }
    structure = {
        "00_Inbox": ["README.md"],
        "10_Theory/Algorithms": ["Complexity_Basics.md"],
        "10_Theory/Data_Structures": ["Trees_and_Graphs.md"],
        "20_Languages/Python": ["Python_MOC.md"],
        "20_Languages/Rust": ["Rust_MOC.md"],
        "30_Frameworks_Tools/Android/assets": [],
        "30_Frameworks_Tools/Android": ["Android_MOC.md"],
        "40_Design_Patterns": ["SOLID_Principles.md", "Architecture_Overview.md"],
        "50_Project_Journal": ["2026_Learning_Log.md"],
        "99_Meta/Templates": ["Technical_Note_Template.md"]
    }

    print("🚀 Inizializzazione Engineering Knowledge Base...")

    for folder, files in structure.items():
        # Crea la cartella (e le parent folder se necessario)
        os.makedirs(folder, exist_ok=True)
        print(f"📁 Creata cartella: {folder}")

        # Crea i file iniziali
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {file.replace('.md', '').replace('_', ' ')}\n\n"
                            f"> Stato: #seed\n\n"
                            f"## Note\n- Inizia a scrivere qui...")
                print(f"  📄 Creato file: {file}")

    # Creazione file speciali nella root
    files_root = {
        "index.md": "# 🧠 Engineering Knowledge Base\n\nBenvenuto nel tuo secondo cervello.",
        ".gitignore": ".vscode/\n*.exe\n.DS_Store\nnode_modules/",
        "README.md": "# Engineering KB\n\nGestito con Foam e VS Code."
    }

    for name, content in files_root.items():
        if not os.path.exists(name):
            with open(name, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"📝 Creato file di sistema: {name}")

    print("\n✅ Struttura completata con successo. Buon coding!")

if __name__ == "__main__":
    create_kb_structure()