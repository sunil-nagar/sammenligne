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


def create_size_mismatch(path):
    return DiffMsg(path, "size difference", True)


def create_file_count_mismatch(path):
    return DiffMsg(path, "file count mismatch", False)


def create_date_mismatch(path):
    return DiffMsg(path, "date mismatch", True)
