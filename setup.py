from setuptools import setup, find_packages
requires = [
    'robotframework',
    'robotframework-ride',
    'robotframework-selenium2library',
    'pywin32',
    'openpyxl',
    'requests',
    'bs4',
]

setup(
name='rpa',
install_requires=requires,
package_dir={'': 'src'},
packages=find_packages('src'),
version='0.0.1',
zip_safe=False,
package_data={'': ['NOTICE']},
    include_package_data=True,
    url="",
)