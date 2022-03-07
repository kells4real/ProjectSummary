import os


def run():
    lines = []
    rootDir = input("Enter Root Dir: ")
    getExt = input("Enter extensions seperated by a comma, no space: ")
    EXT = getExt.split(",")
    for subdir, dirs, files in os.walk(rootDir):
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            for ext in EXT:
                if filepath.endswith(ext):
                    with open(filepath, "r") as python_file:
                        for line in python_file:
                            line = line.strip()
                            if line:
                                lines.append(line)
    print(f"There is {len(lines)} lines of code in this project.")


if __name__ == '__main__':
    run()
