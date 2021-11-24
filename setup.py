# caesarplus Setup file
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='caesarplus',
    url='https://github.com/awesomelewis2007/CaesarPlus/',
    author='Lewis Evans',
    author_email='awesomelewis2007@gmail.com',
    packages=['caesarplus'],
    install_requires=[''],
    version='0.1.7',
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='An advanced caesar cypher python module'
)
