import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyprowl",
    version="1.0.1",
    author="Todd Roberts",
    author_email="todd@toddrob.com",
    description="Prowl API wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toddrob99/pyprowl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)