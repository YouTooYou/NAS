import uuid


class FileData:
    def __init__(self, encoded_string):
        self.id = str(uuid.uuid4().fields[-1])[:5]
        self.encoded_string = encoded_string