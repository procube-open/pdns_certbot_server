import datetime
import logging
import os
import pathlib
import subprocess
import sys
import threading

# absolute path of dir which this code exists
current_dir = pathlib.Path(__file__).resolve().parent
# append path to find module
sys.path.append(str(current_dir) + '/../')

from models.certificate import Certificate  # noqa: E501
from models.error import Error  # noqa: E501

LOCK = threading.Lock()


def get_certificate(fqdn):  # noqa: E501
    """API that get server certificate

    server certificate of the domain which specified in fqdn.  # noqa: E501

    :param fqdn: FQDN of certificate to get
    :type fqdn: str

    :rtype: Certificate
    """
    with LOCK:
        try:
            target_Certificate = Certificate()
            error_message = Error()

            logger = logging.getLogger("LOG")
            handler = logging.StreamHandler()
            logger.addHandler(handler)

            # path
            cert_path = '/etc/letsencrypt/live/' + fqdn + '/cert.pem'
            fullchain_path = '/etc/letsencrypt/live/' + fqdn + '/fullchain.pem'
            key_path = '/etc/letsencrypt/live/' + fqdn + '/privkey.pem'

            # get certificate if not exist
            if not os.path.exists('/etc/letsencrypt/live/' + fqdn):
                args = ['certbot', '--agree-tos', '--text', '--renew-by-default',
                        '-n', '--no-eff-email', '--authenticator',
                        'certbot-pdns:auth', 'certonly', '-d', fqdn]
                if 'CERTBOT_EMAIL' in os.environ:
                    args += ['-m', os.environ['CERTBOT_EMAIL']]
                proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # noqa: E501
                logger.info(f'{proc.stdout.decode()}')
                if proc.returncode != 0:
                    logger.error(f'error occur in certbot new: {proc.stderr.decode()}')  # noqa: E501
                    error_message.message = f'error occur in certbot new: {proc.stderr.decode()}'  # noqa: E501

                    return error_message, 500 + int(proc.returncode)

            # get certificate and assign value
            with open(cert_path, 'r') as cert_file:
                cert = cert_file.read()
                target_Certificate.cert = cert

            with open(fullchain_path, 'r') as fullchain_file:
                fullchain = fullchain_file.read()
                target_Certificate.fullchain = fullchain

            with open(key_path, 'r') as key_file:
                privkey = key_file.read()
                target_Certificate.privkey = privkey

            mtime = datetime.datetime.fromtimestamp(os.stat(cert_path).st_mtime)
            target_Certificate.mtime = mtime

            return target_Certificate

        except Exception as e:
            logger.exception(e)
            error_message.message = e
            return error_message, 501
