def error_handler(file: str):
    try:
        with open(file, "r") as f:
            print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
            print(f"SUCCESS: Archive recovered - ``{f.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISI ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISI ALERT: Attempting access to '{file}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def crisis_response(file: str):
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    lost_file = "lost_archive.txt"
    error_handler(lost_file)
    print()

    permission_deny_file = "classified_vault.txt"
    error_handler(permission_deny_file)
    print()

    error_handler(file)
    print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    file = "standard_archive.txt"
    crisis_response(file)
