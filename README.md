# tensorflow-zero

Demo repository with infrastructure to build [Tensorflow custom OP](https://www.tensorflow.org/extend/adding_an_op)


bazel build //pip_package
bazel-bin/pip_package/pip_package ~/wheels

bazel build //tensorflow_zero/...
bazel test //tensorflow_zero/...



bazel clean --expunge
bazel build tools/pip_package
bazel-bin/tools/pip_package/pip_package

bazel test //tensorflow_zero/...