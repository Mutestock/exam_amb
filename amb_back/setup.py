from setuptools import setup

setup(
    name='amb',
    version='0.0.1',
    py_modules=['main'], 
    description="",
    install_requires=[
        'Click',
        'Flask',
        'flask-restplus',
        'configparser',
        'SQLAlchemy',
        'nose2'
    ],
    author="mute",
    entry_points='''
        [console_scripts]
        amb=cli:amb
    '''
)