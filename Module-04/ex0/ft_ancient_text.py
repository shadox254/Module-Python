def ancient_text(file: str):
    """
    Simulates a 'Cyber Archives' data recovery interface and displays
        the content of the specified file.

    Args:
        file (str): The path to the file to be read.

    Returns:
        None: This function performs side effects (printing) and does not
            return a value, except explicitly None on file error.
    """
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
    print(f.read())
    f.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    file = "ancient_fragment.txt"
    ancient_text(file)
