from setuptools import setup, find_packages
import re

setup(
    name='speechdiarization',
    version='0.0.1',
    description="Speech Diarization",
    classifiers=[],
    keywords='',
    author='Bryony Buck',
    author_email='?@gmail.com',
    url='https://github.com/bryb31/speech-diarization',
    license='',
    packages=find_packages(exclude=['ez_setup', 'test']),
    package_data={
      'speechdiariaztion': []
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # specify your requirements here:
        'pyannote.audio==1.1',
    ],
    extras_require={
        'dev': [
            'flake8',
            'coverage',
            'pytest',
            'pytest-cov',
        ]
    },
    entry_points={
        'console_scripts': [
            'speech = speechdiarization.main:print_hi',
            ]
        },
)