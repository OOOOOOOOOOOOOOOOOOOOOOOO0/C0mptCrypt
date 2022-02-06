with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()
with open("README.md") as fp:
    readme = fp.read()
with open("LICENSE") as fp:
    license = fp.read()

setuptools.setup(
    name="C0mptCrypt",
    description="An object-oriented, minamalistic, simple encryption library in Python.",
    url="https://github.com/execution/C0mptCrypt",
    packages=["C0mptCrypt"],
    license=license,
    install_requires=requirements,
    version=0.1,
    long_description=readme,
)
