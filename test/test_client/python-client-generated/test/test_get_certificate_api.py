# coding: utf-8

"""
    REST powerdns certbot

    Get a server certificate by let's encrypt and distribute. It will be certified by let's encrypt by connecting PowerDNS API defined in environment variable CERTBOT_PDNS_BASE_URL using environment variable CERTBOT_PDNS_API_KEY. It creates let's encrypt account using e-mail address defined in environment variable CERTBOT_EMAIL. When renew API is called, it renew certificate.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mitsuru@procube.jp
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

from OpenSSL.crypto import load_certificate, FILETYPE_PEM

import datetime
import unittest
import sys
import pathlib
import json
import os
import sys

# absolute path of dir which this code exists
current_dir = pathlib.Path(__file__).resolve().parent
# append path to find module
sys.path.append(str(current_dir) + '/../')

# import swagger_client
from swagger_client.api.get_certificate_api import GetCertificateApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGetCertificateApi(unittest.TestCase):
    """GetCertificateApi unit test stubs"""

    def setUp(self):
        self.api = GetCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_certificate(self):
        """Test case for get_certificate

        API that gets certificate.  # noqa: E501
        """

        """ Test case should be checked
        ## Test 1 --- get new certificate when file doesn't exist.
        ## Test 2 --- can get file when file exists.
        ## Test 3 --- renew certificate when it expires in 30 days(do nothing if it is false).
        """ 

        # fqdn
        fqdn = 'www.pdns.procube-demo.jp'

        # certificate got by API
        try:
            target_Certificate = self.api.get_certificate(fqdn)

            # load certificate by OPENSSL
            test_Certificate = load_certificate(FILETYPE_PEM, target_Certificate.cert)

            # contents of certificate
            print("version : " + str(test_Certificate.get_version()))
            print("serial number : " + str(test_Certificate.get_serial_number()))
            print("algorithm : " + str(test_Certificate.get_signature_algorithm()))
            print("name : " + str(test_Certificate.get_issuer().commonName))
            print("begin date : " + str(test_Certificate.get_notBefore()))
            print("expire date : " + str(test_Certificate.get_notAfter()))
            print("subject : "+ str(test_Certificate.get_subject().commonName))
            print("public key : " + str(test_Certificate.get_pubkey()))

            # unittest
            self.assertEqual(fqdn, test_Certificate.get_subject().commonName)
            notAfter = test_Certificate.get_notAfter().decode('utf-8')
            end_date = datetime.datetime(int(notAfter[0:4]), int(notAfter[4:6]), int(notAfter[6:8]), int(notAfter[8:10]), int(notAfter[10:12]), int(notAfter[12:14]))
            self.assertTrue(datetime.datetime.today() < end_date)

        except ApiException as e:
            error = self.api.api_client.deserialize(e, 'Error')
            print(error.message)

if __name__ == '__main__':
    unittest.main()
