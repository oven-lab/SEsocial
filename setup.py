from setuptools import find_packages, setup
setup(
    name='SE_social',
    packages=find_packages(include=['sesocial']),
    version='0.2.0',
    description='A python library for verifying swedish social security numbers',
    author='WBDVP',
    license='MIT',
    classifiers=[
    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
)