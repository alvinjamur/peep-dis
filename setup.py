from setuptools import setup, find_packages


setup(
    name='peepdis',
    version='0.0.1',
    description='Terminal object inspector for python',
    author='Austin McKay',
    author_email='austinmckay303@gmail.com',
    url='https://github.com/TheAustinator/peep-dis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)