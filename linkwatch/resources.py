import importlib.resources

TEMPLATE_NAME = "status.html.j2"


def template_dir():
    return str(importlib.resources.files("linkwatch").joinpath("templates"))
