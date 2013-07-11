from setuptools import setup, find_packages
import os

version = '0.9.11.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'xeditable', 'test_xeditable.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.xeditable',
    version=version,
    description="fanstatic xeditable.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic xeditable redturtle',
    author='RedTurtle Developers',
    url='https://github.com/RedTurtle/js.xeditable',
    author_email='sviluppoplone@redturtle.it',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jqueryui',
        'js.bootstrap',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'xeditable = js.xeditable:library',
            ],
        },
    )
