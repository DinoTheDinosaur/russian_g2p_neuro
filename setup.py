from setuptools import setup, find_packages

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
        'alabaster==0.7.12',
        'allennlp==0.9.0',
        'argon2-cffi==20.1.0',
        'async-generator==1.10',
        'attrs==20.3.0',
        'Babel==2.9.0',
        'backcall==0.2.0',
        'bleach==3.3.0',
        'blis==0.2.4',
        'boto3==1.17.57',
        'botocore==1.20.57',
        'certifi==2020.12.5',
        'cffi==1.14.5',
        'chardet==4.0.0',
        'click==7.1.2',
        'conllu==1.3.1',
        'cycler==0.10.0',
        'cymem==2.0.5',
        'decorator==5.0.7',
        'defusedxml==0.7.1',
        'docutils==0.16',
        'editdistance==0.5.3',
        'entrypoints==0.3',
        'flaky==3.7.0',
        'Flask==1.1.2',
        'Flask-Cors==3.0.10',
        'ftfy==6.0.1',
        'future==0.18.2',
        'gevent==21.1.2',
        'greenlet==1.0.0',
        'h5py==3.2.1',
        'idna==2.10',
        'imagesize==1.2.0',
        'iniconfig==1.1.1',
        'ipykernel==5.5.3',
        'ipython==7.22.0',
        'ipython-genutils==0.2.0',
        'ipywidgets==7.6.3',
        'itsdangerous==1.1.0',
        'jedi==0.18.0',
        'Jinja2==2.11.3',
        'jmespath==0.10.0',
        'joblib==1.0.1',
        'jsonnet==0.17.0',
        'jsonpickle==2.0.0',
        'jsonschema==3.2.0',
        'jupyter==1.0.0',
        'jupyter-client==6.1.12',
        'jupyter-console==6.4.0',
        'jupyter-core==4.7.1',
        'jupyterlab-pygments==0.1.2',
        'jupyterlab-widgets==1.0.0',
        'kiwisolver==1.3.1',
        'MarkupSafe==1.1.1',
        'matplotlib==3.4.1',
        'mistune==0.8.4',
        'murmurhash==1.0.5',
        'nbclient==0.5.3',
        'nbconvert==6.0.7',
        'nbformat==5.1.3',
        'nest-asyncio==1.5.1',
        'nltk==3.6.2',
        'notebook==6.3.0',
        'numpy==1.20.2',
        'numpydoc==1.1.0',
        'overrides==4.1.2',
        'packaging==20.9',
        'pandas==1.2.4',
        'pandocfilters==1.4.3',
        'parsimonious==0.8.1',
        'parso==0.8.2',
        'pexpect==4.8.0',
        'pickleshare==0.7.5',
        'Pillow==8.2.0',
        'plac==0.9.6',
        'pluggy==0.13.1',
        'preshed==2.0.1',
        'prometheus-client==0.10.1',
        'prompt-toolkit==3.0.18',
        'protobuf==3.15.8',
        'ptyprocess==0.7.0',
        'py==1.10.0',
        'pycparser==2.20',
        'Pygments==2.8.1',
        'pyparsing==2.4.7',
        'pyrsistent==0.17.3',
        'pytest==6.2.3',
        'python-dateutil==2.8.1',
        'pytorch-pretrained-bert==0.6.2',
        'pytorch-transformers==1.1.0',
        'pytz==2021.1',
        'pyzmq==22.0.3',
        'qtconsole==5.0.3',
        'QtPy==1.9.0',
        'regex==2021.4.4',
        'requests==2.25.1',
        'responses==0.13.2',
        'russian-g2p-neuro==1.0.0',
        's3transfer==0.4.2',
        'scikit-learn==0.24.1',
        'scipy==1.6.3',
        'Send2Trash==1.5.0',
        'sentencepiece==0.1.95',
        'six==1.15.0',
        'snowballstemmer==2.1.0',
        'spacy==2.1.9',
        'Sphinx==3.5.4',
        'sphinxcontrib-applehelp==1.0.2',
        'sphinxcontrib-devhelp==1.0.2',
        'sphinxcontrib-htmlhelp==1.0.3',
        'sphinxcontrib-jsmath==1.0.1',
        'sphinxcontrib-qthelp==1.0.3',
        'sphinxcontrib-serializinghtml==1.1.4',
        'sqlparse==0.4.1',
        'srsly==1.0.5',
        'tensorboardX==2.2',
        'terminado==0.9.4',
        'testpath==0.4.4',
        'thinc==7.0.8',
        'threadpoolctl==2.1.0',
        'toml==0.10.2',
        'torch==1.5.0',
        'tornado==6.1',
        'tqdm==4.60.0',
        'traitlets==5.0.5',
        'typing-utils==0.0.3',
        'Unidecode==1.2.0',
        'urllib3==1.26.4',
        'wasabi==0.8.2',
        'wcwidth==0.2.5',
        'webencodings==0.5.1',
        'Werkzeug==1.0.1',
        'widgetsnbextension==3.5.1',
        'word2number==1.1',
        'zope.event==4.5.0',
        'zope.interface==5.4.0'
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
    include_package_data=True,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
)
