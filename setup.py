import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leela",
    version="1.0.0",
    author="Evan La Riviere",
    author_email="evan.lariviere@gmail.com",
    description="Agency Prepayment Modelling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "pandas"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Framework :: Sphinx",
        "Framework :: Pytest",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
