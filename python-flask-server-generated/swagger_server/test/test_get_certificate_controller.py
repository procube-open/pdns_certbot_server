# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestGetCertificateController(BaseTestCase):
    """GetCertificateController integration test stubs"""

    def test_get_certificate(self):
        """Test case for get_certificate

        API that gets server certificate.
        """
        response = self.client.open(
            '/v1/get/{fqdn}'.format(fqdn='fqdn_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
