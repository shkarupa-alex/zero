package(
    default_visibility = ["//tensorflow_zero:__subpackages__"],
)

load("//tensorflow_zero:zero.bzl", "rpath_linkopts")
load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_kernel_library")

tf_kernel_library(
    name = "zero_out",
    srcs = ["zero_out.cc"],
    deps = [
        "@org_tensorflow//tensorflow/core:framework_headers_lib",
        "@org_tensorflow//tensorflow/core:framework_lite",
        "@protobuf_archive//:protobuf",
    ],
    alwayslink = 1,
)