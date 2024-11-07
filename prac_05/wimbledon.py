"""
Estimate = 20 minutes
Actual = 32 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Provide information to the user on previous wimbledon winners."""
    champions = get_champions(FILENAME)
    champion_to_count, countries = process_champions(champions)
    display_champions(champion_to_count, countries)


def get_champions(filename):
    """Read target file to return champions as a list."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            champions.append(parts)
    return champions


def process_champions(champions):
    """Create dictionary of champions and their total wins."""
    champion_to_count = {}
    countries = set()
    for champion in champions:
        countries.add(champion[INDEX_COUNTRY])
        try:
            champion_to_count[champion[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[champion[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_champions(champion_to_count, countries):
    """Display champions and associated countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
