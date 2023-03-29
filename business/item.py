import base64
import os
import json
import mimetypes

# import file_data


class Item:
    def __init__(self, absolute_path):
        self.is_dir = os.path.isdir(absolute_path)
        self.position = -1

        self.global_path = absolute_path + "/" if self.is_dir else absolute_path
        self.static_path = "static/root" + self.global_path

        self.href = f"{absolute_path}"
        
        self.filename = absolute_path.split("/")[-1] + "/" \
                        if self.is_dir \
                        else absolute_path.split("/")[-1]
        self.name = self.filename.replace("/", "")

        self.extension = self.filename.split(".")[-1] \
                         if self.is_dir else False
        
        self.type = mimetypes.guess_type(self.global_path)

        self.is_img = self.type[0] is not None and self.type[0].__contains__("image")
        self.is_video = self.type[0] is not None and self.type[0].__contains__("video")
        self.is_media = self.is_video or self.is_img
        self.key = self.global_path

        self.active_item = False

        # if self.is_img or self.is_video:
        #     with open(self.global_path, "rb") as media:
        #         self.encoded_string = base64.b64encode(media.read())
        # else:
        #     self.encoded_string = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def set_position(self, position):
        self.position = position

    def __str__(self):
        # return json.dumps(self, default=lambda o: o.__dict__())
        return str(self.__dict__)
