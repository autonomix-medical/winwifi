"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import io
import os
import setuptools


here: str = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
f: io.TextIOWrapper
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='winwifi2',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.666',

    description='A Windows Wi-Fi CLI utility',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/changyuheng/winwifi',

    # Author details
    author='Johann Chang',
    author_email='mr.changyuheng@gmail.com',

    # Choose your license
    license='MPL-2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',

        'Environment :: Win32 (MS Windows)',
    ],

    #  # What does your project relate to?
    #  keywords='sample setuptools development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=setuptools.find_packages('src', exclude=['contrib', 'docs', 'tests']),
    package_dir={'': 'src'},

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'comtypes',
        'plumbum',
    ],

    python_requires='>=3.6',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'winwifi': ['data/profile-template.xml'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #  data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'wifi=winwifi.__main__:main',
        ],
    },
)
