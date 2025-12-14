from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def resource_path(*paths):
    return PROJECT_ROOT.joinpath("resources", *paths)
