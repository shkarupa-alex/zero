from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_zero.python._gen import zero_out
from tensorflow.python.framework import load_library, ops
from tensorflow.python.platform import resource_loader
import os

_zero_ops_lib = load_library.load_op_library(resource_loader.get_path_to_datafile(
    os.path.join('..', 'cc', 'ops', '_tensorflow_zero.so')))

ops.NotDifferentiable("ZeroOut")
