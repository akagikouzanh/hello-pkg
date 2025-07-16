from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("hellopkg")
except PackageNotFoundError:
    __version__ = "unknown"