import difflib


def diff(path1, path2):
    try:
        with open(path1, "r") as f1, open(path2, "r") as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

        # Generate the unified diff
        diff = difflib.unified_diff(
            file1_lines,
            file2_lines,
            fromfile=path1,
            tofile=path2,
            lineterm="",  # Important for consistent output across OS
        )
        return list(diff)
    except FileNotFoundError:
        print(f"Error: One or both files not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def cdiff(path1, path2):
    clean = []
    linediffs = diff(path1, path2)
    if linediffs and len(linediffs) > 0:
        count = 0
        for ld in linediffs:
            line = ld.strip()
            if len(line) > 80:
                line = line[0:80]
            if (
                len(line) > 0
                and count < 10
                and (line.startswith("+") or line.startswith("-"))
            ):
                clean.append(line)
                count = count + 1
    return "\n".join(clean)
