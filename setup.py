from setuptools import setup, find_packages

def format_version(version):
    return version.tag.replace("dev-v", "").replace('v', '') if version.tag else None

setup(
    name="hellopkg",
    # ここでカスタムversion_scheme、local_schemeを記載するのであれば、toml側では不要
    use_scm_version={
        "version_scheme": format_version,
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    entry_points={"console_scripts": ["hello=hellopkg.cli:main",]},
)
