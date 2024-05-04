#calculates md5 of all files located in "." (same location where script is being runned)

import os
import hashlib

def cmd5(file_path):
    hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): hash.update(chunk)
    return hash.hexdigest()

def dump_result(results):
    with open("results.txt", "w") as f:
        if 1:
            for file_path, md5 in results.items():
                f.write(f"{file_path}: {md5}\n")
        else:
            f.write(json.dumps(result))

def main():
    results = {}
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            md5 = cmd5(file_path)
            print("%s > %s" % (file_path, md5))
            results[file_path] = md5
    
    dump_result(results)

if __name__ == "__main__":
    main()
