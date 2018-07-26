package(default_visibility = ["//visibility:public"])

load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_custom_op_py_library", "tf_gen_op_wrapper_py")


py_library(
    name = "python",
    srcs = ["__init__.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":ops_py_library",
    ],
)


tf_custom_op_py_library(
    name = "ops_py_library",
    srcs = ["ops.py"],
    dso = ["//tensorflow_zero/cc:ops/_tensorflow_zero.so"],
    kernels = ["//tensorflow_zero/cc/kernels"],
    srcs_version = "PY2AND3",
    deps = [
        ":ops_py_wrapper",
        "@org_tensorflow//tensorflow:tensorflow_py",
        "@org_tensorflow//tensorflow/python:framework_for_generated_wrappers",
    ],
)


tf_gen_op_wrapper_py(
    name = "ops_py_wrapper",
    out = "_gen.py",
    deps = [
        "//tensorflow_zero/cc",
    ],
)
