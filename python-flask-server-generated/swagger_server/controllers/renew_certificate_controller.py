import connexion
import six
import subprocess

from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util
from swagger_server.controllers import LOCK, logger


def renew():  # noqa: E501
    """renew server certificate

    API that renew certificate which is about to expire. This should be called regularly by clock daemon.  # noqa: E501


    :rtype: None
    """
    with LOCK:
        try:
            error_message = Error()
            args = ['certbot', 'renew']
            proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # noqa: E501
            logger.info(f'{proc.stdout.decode()}')
            if proc.returncode != 0:
                logger.error(f'error occur in certbot renew: {proc.stderr.decode()}')  # noqa: E501
                error_message.message = f'error occur in certbot renew: {proc.stderr.decode()}'  # noqa: E501

                return error_message, 500 + int(proc.returncode)
            error_message.message = f'{proc.stdout.decode()}'
            return error_message, 200
        except Exception as e:
            logger.exception(e)
            error_message.message = e
            return error_message, 501

