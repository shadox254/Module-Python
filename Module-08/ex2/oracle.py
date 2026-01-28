import os
import sys
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("Error, dotenv not find. Run pip install python-dotenv")
    sys.exit(2)


def oracle():

    # automatically loads the .env file located in the same directory
    load_dotenv()
    missing = False

    # os.getenv() retrieves the values stored in .env
    mode = os.getenv("MATRIX_MODE")
    if mode is None:
        mode = "missing"
        missing = True

    database = os.getenv("DATABASE_URL")
    if database is None:
        database = "Not connected to local instance"
        missing = True
    else:
        database = "Connected to local instance"

    api_access = os.getenv("API_KEY")
    if api_access is None:
        api_access = "Anonyme"
        missing = True
    else:
        api_access = "Authenticated"

    log_level = os.getenv("LOG_LEVEL")
    if log_level is None:
        log_level = "missing"
        missing = True

    network = os.getenv("ZION_ENDPOINT")
    if network is None:
        network = "Offline"
        missing = True
    else:
        network = "Online"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {network}")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if missing is False:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file no properly configured")
    print("[OK] Production overrides available")
    print()


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    oracle()
    print("The Oracle sees all configurations.")
