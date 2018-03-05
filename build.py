#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_header_only


if __name__ == "__main__":
    builder = build_template_header_only.get_builder()
    options = dict(map(lambda o: o.split('='), os.environ['CONAN_OPTIONS'].split(';')))
    builder.add(options=options)
    builder.run()
