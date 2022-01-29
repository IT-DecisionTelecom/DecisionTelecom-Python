import pkg_resources
import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="decisiontelecom",
    version="1.0.0",
    description="A Python client library for IT-Decision Telecom messaging API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/IT-DecisionTelecom/DecisionTelecom-Python",
    author="IT-Decision Telecom",
    author_email="info@it-decision.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests>=2.27.1"],
    extras_require={
        "dev": [
            "unittest",
            "responses",
        ]
    },
    keywords=["decisiontelecom", "sms", "viber", "messaging"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
