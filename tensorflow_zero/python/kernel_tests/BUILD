licenses(["notice"])  # Apache 2.0

package(
    default_visibility = [
        "//tensorflow_zero:__subpackages__",
    ],
)

py_test(
    name = "zero_out_test",
    size = "medium",
    srcs = ["zero_out_test.py"],
    srcs_version = "PY2AND3",
    deps = [
        "@org_tensorflow//tensorflow:tensorflow_py",
        "//tensorflow_zero/python:zero_ops_py",
    ],
)