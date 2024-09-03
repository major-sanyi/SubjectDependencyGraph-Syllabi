import os
import json

def collect_json_objects(directory):
    json_objects = []
    for root, dirs, files in os.walk(directory):
        # Ne nézzük a 'docs' mappát
        if 'docs' in dirs:
            dirs.remove('docs')
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        if isinstance(data, dict):
                            # Ha a JSON adat egy objektum, hozzáadjuk a listához
                            json_objects.append(data)
                        elif isinstance(data, list):
                            # Ha a JSON adat egy tömb, hozzáadjuk az összes elemet a listához
                            json_objects.extend(data)
                    except json.JSONDecodeError as e:
                        print(f"JSON Decode Error in file {file_path}: {e}")
    return json_objects

def main():
    base_directory = 'Syllabi'  # A 'Syllabi' mappa
    
    # Gyűjtjük a JSON objektumokat a 'Syllabi' mappából
    syllabi_objects = collect_json_objects(base_directory)

    # Gyűjtjük a JSON objektumokat az 'Equivalence' mappából, ha létezik
    equivalence_directory = os.path.join('Equivalence')
    equivalence_objects = collect_json_objects(equivalence_directory)

    # A 'docs' mappa elérési útja
    docs_directory = os.path.join('docs')
    os.makedirs(docs_directory, exist_ok=True)  # Biztosítjuk, hogy a 'docs' mappa létezik

    # Kimeneti fájlok elérési útjai
    syllabi_output_file = os.path.join(docs_directory, 'syllabi.json')
    equivalence_output_file = os.path.join(docs_directory, 'equivalence.json')

    # Az összes JSON objektum mentése egyetlen fájlba
    try:
        with open(syllabi_output_file, 'w', encoding='utf-8') as f:
            json.dump(syllabi_objects, f, ensure_ascii=False, indent=4)
        print(f"Összefűzött JSON sikeresen mentve: {syllabi_output_file}")
    except IOError as e:
        print(f"IO Error while writing the file {syllabi_output_file}: {e}")

    try:
        with open(equivalence_output_file, 'w', encoding='utf-8') as f:
            json.dump(equivalence_objects, f, ensure_ascii=False, indent=4)
        print(f"Összefűzött JSON sikeresen mentve: {equivalence_output_file}")
    except IOError as e:
        print(f"IO Error while writing the file {equivalence_output_file}: {e}")

if __name__ == '__main__':
    main()
