#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")


name = "unitPy2"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("mockito")