# tensorflow-zero

Demo repository with infrastructure to build wheel for [Tensorflow custom OP](https://www.tensorflow.org/extend/adding_an_op)

## Develop commands

```bash
bazel build //tensorflow_zero/...
bazel test //tensorflow_zero/...
```

## Build commands

```bash
bazel clean --expunge
bazel build //pip_package
bazel-bin/pip_package/pip_package ~/wheels
```
