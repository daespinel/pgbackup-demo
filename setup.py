from setuptools import find_packages, setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='David Espinel',
    author_email='dafespinelsa@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/linusacademy/pgbackup',
    packages=find_packages('src')
)