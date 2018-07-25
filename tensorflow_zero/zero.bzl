# -*- Python -*-

def _add_tf_search_path(prefix, levels_to_root):
  root = "%s/%s" % (prefix, "/".join([".."] * (levels_to_root + 1)))
  tf_root = "%s/external/org_tensorflow/tensorflow" % root
  return "-rpath,%s" % tf_root

def rpath_linkopts(name):
  """Add proper rpath_linkopts to the build rule.

  This function adds tensorflow root to rpath for Darwin builds.

  Args:
    name: Name of the target.

  Returns:
    rpath linker options.
  """
  levels_to_root = PACKAGE_NAME.count("/") + name.count("/")
  return select({
      "@org_tensorflow//tensorflow:darwin": [
          "-Wl,%s" % (_add_tf_search_path("@loader_path", levels_to_root),),
      ],
      "//conditions:default": [
      ],
  })
