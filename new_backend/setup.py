from setuptools import setup, find_packages

def read_requirements(file_path:str):
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements


setup(
    name='ses_backend',
    version='1.0.0',
    description='backend for smart enrollment system',
    author='hiram',
    author_email='hiram.artnak@gmail.com',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    classifiers=[],
    entry_points={
        'console_scripts': [
            'ses_backend = ses_backend.api.__main__:main'
        ]
    }
)
