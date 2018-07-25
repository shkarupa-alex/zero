from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
from sys import version

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install as InstallCommandBase
from setuptools.dist import Distribution

import warnings


__version__ = '0.9.6'


REQUIRED_PACKAGES = [
    'six >= 1.10.0',
    'protobuf >= 3.4.0',
]


if '--gpu' in sys.argv:
  use_gpu = True
  sys.argv.remove('--gpu')
else:
  use_gpu = False


if use_gpu:
  project_name = 'tensorflow-zero-gpu'
  REQUIRED_PACKAGES.append('tensorflow-gpu==1.5.0')
else:
  project_name = 'tensorflow-zero'
  REQUIRED_PACKAGES.append('tensorflow==1.5.0')


class BinaryDistribution(Distribution):
  """This class is needed in order to create OS specific wheels."""
  def has_ext_modules(self):
    return True


warnings.warn('tensorflow-zero is likley to fail when building from a '
              'source distribution (sdist). Please follow instructions in '
              '(https://github.com/tensorflow/zero/INSTALL.md) '
              'to build this from the source.')


setup(
    name=project_name,
    version=__version__,
    description=('TensorFlow zero provides zero models in TensorFlow'),
    long_description='',
    url='https://github.com/tensorflow/zero',
    author='Google Inc.',
    author_email='tensorflow-zero-releasing@google.com',
    # Contained modules and scripts.
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    # Add in any packaged data.
    include_package_data=True,
    package_data={'': ['*.so']},
    exclude_package_data={'': ['BUILD', '*.h', '*.cc']},
    zip_safe=False,
    distclass=BinaryDistribution,
    cmdclass={
        'pip_pkg': InstallCommandBase,
    },
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        ],
    license='Apache 2.0',
    keywords='zero tensorflow tensor machine learning',
)
