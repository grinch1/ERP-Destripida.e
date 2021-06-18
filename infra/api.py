import logging
import requests

logger = logging.getLogger(__name__)


class Api(object):

    def __init__(self, api_key):

        self.api_key = api_key
        self.root_uri = 'https://bling.com.br/Api/v2'
        self.session = requests.Session()

    def get_products(
        self, creation_date=None, modification_date=None,
        store_creation_date=None, store_modification_date=None,
        type=None, situation=None, stock='S', image='N', store_code=None
    ):
        filters = []
        params = dict()

        if creation_date:
            filter = 'dataInclusao[{} TO {}]'.format(
                creation_date[0], creation_date[1]
            )
            filters.append(filter)

        if modification_date:
            filter = 'dataAlteracao[{} TO {}]'.format(
                modification_date[0], modification_date[1]
            )
            filters.append(filter)

        if store_creation_date:
            filter = 'dataInclusaoLoja[{} TO {}]'.format(
                store_creation_date[0], store_creation_date[1]
            )
            filters.append(filter)

        if store_modification_date:
            filter = 'dataAlteracaoLoja[{} TO {}]'.format(
                store_modification_date[0], store_modification_date[1]
            )
            filters.append(filter)

        if type:
            filter = 'tipo[{}]'.format(type)
            filters.append(filter)

        if situation:
            filter = 'situacao[{}]'.format(situation)
            filters.append(filter)

        params['estoque'] = stock
        params['imagem'] = image

        if store_code:
            params['loja'] = store_code

        if len(filters):
            filters_value = ';'.join(filters)
            params['filters'] = filters_value

        return self._get_objects('produtos', 'produto', params)

    def get_order(self, number):
        uri = '/pedido/{}'.format(number)
        resp = self._make_request('GET', uri)
        return resp['retorno']['pedidos'][0]['pedido']

    def get_orders(
        self, issued_date=None, change_date=None, expected_date=None,
        situation_id=None, contact_id=None
    ):
        filters = []
        params = {}

        if issued_date:
            filter = 'dataEmissao[{} TO {}]'.format(
                issued_date[0], issued_date[1]
            )
            filters.append(filter)

        if change_date:
            filter = 'dataAlteracao[{} TO {}]'.format(
                change_date[0], change_date[1]
            )
            filters.append(filter)

        if expected_date:
            filter = 'dataPrevista[{} TO {}]'.format(
                expected_date[0], expected_date[1]
            )
            filters.append(filter)

        if situation_id:
            filter = 'idSituacao[{}]'.format(situation_id)
            filters.append(filter)

        if contact_id:
            filter = 'idContato[{}]'.format(contact_id)
            filters.append(filter)

        if len(filters):
            filters_value = ';'.join(filters)
            params = {'filters': filters_value}

        return self._get_objects('pedidos', 'pedido', params)

    def get_product(self, sku):
        uri = '/produto/{}'.format(sku)
        resp = self._make_request('GET', uri)
        return resp['retorno']['produtos'][0]['produto']

    def _get_objects(self, resource, root_elem, params=None):
        objs = []
        page = 1

        while True:
            try:
                uri = '/{}/page={}'.format(resource, page)
                resp = self._make_request('GET', uri, params=params)
                items = resp['retorno'][resource]
                for item in items:
                    objs.append(item[root_elem])
                page += 1
            except KeyError:
                break

        return objs

    def _make_request(self, method, uri, params=None, data=None):
        logger.info('method = {}'.format(method))
        logger.info('uri = {}'.format(uri))
        logger.info('params = {}'.format(params))
        logger.info('data = {}'.format(data))
        url = '{}{}/json/?apikey={}'.format(self.root_uri, uri, self.api_key)
        logger.info('url = {}'.format(url))
        try:
            resp = self.session.request(method, url, data=data, params=params)
            logger.debug(resp)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as e:
            raise ApiError(e.request, e.response)
        except requests.exceptions.RequestException as e:
            raise ApiError(e.request)


class ApiError(Exception):
    def __init__(self, request, response=None):
        self.request = request
        self.response = response
