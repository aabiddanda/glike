from setuptools import dist, setup, Extension

dist.Distribution().fetch_build_eggs(["numpy>=1.14.5"])

import numpy as np 

setup_args = dict(
    ext_modules = [
        Extension(
            'npe',
            ['src/npe.c'],
            include_dirs = [np.get_include()],
            py_limited_api = True
        )
    ]
)
setup(**setup_args)
