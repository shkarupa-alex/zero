from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, find_packages
from setuptools.dist import Distribution

import warnings

__version__ = '0.0.4'


class BinaryDistribution(Distribution):
    """This class is needed in order to create OS specific wheels."""

    def has_ext_modules(self):
        return True


warnings.warn('tensorflow-zero will fail when building from a source distribution (sdist). Please follow  instructions '
              'in (https://github.com/shkarupa-alex/zero/README.md) to build this from the source.')

setup(
    name='tensorflow-zero',
    version=__version__,
    description='TensorFlow op that takes a tensor of int32s '
                'and outputs a copy with all but the first element set to zero',
    url='https://github.com/shkarupa-alex/zero',
    author='Shkarupa Alex',
    author_email='shkarupa.alex@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=1.8.0',
    ],
    include_package_data=True,
    package_data={'': ['*.so']},
    exclude_package_data={'': ['BUILD', '*.h', '*.cc']},
    zip_safe=False,
    distclass=BinaryDistribution,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='tensorflow custom op',
)
