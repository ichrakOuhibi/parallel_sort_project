import random

def generate_large_file(filename="large_input.txt", lines=1_000_000):
    with open(filename, "w") as f:
        for _ in range(lines):
            number = random.randint(1, 1_000_000)
            f.write(f"{number}\n")
    print(f"[✅] Fichier généré : {filename} avec {lines} lignes.")

if __name__ == "__main__":
    generate_large_file()