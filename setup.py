from setuptools import Extension, setup

extensions = [Extension("audioop", ["audioop.c"])]

setup(name="py-audioop", ext_modules=extensions)
