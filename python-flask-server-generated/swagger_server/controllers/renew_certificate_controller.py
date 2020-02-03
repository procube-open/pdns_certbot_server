import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def renew():  # noqa: E501
    """renew server certificate

    API that renew certificate which is about to expire. This should be called regularly by clock daemon.  # noqa: E501


    :rtype: None
    """
    try:
        error = certbot_main.main(['renew'])
        if error:
            logger.error(f'error occuer in certbot renew: {error}')
        else:
            pass # TODO : research what to do.
    except Exception as e:
        logger.exception(e)
