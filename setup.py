#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
      entry_points={
          'napari.plugin': [
              'napari-stl-exporter = napari_stl_exporter',
              ],
          }
      )
