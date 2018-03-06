#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_header_only
import os

if __name__ == "__main__":
    builder = build_template_header_only.get_builder()
    builder.builds = []
    options = dict(map(lambda o: o.split('='), os.getenv('CONAN_OPTIONS').split(';'))) if os.getenv('CONAN_OPTIONS', None) else None
    builder.add(options=options)
    builder.run()
