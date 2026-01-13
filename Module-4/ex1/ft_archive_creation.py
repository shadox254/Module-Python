def archive_creation(file):
    text = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()

    print(f"Initializing new storage unit: {file}")
    f = open(file, "w")
    print("Storage unit created successfully...")
    print()

    print("Inscribing preservation data...")
    for line in text:
        f.write(line + '\n')
        print(line.replace("[", "{[}").replace("]", "{]}"))
    f.close()
    print()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file}' ready for long-term preservation.")


if __name__ == "__main__":
    file = "new_discovery.txt"
    archive_creation(file)
