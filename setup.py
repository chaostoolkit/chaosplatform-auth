#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
import re
import sys
from os.path import abspath, dirname, join, normpath

from setuptools import find_packages, setup


def get_version_from_package() -> str:
    """
    Read the package version from the source without importing it.
    """
    path = join(dirname(__file__), "chaosplt_auth/__init__.py")
    path = normpath(abspath(path))
    with open(path) as f:
        for line in f:
            if line.startswith("__version__"):
                token, version = line.split(" = ", 1)
                version = version.replace("'", "").strip()
                return version


def read(*names, **kwargs) -> str:
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

setup(
    name='chaosplatform-auth',
    version=get_version_from_package(),
    license='Apache Software License 2.0',
    description='The auth service of the Chaos Platform',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    author='ChaosIQ',
    author_email='contact@chaosiq.io',
    url='https://github.com/chaostoolkit/chaosplatform-auth',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    setup_requires=pytest_runner,
    zip_safe=False,
    python_requires='>=3.6.*',
    project_urls={
        'CI: Travis': 'https://travis-ci.org/chaostoolkit/chaosplatform-auth',
        'Docs: RTD': 'https://docs.chaosplatform.org',
        'GitHub: issues': 'https://chaostoolkit/chaostoolkit/chaosplatform-auth/issues',
        'GitHub: repo': 'https://chaostoolkit/chaostoolkit/chaosplatform-auth'
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    entry_points={
        'console_scripts': [
            'chaosplatform-auth = chaosplt_auth.cli:cli',
        ]
    }
)
