from setuptools import setup

setup(
    name='Test',
    version='1.0',
    py_modules=['test'],
    entry_points='''
        [console_scripts]
        test=test:main
    '''
)