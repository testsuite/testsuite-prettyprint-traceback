import pkgutil
from setuptools import setup


def get_packages():
    return [name for _, name, ispkg in pkgutil.walk_packages('.') if name.startswith('testsuite') and ispkg]

setup(
    name='testsuite-prettyprint-stacktrace',
    version='0.1.0',
    packages=get_packages(),
    url='',
    license='BSD3',
    author='Omer Katz',
    author_email='omer.drow@gmail.com',
    description='',
    namespace_packages=['testsuite', 'testsuite.prettyprint'],
    install_requires=['nose2>=0.4.6', 'pygments>=1.6']
)
