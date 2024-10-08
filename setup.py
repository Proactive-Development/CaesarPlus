from setuptools import setup
#This is to include the readme from the github repo
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='caesarplus',
    url='https://github.com/awesomelewis2007/CaesarPlus/',
    author='Proactive-Development',
    packages=['caesarplus'],
    install_requires=[''],
    version='0.1.8',
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='An advanced caesar cypher python module'
)
