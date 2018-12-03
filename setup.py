import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zenodo",
    version="0.0.1",
    author="Ronald van Haren",
    author_email="r.vanharen@esciencecenter.nl",
    description=("A python library to upload to Zenodo"),
    license="Apache 2.0",
    keywords="Zenodo",
    url="https://github.com/ewatercycle/zenodo",
    packages=['zenodo'],
    include_package_data=False,    # include everything in source control
    scripts=['zenodo/scripts/zenodo'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=['requests', 'configargparse', 'yaml', 'json', 'urllib',
                      'datatime'],
)
