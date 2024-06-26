from setuptools import find_packages, setup

setup(
    name='pipelinechain',
    packages=find_packages(),
    version='1.0.1',
    description='A library that implements the Chain of Responsibility pattern.',
    author='Matthew Batchelder',
    author_email='borkweb@gmail.com',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
