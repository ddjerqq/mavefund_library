import setuptools
from mavefund import __version__


with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()


setuptools.setup(
    name="mavefund",
    version=".".join(map(str, __version__)),
    license="GNU",
    author="ddjerqq",
    author_email="ddjerqq@gmail.com",
    url="https://github.com/ddjerqq/mavefund",
    keywords="mavefund stocks investing datascience finance",
    description="The official API client for the MaveFund.com",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas",
        "requests",
        "pydantic",
    ],
    packages=["mavefund"],
)
