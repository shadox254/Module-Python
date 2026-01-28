def vault_security(file_to_open: str, file_to_create: str):
    """
    Simulates a secure vault operation using context managers.

    Demonstrates the use of the 'with' statement to safely handle file
        opening and automatic closing (resource management), ensuring
        the 'vault' is sealed even if errors occur during processing.

    Args:
        file_to_open (str): The path of the secure file to read.
        file_to_create (str): The path of the new file to generate.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    try:
        with open(file_to_open, "r") as f:
            print("Vault connection established with failsafe protocols")
            print()
            print("SECURE EXTRACTION:")
            print(f.read())
    except FileNotFoundError:
        print(f"The file: {file_to_open} does not exist.")
        print("Run data_generator.py first with: python3 data_generator.py")
    print()
    with open(file_to_create, "w") as f:
        print("SECURE PRESERVATION:")
        content = "[CLASSIFIED] New security protocols archived"
        f.write(content)
        print(content)
        print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    file_to_open = "classified_data.txt"
    file_to_create = "security_protocols.txt"
    vault_security(file_to_open, file_to_create)
