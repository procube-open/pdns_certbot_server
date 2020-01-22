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
    let&#x27;s encrypt でサーバ証明書を取得し配布する。 環境変数\
    CERTBOT_PDNS_BASE_URL に指定された URL   に対して\
    CERTBOT_PDNS_API_KEY に指定された API 鍵で PowerDNS の\
    API に接続して letsencrpt の認証を受ける。 認証時は CERTBOT_EMAIL\
    に指定したメールアドレスで lets encrypt のアカウントを作成する。 \
    また、 renew API が呼び出されると取得した証明書を更新する。
    """
)
