
import business_prototype.convert_scss_to_css
from flask import Flask, render_template, request, send_from_directory, send_file
from flask_cors import CORS
import json
from business.cursor import Cursor

cr = Cursor()
app = Flask(__name__)
CORS(app)


@app.route('/prototype', defaults={"path": "*"}) # Over die defaults ben ik nimeer zeker khad da verwijderd :///
# @app.route("/<path:path>")
def hello_world(path):  # put application's code here
    if not path:
        path = "/"
    else:
        path = "static/root/" + path
    cr.walk(path)
    return render_template("index.html", items=cr.environment.items)


# @app.route("/", defaults={"path": ""})
@app.route("/prototype2", methods=["GET"])
def home():
    # if "index.js" not in path and "style.css" not in path:
    cr.walk("/")
    return render_template("index.html", items=cr.items, is_root=(cr.current_global_path == "/"))


@app.route("/prototype2", methods=["POST"])
def walk_prototype2():
    path = request.json["path"]
    if path == "back":
        cr.fall()
    else:
        cr.walk(path)
    return render_template("index.html", items=cr.items)

@app.route("/video_prototype2", methods=["POST"])
def video():
    path = request.json["path"]

    debug_var = send_from_directory("/".join(cr.current_global_path.split("/")[:-2]), cr.current_global_path.split("/")[-1])
    return debug_var



@app.route("/get_item", methods=["POST"])
def get_item():
    path = request.json.get("path")
    return send_from_directory("/".join(path.split("/")[:-1]), path.split("/")[-1])


@app.route("/", methods=["POST"])
def walk():
    path = request.json["path"]
    if path == "back":
        cr.fall()
    else:
        cr.walk(path)
    # sorted(cr.items, lambda item: item.type[0]) TODO fix this
    json_items = []
    for item in cr.items:
        json_items.append(item.__dict__)

    return json.dumps(json_items)

@app.route("/media_items", methods=["POST"])
def get_media_items():
    path = request.json["path"]
    active_item_global_path = request.json["activeItem.global_path"]

    if path == "back":
        media_items = []
    else:
        media_items = cr.get_media_items(path, active_item_global_path)
    json_media_items = []
    for item in media_items:
        json_media_items.append(item.__dict__)

    return json.dumps(json_media_items)


@app.route("/get_items", methods=["POST"])
def get_items():
    path = request.json["path"]
    if not path:
        path = "/"
    cr.walk(path)
    iets: dict = {}
    json_builder = "["
    for item in cr.items:
        json_builder += item.__dict__.__str__() + ","
    json_builder += "]"
    # return json_builder.replace("'", '"')
    return '[{"is_dir": "True", "global_path": "/var/", "static_path": "static/root/var/", "href": "/var", "filename": "var/", "name": "var", "extension": "var/", "type": "None", "is_img": "False", "is_video": "False", "encoded_string": "None"}]'

if __name__ == '__main__':
    app.run()
