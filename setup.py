from setuptools import setup

setup(
    name='fast.com',
    version='1.0.2',
    description='fast.com speedtest cli',
    url='https://github.com/banteg/fast',
    author='banteg',
    licence='MIT',
    py_modules=['fast'],
    install_requires=['aiohttp'],
    entry_points={
        'console_scripts': [
            'fast=fast:main',
        ]
    }
)
