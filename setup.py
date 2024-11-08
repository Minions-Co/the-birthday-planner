from setuptools import setup, find_packages

setup(
    name='personal_assistant',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'assistant=personal_assistant.main:main',
        ],
    },
    install_requires=[
        'python-dateutil',
    ],
    description='The Ultimate Birthday Planner!',
    author='Minions Co.',
    author_email='dev@minions.co',
)
