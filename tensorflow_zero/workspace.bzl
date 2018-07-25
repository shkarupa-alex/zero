load("@org_tensorflow//tensorflow:workspace.bzl", "tf_workspace")

def tf_zero_workspace():
  tf_workspace(path_prefix = "", tf_repo_name = "org_tensorflow")

