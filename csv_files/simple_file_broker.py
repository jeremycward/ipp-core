from .file_storage_method import FileStorageMethod
from core.core import AbstractDataBroker


class SimpleFileBroker(AbstractDataBroker):
    def __init__(self,root_directory):
        super().__init__(FileStorageMethod(root_directory))





