#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
      entry_points={'napari.plugin': 'plugin-name = napari-stl-exporter.napari_stl_exporter'}
      )
