from setuptools import setup, find_packages

version_ns = {}
with open("hellopkg/__init__.py") as f:
    exec(f.read(),version_ns)


setup(
    name="hellopkg",
    version=version_ns["__version__"],
    packages=find_packages(),
    entry_points={"console_scripts": ["hello=hellopkg.cli:main",]},
)
