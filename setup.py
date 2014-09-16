from setuptools import setup


def desc():
    with open("README.md") as f:
        return f.read()


setup(
    name='frasco-subdomains',
    version='0.1',
    url='http://github.com/frascoweb/frasco-subdomains',
    license='MIT',
    author='Maxime Bouroumeau-Fuseau',
    author_email='maxime.bouroumeau@gmail.com',
    description="Subdomains awareness for Frasco",
    long_description=desc(),
    py_modules=['frasco_subdomains'],
    platforms='any',
    install_requires=[
        'frasco'
    ]
)