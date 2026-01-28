import sys


# def stream_management_print():
#     print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
#     print()

#     archivist_id = input("Input Stream active. Enter archivist ID: ")
#     status_report = input("Input Stream active. Enter status report: ")
#     print()

#     print(f"{{[}}STANDARD{{]}} Archive status from {archivist_id}: "
#           f"{status_report}")
#     print("{[}ALERT{]} System diagnostic: Communication channels verified",
#           file=sys.stderr)
#     print("{[}STANDARD{]} Data transmission complete")
#     print()

#     print("Three-channel communication test successful.")


def stream_management():
    """
    Manages standard I/O streams to simulate a communication interface.

    Uses sys.stdin for reading user input, sys.stdout for standard messages,
        and sys.stderr for system alerts. This bypasses the higher-level
        print() and input() functions to interact directly with
        file descriptors.
    """
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    sys.stdout.write("\nInput Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().rstrip('\n')
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status_report = sys.stdin.readline().rstrip('\n')

    sys.stdout.write("\n[STANDARD] Archive status from "
                     f"{archivist_id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                     "verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    stream_management()
    # stream_management_print()
