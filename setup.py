import re

from setuptools import setup, find_packages

PACKAGE_NAME = "n2w-it"

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Natural Language :: Italian",
    "Environment :: Console",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Internationalization",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Localization",
    "Topic :: Text Processing :: Linguistic",
]

requirements = []

setup_requirements = []

test_requirements = []


def get_version():
    version_regex = re.compile(r"^__version__ = ['\"]([^'\"]*)['\"]")

    with open("n2w_it/__init__.py", "r") as version_file:
        for line in version_file:
            version = version_regex.match(line)

            if version:
                return version.group(1)


def get_long_description():
    with open("README.md", "r") as readme_file:
        readme = readme_file.read()

    with open("HISTORY.md", "r") as history_file:
        history = history_file.read()

    return readme + '\n\n' + history


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    description="Converts numbers to italian words.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT license",
    author="Andrea Galvani",
    author_email="Andrea.Galvani96@outlook.com",
    keywords=[
        "n2w-it",
        "n2w_it",
        "italian number words converter",
    ],
    url="https://github.com/IlGalvo/N2W-IT",
    packages=find_packages(include=["n2w_it", "n2w_it.*"]),
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "n2w-it=n2w_it.__main__:main",
        ],
    },
    classifiers=CLASSIFIERS,
    python_requires=">=3.5",
    setup_requires=setup_requirements,
    install_requires=requirements,
    tests_require=test_requirements,
    include_package_data=True,
    zip_safe=False,
)
