def ancient_text(file):
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file}")
    try:
        f = open(file, 'r')
        print("Connection established...")
        print()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return None
    print("RECOVERED DATA:")
    print(f.read().replace("[", "{[}").replace("]", "{]}"))
    f.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    file = "ancient_fragment.txt"
    ancient_text(file)
