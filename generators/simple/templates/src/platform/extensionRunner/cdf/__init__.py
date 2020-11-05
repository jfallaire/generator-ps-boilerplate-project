# no modules depend on distribution_framework, but it contains types that may be returned by CMF such as
# generic exceptions and stuff. if it's not imported, it cannot be discovered, so we'll force it.

try:
    from . import distribution_framework
except ImportError:
    ...  # this might happen when regenerating the code from scratch, since the code generator imports root module
