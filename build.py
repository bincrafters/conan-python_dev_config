#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_header_only
import os

if __name__ == "__main__":

    builder = build_template_header_only.get_builder()
    
    updated_settings={
        'arch':os.getenv('conan_archs')
    }
    
    updated_options={
        "python_dev_config:python" : os.getenv("conan_python_path", "python"),
    }
           

    updated_builds = []

    for settings, options, env_vars, build_requires, reference in builder.items:
         updated_builds.append([updated_settings, updated_options, env_vars, build_requires])
    
    builder.builds = updated_builds    
    
    builder.run()
