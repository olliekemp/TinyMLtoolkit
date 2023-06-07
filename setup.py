from setuptools import setup

setup(
    name='tinymltoolkit',
    version='0.1',
    description='Functions to train and compress neural networks',
    author='Ollie Kemp',
    packages = setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
