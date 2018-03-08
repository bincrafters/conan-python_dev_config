#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_header_only
import os

if __name__ == "__main__":
    builder = build_template_header_only.get_builder()
    builder.builds = []
    options = dict(map(lambda o: o.split('='), os.getenv('CONAN_OPTIONS').split(';'))) if os.getenv('CONAN_OPTIONS', None) else None
    archs = os.getenv('CONAN_ARCHS','').split(',')
    if archs and len(archs) > 0:
        for arch in archs:
            builder.add({'arch':arch},options=options)
    else:
        builder.add(options=options)
    builder.run()
