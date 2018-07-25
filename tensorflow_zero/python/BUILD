package(default_visibility = ["//tensorflow_zero:__subpackages__"])

load("//tensorflow_zero:zero.bzl", "rpath_linkopts")
load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_gen_op_wrapper_py")
load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_custom_op_py_library")


tf_custom_op_py_library(
    name = "zero_ops_py",
    srcs = [
        "ops/zero_ops.py",
    ],
    dso = [
        "//tensorflow_zero/cc:ops/_zero_ops.so",
    ],
    kernels = [
        "//tensorflow_zero/cc:zero_ops",
        "//tensorflow_zero/cc/kernels:zero_out_kernels",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":zero_out_py_wrapper",
        "@org_tensorflow//tensorflow:tensorflow_py",
        "@org_tensorflow//tensorflow/python:framework_for_generated_wrappers",
    ],
)

tf_gen_op_wrapper_py(
    name = "zero_out_py_wrapper",
    out = "ops/gen_zero_out.py",
    cc_linkopts = rpath_linkopts("zero_out_py_wrapper"),
    hidden = [],
    deps = [
        "//tensorflow_zero/cc:zero_out_op_lib",
    ],
)