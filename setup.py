from setuptools import find_packages, setup

setup(
    name='py-nobitex-api',
    version='1.0.0',
    license="MIT",
    description='simple nobitex api module',
    author='Hmohammad2520',
    author_email='Hmohammad2520@gmail.com',
    url='https://github.com/Hmohammad2520/py-nobitex-api',
    install_requires=[
        'requests==2.32.3',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)