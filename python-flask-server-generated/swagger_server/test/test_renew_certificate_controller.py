# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestRenewCertificateController(BaseTestCase):
    """RenewCertificateController integration test stubs"""

    def test_renew(self):
        """Test case for renew

        サーバ証明書を更新する
        """
        response = self.client.open(
            '/v1/renew',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
