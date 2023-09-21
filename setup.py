import setuptools

with open("version.txt") as version_file:
    version = version_file.read().strip()

with open("README.md") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = [row.strip() for row in requirements_file]


setuptools.setup(
    name="tuple_math",
    version=version,
    author="y-lily",
    author_email="yisitlily@gmail.com",
    description="This package provides implementation of basic math operations for tuples.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/y-lily/tuple_math",
    license="MIT",
    packages=["tuple_math"],
    install_requires=requirements,
)
