from setuptools import setup, find_packages
from setuptools_scm import get_version


setup(
    name="hellopkg",
    # ここでカスタムversion_scheme、local_schemeを記載するのであれば、toml側では不要
    version=get_version(),
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    entry_points={"console_scripts": ["hello=hellopkg.cli:main",]},
)
