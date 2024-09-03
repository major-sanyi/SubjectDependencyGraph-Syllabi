import os
import json

def collect_json_files(directory):
    json_data = []
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
                        json_data.append(data)
                    except json.JSONDecodeError as e:
                        print(f"JSON Decode Error in file {file_path}: {e}")
    return json_data

def main():
    base_directory = '.'  # A jelenlegi munkakönyvtár
    json_data = collect_json_files(base_directory)

    # A kimeneti fájl elérési útja
    output_file = os.path.join(base_directory, 'docs', 'tantervek.json')

    # Az összes JSON adat mentése egyetlen fájlba
    with open(output_file, 'w', encoding='utf-8') as f:
        try:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
            print(f"Összefűzött JSON sikeresen mentve: {output_file}")
        except IOError as e:
            print(f"IO Error while writing the file {output_file}: {e}")

if __name__ == '__main__':
    main()
