def vault_security(file_to_open: str, file_to_create: str):
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    try:
        with open(file_to_open, "r") as f:
            print("Vault connection established with failsafe protocols")
            print()
            print("SECURE EXTRACTION:")
            print(f.read().replace("[", "{[}").replace("]", "{]}"))
    except FileNotFoundError:
        print(f"The file: {file_to_open} does not exist.")
        print("Run data_generator.py first with: python3 data_generator.py")
    print()
    with open(file_to_create, "w") as f:
        print("SECURE PRESERVATION:")
        content = "[CLASSIFIED] New security protocols archived"
        f.write(content)
        print(content.replace("[", "{[}").replace("]", "{]}"))
        print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    file_to_open = "classified_data.txt"
    file_to_create = "security_protocols.txt"
    vault_security(file_to_open, file_to_create)
