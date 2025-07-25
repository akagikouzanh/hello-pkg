from setuptools import setup, find_packages

setup(
    name="hellopkg",
    # ここでカスタムversion_scheme、local_schemeを記載するのであれば、toml側では不要
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    entry_points={"console_scripts": ["hello=hellopkg.cli:main",]},
)
