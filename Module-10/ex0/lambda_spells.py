def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    avg_power = sum(map(lambda x: x['power'], mages)) / len(mages)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


def lambda_spells():

    print("Testing artifact sorter...")
    artifacts_list = [
        {"name": "Keyblade", "power": 34, "type": "Sword"},
        {"name": "Light saber", "power": 77, "type": "Saber"},
        {"name": "F.L.U.D.D.", "power": 17, "type": "Water gun ?"},
        {"name": "BFG 9000", "power": 96, "type": "Gun"},
        {"name": "Tharkun", "power": 23, "type": "Staff"},
        {"name": "Master Sword", "power": 29, "type": "Sword"},
        {"name": "Azir's Staff", "power": 91, "type": "Staff"},
        {"name": "Kraber", "power": 50, "type": "Sniper"}
    ]
    sorted_artifacts_list = artifact_sorter(artifacts_list)
    i = 1
    artifacts_count = len(sorted_artifacts_list)
    for artifact in sorted_artifacts_list:
        print(f"{artifact["name"]} ({artifact["power"]} power) ", end="")
        if not i == 1 and not i == artifacts_count:
            print("and ", end="")
        if not i == artifacts_count:
            print("comes before ", end="")
        i += 1
    print("\n")
    print("========================================")
    print()
    print("Testing power filter...")
    mages_list = [
        {"name": "Kieffrey", "power": 321, "element": "Energie"},
        {"name": "Ryze", "power": 764, "element": "Runes"},
        {"name": "Schierke", "power": 543, "element": "Mind"},
        {"name": "Edward Elric", "power": 328, "element": "Alchemy"},
        {"name": "Mashle", "power": 99, "element": "Muscle"},
        {"name": "Gandalf", "power": 32, "element": "Yes"},
        {"name": "Dumbledore", "power": 32, "element": "Yes"},
        {"name": "Vel'Koz", "power": 123, "element": "Void"},
        {"name": "Aurelion Sol", "power": 1243, "element": "Stars"},
        {"name": "Sylas", "power": 342, "element": "Other"}
    ]
    min_power = 300
    filtered_mages_list = power_filter(mages_list, min_power)
    mages_count = len(filtered_mages_list)
    i = 1
    for mages in filtered_mages_list:
        print(f"{mages["name"]} ", end="")
        if i < mages_count:
            print("and ", end="")
        if i == mages_count:
            print(f"have a power rating above {min_power}")
        i += 1
    print()
    print("========================================")
    print()
    print("Testing spell transformer...")
    spells_list = ["Wind Slash", "Weaver's Wall", "Dragon's Rage",
                   "Glacial Storm", "Let's Bounce!", "Death Mark",
                   "Soul Shackles", "Public Execution", "Endless Banquet",
                   "Paranoia"]
    mapped_spells_list = spell_transformer(spells_list)
    for spell in mapped_spells_list:
        print(spell, end=" ")
    print("\n")
    print("========================================")
    print()
    mages_list = [
        {"name": "Kieffrey", "power": 321, "element": "Energie"},
        {"name": "Ryze", "power": 764, "element": "Runes"},
        {"name": "Schierke", "power": 543, "element": "Mind"},
        {"name": "Edward Elric", "power": 328, "element": "Alchemy"},
        {"name": "Mashle", "power": 0, "element": "Muscle"},
        {"name": "Gandalf", "power": 33, "element": "Yes"},
        {"name": "Dumbledore", "power": 33, "element": "Yes"},
        {"name": "Vel'Koz", "power": 123, "element": "Void"},
        {"name": "Aurelion Sol", "power": 1243, "element": "Stars"},
        {"name": "Sylas", "power": 342, "element": "Other"}
    ]
    stats = mage_stats(mages_list)
    print(f"max power: {stats["max_power"]["name"]} with \
{stats["max_power"]["power"]} power")
    print(f"min power: {stats["min_power"]["name"]} with \
{stats["min_power"]["power"]} power")
    print(f"average power: {stats["avg_power"]}")


if __name__ == "__main__":
    lambda_spells()
