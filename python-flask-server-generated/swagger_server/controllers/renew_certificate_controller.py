import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util


def renew():  # noqa: E501
    """サーバ証明書を更新する

    取得済みの証明書の期限切れをチェックし、期限切れが 近いものを更新するAPIである。クロックデーモンにより、 定期的に呼び出されることを前提としている。  # noqa: E501


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
