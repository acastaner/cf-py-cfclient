import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cyberfloodClient',
    version='0.0.2',
    author="Arnaud Castaner",
    author_email="arnaud.castaner@outlook.com",
    description="A CyberFlood REST API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acastaner/cf-py-cfclient",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
