from setuptools import setup, find_packages

setup(
    name='human',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='creator',
    author_email='seasonluke@gmail.com',
    description='Human',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/spoonbobo/human',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)