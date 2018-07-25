package(
    default_visibility = ["//tensorflow_zero:__subpackages__"],
)

load(
    "//tensorflow_zero:zero.bzl",
    "rpath_linkopts",
)
load(
    "@org_tensorflow//tensorflow:tensorflow.bzl",
    "tf_custom_op_library",
    "tf_gen_op_libs",
)


tf_custom_op_library(
    name = "ops/_zero_ops.so",
    srcs = [
        ":ops/zero_out.cc",
    ],
    linkopts = rpath_linkopts("ops/_zero_ops.so"),
    deps = [
        "//tensorflow_zero/cc/kernels:zero_out",
    ],
)

cc_library(
    name = "zero_ops",
    deps = [
        ":zero_out_op_lib",
    ],
    alwayslink = 1,
)

tf_gen_op_libs(
    op_lib_names = ["zero_out"],
    deps = [
        "//tensorflow_zero/cc/kernels:zero_out",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)