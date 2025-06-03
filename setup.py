from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    description='A package for phishing detection and analysis',
    author='Akshay',
    author_email='akshayfracis891@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'pymongo',
        'python-dotenv'
    ],
    python_requires='>=3.7',
)