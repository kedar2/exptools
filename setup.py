from setuptools import setup

INSTALL_REQUIRES = [
    'pandas',
    'submitit'
]

setup(
    name='exptools',
    version='0.0.1',
    description='Experiment tools',
    install_requires=INSTALL_REQUIRES,
)