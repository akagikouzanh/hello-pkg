from setuptools import setup, find_packages
from setuptools_scm import get_version

target_version = get_version()
fromatted_version = target_version.replace("dev-v", "").replace('v', '') if target_version else None

setup(
    name="hellopkg",
    version=fromatted_version,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    entry_points={"console_scripts": ["hello=hellopkg.cli:main",]},
)
