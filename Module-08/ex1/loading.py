import importlib.util
try:
    import pandas
    import requests
    import matplotlib.pyplot as plt
except ImportError:
    pass


def loading():
    print("Checking dependencies:")

    # dependecies_list contains all dependency names contained in
    #       requirements.txt
    dependencies_list = ["pandas", "requests", "matplotlib"]

    # Checks each dependency to see if it is installed and displays an
    #       installation message or an error message.
    for dependecy in dependencies_list:

        # importlib.util.find_spec(dependency) return lot of information
        #       about the dependency
        name = importlib.util.find_spec(dependecy)
        if name is None:
            print(f"[KO] {dependecy} is not installed. Run pip install -r \
requirements.txt or poetry install.")
            return
        else:
            name = __import__(dependecy)
            version = name.__version__
            print(f"[OK] {dependecy} ({version}) - ", end="")
            if dependecy == "pandas":
                print("Data manipulation ready")
            elif dependecy == "requests":
                print("Network access ready")
            elif dependecy == "matplotlib":
                print("Visualization ready")
    print()

    print("\nSimulate request...")
    try:
        # to tests if requests work
        # requests.get("https://www.python.org/") returns informations of url
        response = requests.get("https://www.python.org/")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    print()

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    # Create a DataFrame with sample data
    data = pandas.DataFrame([{'A': 3, 'B': 5, 'C': 1, 'D': 2},
                             {'A': 6, 'B': 4, 'C': 7, 'D': 6},
                             {'A': 7, 'B': 5, 'C': 3, 'D': 1}])
    print(data)
    print("Generating visualization...")
    print()

    filename = "matrix_analysis.png"
    # Create a bar chart from the data
    data.plot(kind='bar', title="Matrix Analysis Simulation")

    # Label the axes for clarity
    plt.xlabel("Index")
    plt.ylabel("Values")

    # Save the plot to a file instead of displaying it
    plt.savefig(filename)

    print("Analysis complete!")
    print(f"Result saved to: {filename}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    loading()
