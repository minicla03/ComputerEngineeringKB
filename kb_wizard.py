import os

def get_subfolders(path='.'):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d[0].isdigit()]

def create_note(path, filename, title, parent_moc):
    full_path = os.path.join(path, f"{filename}.md")
    if not os.path.exists(full_path):
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\nParent: [[{parent_moc}]]\n\n## Note\n- ")
    return full_path

def interactive_wizard():
    print("="*50)
    print("🏛️  ENGINEERING KB - ARCHITECT COMMAND CENTER")
    print("="*50)
    print("1. 📁 Nuova Macro-Area (es. 60_Infrastructure)")
    print("2. 📦 Nuovo Modulo in Area Esistente (es. Docker in 30_Tools)")
    print("3. 🚀 Setup Completo (Nuova Area + Nuovo Modulo)")
    
    choice = input("\nSeleziona un'opzione (1/2/3): ").strip()

    parent_path = ""
    module_name = ""

    # --- LOGICA DI SELEZIONE ---
    if choice == '1' or choice == '3':
        parent_path = input("Nome Nuova Macro-Area (es. 70_DevOps): ").strip().replace(" ", "_")
        os.makedirs(parent_path, exist_ok=True)
        if choice == '1':
            print(f"✅ Macro-Area '{parent_path}' creata.")
            return

    if choice == '2':
        parents = get_subfolders()
        if not parents:
            print("❌ Nessuna Macro-Area trovata. Crea prima una Macro-Area (Opzione 1).")
            return
        print(f"\nMacro-Aree disponibili: {', '.join(parents)}")
        parent_path = input("In quale Macro-Area vuoi operare?: ").strip()

    if choice in ['2', '3']:
        module_name = input("Nome del nuovo Modulo (es. Kubernetes): ").strip().replace(" ", "_")
        module_full_path = os.path.join(parent_path, module_name)
        os.makedirs(os.path.join(module_full_path, "assets"), exist_ok=True)
        
        # --- CREAZIONE NOTE ---
        print("\n📝 Inserisci i titoli delle note atomiche (separati da virgola):")
        subs_input = input("> ").split(',')
        sub_topics = [s.strip() for s in subs_input if s.strip()]

        moc_name = f"{module_name}_MOC"
        moc_path = os.path.join(module_full_path, f"{moc_name}.md")
        
        with open(moc_path, "w", encoding="utf-8") as f:
            f.write(f"# 🗺️ {module_name.replace('_', ' ')} (MOC)\n\n> Area: [[{parent_path}]]\n\n## 📌 Indice\n")
            for sub in sub_topics:
                sub_filename = f"{module_name}_{sub.replace(' ', '_')}"
                f.write(f"* [[{sub_filename}]]\n")
                create_note(module_full_path, sub_filename, sub, moc_name)

    print("\n" + "="*50)
    print(f"✨ Operazione completata con successo!")
    print("="*50)

if __name__ == "__main__":
    try:
        interactive_wizard()
    except KeyboardInterrupt:
        print("\n\n👋 Wizard interrotto.")