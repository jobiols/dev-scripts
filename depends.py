import os
import ast

excludes = [
    "base",
    "sale",
    "uom",
    "contacts",
    "portal",
    "sms",
    "product",
    "account",
    "web_editor",
    "website",
    'sales_team'
]


def load_manifest(filename):
    """
    Loads a manifest
    :param filename: absolute filename to manifest
    :return: manifest in dictionary format
    """
    manifest = ""
    with open(filename, "r") as _f:
        for line in _f:
            if line.strip() and line.strip()[0] != "#":
                manifest += line
        try:
            ret = ast.literal_eval(manifest)
        except Exception:
            return {"name": "none"}
        return ret


def get_uml_data(path):
    """return a list of module data
    [
        {'name':['name1','name2','name3']},
        {'name2':['name4','name5','name6']}
    ]
    """
    ret = list()
    for root, dirs, files in os.walk(path):
        file_set = set(["__openerp__.py", "__manifest__.py"]).intersection(files)
        for file in list(file_set):
            manifest_file = "%s/%s" % (root, file)
            manifest = load_manifest(manifest_file)
            module = root[2:]
            if module in excludes:
                continue
            depends = list()
            for dep in manifest.get("depends"):
                if dep in excludes:
                    continue
                depends.append(dep)
            ret.append({module: depends})
    return ret


def create_uml():
    uml_data = get_uml_data("./")
    with open("depends.plantuml", "w") as _f:
        _f.write("@startuml\n")
        _f.write("\n")

        for module_data in uml_data:
            module_name = list(module_data.keys())[0]
            for depends in module_data[module_name]:
                _f.write("%s -d-> %s\n" % (module_name, depends))

        _f.write("\n")
        _f.write("@enduml\n")


create_uml()
