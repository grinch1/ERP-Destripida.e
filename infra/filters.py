from datetime import datetime

def filter_product(product):
		product['id'] = int(product['id'])
		if product['idFabricante'] != '':
			product['idFabricante'] = int(product['idFabricante'])
		product.pop('tipo')
		product.pop('descricaoCurta')
		product.pop('descricaoComplementar')
		product.pop('imageThumbnail')
		product.pop('urlVideo')
		product.pop('codigoFabricante')
		product.pop('class_fiscal')
		product.pop('cest')
		product.pop('origem')
		product.pop('idGrupoProduto')
		product.pop('linkExterno')
		product.pop('observacoes')
		product.pop('grupoProduto')
		product.pop('garantia')
		product.pop('descricaoFornecedor')
		product.pop('categoria')
		product.pop('pesoLiq')
		product.pop('pesoBruto')
		product.pop('gtin')
		product.pop('gtinEmbalagem')
		product.pop('larguraProduto')
		product.pop('alturaProduto')
		product.pop('profundidadeProduto')
		product.pop('unidadeMedida')
		product.pop('itensPorCaixa')
		product.pop('volumes')
		product.pop('localizacao')
		product.pop('crossdocking')
		product.pop('condicao')
		product.pop('producao')
		product.pop('freteGratis')
		if 'producao' in product:
			product.pop('producao')
		product.pop('dataValidade')
		product.pop('spedTipoItem')
		product.pop('depositos')
		emin = float(product['estoqueMinimo'])
		emax = float(product['estoqueMaximo'])
		product['estoqueMinimo'] = int(emin)
		product['estoqueMaximo'] = int(emax)
		product['preco'] = float(product['preco'])
		if product['precoCusto'] is None:
			product['precoCusto'] = 0.00
		else:
			product['precoCusto'] = float(product['precoCusto'])
		return product

def filter_client(client):
	client['cpf'] = client['cnpj']
	client['id'] = int(client['id'])
	client.pop('cnpj')
	client.pop('ie')

def filter_item(item):
	item["quantidade"] = float(item["quantidade"])
	item["quantidade"] = int(item["quantidade"])
	item["valorunidade"] = float(item["valorunidade"])
	if item['precocusto'] == None:
		item["precocusto"] = 0.0
	item["precocusto"] = float(item["precocusto"])
	item["descontoItem"] = float(item["descontoItem"])

	item.pop('pesoBruto')
	item.pop('largura')
	item.pop('altura')
	item.pop('profundidade')
	item.pop('descricaoDetalhada')
	item.pop('unidadeMedida')
	item.pop('gtin')
	return item

def filter_order(order):
	if order['desconto'][-1:] == '%':
		order['desconto'] = order['desconto'][0:-1]
	order['desconto'] = order['desconto'].replace(',', '.')
	order['desconto'] = float(order['desconto'])

	order['valorfrete'] = float(order['valorfrete'])
	order['totalprodutos'] = float(order['totalprodutos'])
	order['totalvenda'] = float(order['totalvenda'])

	order['numero'] = int(order['numero'])
	order.pop('observacoes')
	order.pop('observacaointerna')
	order.pop('numeroOrdemCompra')
	order.pop('parcelas')
	if 'pagamento' in order:
		order.pop('pagamento')
	return order

def filter_account(account):
	if account['situacao'] == 'pago':
		return {}

	account['id'] = int(account['id'])
	account['valor'] = float(account['valor'])
	account['saldo'] = float(account['saldo'])

	account.pop('linkBoleto')
	account['pagamento'].pop('borderos')
	account['idCliente'] = int(account['cliente']['idContato'])
	account.pop('cliente')
	return account