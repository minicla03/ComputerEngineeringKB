import os
import re

def update_readme_stats():
    # 1. Analisi delle cartelle
    categories = [d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()]
    categories.sort()

    stats_table = "| Categoria | Note | Stato |\n| :--- | :--- | :--- |\n"
    total_notes = 0

    for cat in categories:
        # Conta i file .md escludendo i MOC e gli asset
        count = len([f for f in os.listdir(cat) if f.endswith('.md') and not f.endswith('_MOC.md')])
        total_notes += count
        
        # Indicatore visivo di "densità" della conoscenza
        progress = "🟢" if count > 10 else "🟡" if count > 0 else "⚪"
        stats_table += f"| {cat.replace('_', ' ')} | {count} | {progress} |\n"

    stats_table += f"| **TOTALE** | **{total_notes}** | 🚀 |\n"

    # 2. Aggiornamento del file README.md
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Sostituzione del contenuto tra i tag
    pattern = r".*?"
    replacement = f"\n\n{stats_table}\n"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"📊 Statistiche aggiornate: {total_notes} note totali.")

if __name__ == "__main__":
    update_readme_stats()