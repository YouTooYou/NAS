import os
from .item import Item

TEMPLATE = "TEMPLATE"
IMAGE = "IMAGE"
VIDEO = "VIDEO"


class Cursor:
    def __init__(self):
        self.current_global_path = None
        self.current_static_path = None
        self.set_global_path("/")

        self.items = []
        self.item_names = []
        self.mode = TEMPLATE

    def update_items(self):
        # Clear lists
        self.items.clear()
        self.item_names.clear()

        # Fill objects
        for filename in os.listdir(self.current_global_path):
            self.items.append(Item(self.current_global_path + filename))
        # Sort objects
        self.items.sort(key=lambda x: (x.is_dir, x.name))

        # Fill filenames -> for easier access
        self.item_names = list(map(lambda i: i.name, self.items))

    def walk(self, absolute_path):
        self.set_global_path(absolute_path)
        # TODO Add check on file type
        self.update_items()
        print()

    def fall(self):
        self.set_global_path(
            "/".join(self.current_global_path.split("/")[:-2])
        )
        self.update_items()
        print()

    def set_global_path(self, path):
        if not path:
            path = "/"
        if not path[-1] == "/" and os.path.isdir(path):
            path += "/"


        self.current_global_path = path
        self.current_static_path = "static/root" + path

    def __str__(self):
        return self.current_global_path

    def get_item(self, global_path):
        for item in self.items:
            if item.global_path == global_path:
                return item

    def get_media_items(self, path, active_item_global_path):
        self.walk(path)
        media_items = []
        print("All media items:")
        for position, item in enumerate(self.items):
            if item.is_media:
                item.set_position(position)
                media_items.append(item)

                if item.global_path == active_item_global_path:
                    item.active_item = True

        return media_items