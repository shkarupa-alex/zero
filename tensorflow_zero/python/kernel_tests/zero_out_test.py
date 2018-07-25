from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_zero import zero_out
import tensorflow as tf


class ZeroOutTest(tf.test.TestCase):
    def testZeroOut(self):
        with self.test_session():
            result = zero_out([5, 4, 3, 2, 1])
            self.assertAllEqual(result.eval(), [5, 0, 0, 0, 0])


if __name__ == "__main__":
    tf.test.main()
