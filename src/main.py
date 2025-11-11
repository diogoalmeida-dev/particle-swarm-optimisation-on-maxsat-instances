from src import utils

CNF_FILES = {
    "1": "../cnf_files/uf20-01.cnf",
    "2": "../cnf_files/uf100-01.cnf",
    "3": "../cnf_files/uf250-01.cnf"
}

def main():
    while True:
        print("Select CNF file:")
        print("1 - uf20-01.cnf")
        print("2 - uf100-01.cnf")
        print("3 - uf250-01.cnf")
        cnf_choice = input("Enter choice (1-3): ").strip()
        if cnf_choice not in CNF_FILES:
            print("Invalid CNF file choice.")
            continue

        cnf_path = CNF_FILES[cnf_choice]
        clauses, num_clauses, num_vars = utils.read_cnf(cnf_path)
        print(f"\nLoaded: {cnf_path} — vars={num_vars}, clauses={num_clauses}")

if __name__ == "__main__":
    main()
