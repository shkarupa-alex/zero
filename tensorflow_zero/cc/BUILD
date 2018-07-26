package(default_visibility = ["//visibility:public"])

load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_gen_op_libs")
load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_custom_op_library")


cc_library(
    name = "cc",
    deps = [
        ":zero_out_op_lib",
    ],
    # alwayslink = 1,
)

tf_gen_op_libs(
    op_lib_names = ["zero_out"],
    deps = [
        "//tensorflow_zero/cc/kernels:zero_out",
        "@org_tensorflow//tensorflow/core:lib",
    ],
)

tf_custom_op_library(
    name = "ops/_tensorflow_zero.so",
    srcs = [
        ":ops/zero_out.cc",
    ],
    deps = [
        "//tensorflow_zero/cc/kernels:zero_out",
    ],
)