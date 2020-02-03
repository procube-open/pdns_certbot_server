# coding: utf-8

from setuptools import find_packages, setup

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="REST powerdns certbot",
    author_email="mitsuru@procube.jp",
    url="",
    keywords=["Swagger", "REST powerdns certbot"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Get a server certificate by let&#x27;s encrypt and distribute.\
    It will be certified by let&#x27;s encrypt by connecting PowerDNS API defined in environment variable \
    CERTBOT_PDNS_BASEURL using environment variable CERTBOT_PDNS_API_KEY.\
    It creates let&#x27;s encrypt account using e-mail address defined in environment variable CERTBOT_EMAIL. \
    When renew API is called, it renew certificate.
    """
)
