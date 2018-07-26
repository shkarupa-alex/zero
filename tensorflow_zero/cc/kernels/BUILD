package(default_visibility = ["//visibility:public"])

load("@org_tensorflow//tensorflow:tensorflow.bzl", "tf_kernel_library")


tf_kernel_library(
    name = "zero_out",
    srcs = ["zero_out.cc"],
    hdrs = [],
    deps = [
        "@org_tensorflow//tensorflow/core:framework_headers_lib",
        "@org_tensorflow//tensorflow/core:framework_lite",
        "@protobuf_archive//:protobuf",
    ],
)