import setuptools

setuptools.setup(
    name = "pixie-python",
    version = "0.1.0",
    author = "Andre von Houck",
    author_email = "starplant@gmail.com",
    description = "Python bindings for Pixie, a full-featured 2D graphics library",
    url = "https://github.com/treeform/pixie-python",
    package_dir = {"": "src"},
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
