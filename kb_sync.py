import subprocess
import datetime
import sys

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore Git: {e.stderr}")
        return None

def sync_kb():
    print("🔄 Avvio sincronizzazione Knowledge Base...")

    # 1. Git Add
    run_git_command(["git", "add", "."])

    # 2. Git Commit
    # Se l'utente passa un messaggio come argomento, lo usa; altrimenti usa un timestamp.
    commit_msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else f"Auto-sync: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    commit_res = run_git_command(["git", "commit", "-m", commit_msg])
    if commit_res:
        print(f"✅ Commit effettuato: {commit_msg}")
    else:
        print("⚠️ Nulla da committare, il repository è già aggiornato.")

    # 3. Git Push
    print("🚀 Invio dati al server remoto...")
    push_res = run_git_command(["git", "push", "origin", "main"])
    
    if push_res is not None:
        print("🏁 Sincronizzazione completata con successo!")

if __name__ == "__main__":
    sync_kb()