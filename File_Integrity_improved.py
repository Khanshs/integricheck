import datetime
import os
import hashlib
import json


# ================= HASHING =================

def compute_file_hash(file_path, algorithm='sha256'):
    # Compute the hash of a single file.
    # Tính toán hash của một file duy nhất.
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


# ================= SCANNING =================

def scan_file(file_path, algorithm='sha256'):
    # Scan a single file.
    # Quét một file duy nhất (nếu tồn tại).
    if os.path.isfile(file_path):
        print(f"[FILE] {file_path}")
        print(f"[{algorithm}] Hash: {compute_file_hash(file_path, algorithm)}")
    else:
        print(f"Error: {file_path} is not a file.")
    separator(file_path)
    write_hash_record(file_path, "N/A")


def scan_folder(folder_path, algorithm='sha256'):
    # Scan all files in a folder (including subfolders).
    # Quét toàn bộ thư mục (kể cả thư mục con).
    if os.path.isdir(folder_path):
        separator(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                print(f"[FOLDER] {full_path}")
                print(f"[{algorithm}] Hash: {compute_file_hash(full_path, algorithm)}")
                write_hash_record(full_path, compute_file_hash(full_path, algorithm))
    else:
        print(f"Error: {folder_path} is not a folder.")


# ================= RECORDING =================

def write_hash_record(file_path, file_hash):
    # Write hash record to JSON file.
    # Ghi bản ghi hash vào file JSON.
    if os.path.basename(file_path) == "hash_log.json":
        return

    record = {
        "file_name": os.path.basename(file_path),
        "file": file_path,
        "sha256": file_hash,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    record_dir = os.path.dirname(file_path) if os.path.isfile(file_path) else file_path
    record_file = os.path.join(record_dir, "hash_log.json")

    if os.path.exists(record_file):
        with open(record_file, 'r') as rf:
            records = json.load(rf)
    else:
        records = []

    records.append(record)

    with open(record_file, 'w') as wf:
        json.dump(records, wf, indent=4)


def separator(file_path):
    # Insert a separator in JSON file for each scan session.
    # Thêm dấu phân cách trong JSON cho từng lần quét.
    record_dir = os.path.dirname(file_path) if os.path.isfile(file_path) else file_path
    record_file = os.path.join(record_dir, "hash_log.json")

    if os.path.exists(record_file):
        with open(record_file, 'r') as rf:
            records = json.load(rf)
    else:
        records = []

    records.append({
        "separator": f"------ New Records at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ------"
    })

    with open(record_file, 'w') as wf:
        json.dump(records, wf, indent=4)


# ================= MAIN =================

def main(path, algorithm='sha256'):
    # Decide whether to scan a file or a folder.
    # Quyết định quét file hay thư mục.
    if os.path.isfile(path):
        scan_file(path, algorithm)
    elif os.path.isdir(path):
        scan_folder(path, algorithm)
    else:
        print("Error: Path does not exist.")


if __name__ == "__main__":
    user_input = input("Enter file or folder path: ").strip()
    main(user_input, algorithm='sha256')
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Integrity record updated in 'hash_log.json'.")
