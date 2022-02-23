import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_cicd_test",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Indian966/pythonCIDITest",
    project_urls={
        "Bug Tracker": "https://github.com/Indian966/pythonCIDITest/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pybo"},
    packages=setuptools.find_packages(where="pybo"),
    python_requires=">=3.6",
)