from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Otto Aulicino",
    author_email="otto.aulicino@gmail.com",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 Snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/oaulicino/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scrypts]
    shotty=shotty.shotty:cli
    ''',
)
