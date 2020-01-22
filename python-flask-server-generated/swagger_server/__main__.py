#!/usr/bin/env python3

import json
import os

import connexion

from swagger_server import encoder


def main():
    certbot_pdns_config = {
        'api-key': os.environ["CERTBOT_PDNS_API_KEY"],
        'base-url': os.environ["CERTBOT_PDNS_BASE_URL"],
        'axfr-time': 5
    }
    with open('/etc/letsencrypt/certbot-pdns.json', 'w') as config_file:
        json.dump(certbot_pdns_config, config_file)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'REST powerdns certbot'},
                pythonic_params=True)
    app.run(port=8080, debug=False, threaded=False)  # modified


if __name__ == '__main__':
    main()
