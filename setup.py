import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pixie-python",
    version = "0.1.5",
    author = "Andre von Houck",
    author_email = "starplant@gmail.com",
    description = "Python bindings for Pixie, a full-featured 2D graphics library",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/treeform/pixie-python",
    package_dir = {"pixie": "src/pixie"},
    packages = setuptools.find_packages(where="src"),
    include_package_data = True,
    package_data = {"pixie": ["pixie.dll", "libpixie.so", "libpixie.dylib"]},
    python_requires = ">=3.6.0",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
  ],
)
