# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages
from src.hatak import VERSION

install_requires = [
    'bael.project==0.1.1',
    'pyramid',
]


if __name__ == '__main__':
    setup(
        name='hatak',
        version=VERSION,
        description='Small Pyramid extension/project managment',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        namespace_packages=['bael'],
        zip_safe=False,
        package_data={
            '': [
                'hatak/templates/*.ini',
                'hatak/templates/*.tpl',
                'hatak/templates/project/*.tpl'],
        },
        entry_points="""\
          [console_scripts]
              hatak = bael.hatak.recipe:run
        """,
        )
