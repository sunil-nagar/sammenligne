class DiffMsg:
    path = None
    message = None
    displayable = False    

    def __init__(self, path, message, displayable):
        self.path = path
        self.message = message
        self.displayable = displayable

    def display(self):
        if self.displayable:
            print(self.path, self.message)


def create_not_found(path):
    return DiffMsg(path, "not found", True)


def create_size_mismatch(path, size1, size2):
    return DiffMsg(path, f"size difference ({size1}/{size2})", True)


def create_file_count_mismatch(path):
    return DiffMsg(path, "file count mismatch", False)


def create_date_mismatch(path, date1, date2):
    return DiffMsg(path, f"date mismatch ({date1}/{date2})", True)

def create_major_version_mismatch(path, majver1, majver2):
    return DiffMsg(path, f"major version mismatch ({majver1}/{majver2})", True)
