from setuptools import setup, find_packages
from os import path

setup(
    name='russian_g2p_neuro',

    version='1.0.0',

    description='G2P tool for Russian language with vosk-model-ru styled transcriptions',
    
    # The project's main homepage.
    url='https://github.com/DinoTheDinosaur/russian_g2p_neuro',

    # Author details
    author='DinoTheDinosaur',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: System :: Networking',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Operating System :: POSIX :: Linux',


        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='ASR speech recognition g2p russian grapheme-to-phoneme',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
    scripts=['bin/generate_transcriptions'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'torch==1.5.0', 'allennlp==0.9.0'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'model': [
            'weights.th', 'tokens.txt',
            'non_padded_namespaces.txt',
            'target_tokens.txt'
        ]
    },
    data_files=[
        ('model', ['model/weights.th']),
        ('model/vocabulary/', ['model/vocabulary/tokens.txt']),
        ('model/vocabulary/', ['model/vocabulary/target_tokens.txt']),
        ('model/vocabulary/', ['model/vocabulary/non_padded_namespaces.txt']),
    ],
    include_package_data = True,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
)