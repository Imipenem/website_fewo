import os
from setuptools import find_packages, setup

import website_fewo as module

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


setup(
    name=module.__name__.replace("_", "-"),
    version='1.0.0',
    description="Website FewoRhein",
    long_description=readme,
    platforms="all",
    license=license,
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    zip_safe=False,
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__),
            'templates', 'static'
        ),
    },
    entry_points={
        'console_scripts': [
            'website_fewo = {}.server:main'.format(module.__name__),
        ]
    },
    install_requires=required,
)