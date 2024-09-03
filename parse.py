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
    base_directory = '.'  # A jelenlegi munkakönyvtár
    json_objects = collect_json_objects(base_directory)

    # A kimeneti fájl elérési útja
    output_file = os.path.join(base_directory, 'docs', 'syllabi.json')

    # Az összes JSON objektum mentése egyetlen fájlba
    with open(output_file, 'w', encoding='utf-8') as f:
        try:
            json.dump(json_objects, f, ensure_ascii=False, indent=4)
            print(f"Összefűzött JSON sikeresen mentve: {output_file}")
        except IOError as e:
            print(f"IO Error while writing the file {output_file}: {e}")

if __name__ == '__main__':
    main()
