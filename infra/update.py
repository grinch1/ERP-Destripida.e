import mysql.connector  
from infra.api import Api, ApiError
from infra.apiKey import api_key
from infra.connection import Database
import pandas as pd
import json
from jsondiff import diff

api = Api(api_key)
class Import():

	def filter_product(self, product):
		product.pop('tipo')
		product.pop('descricaoCurta')
		product.pop('descricaoComplementar')
		product.pop('imageThumbnail')
		product.pop('urlVideo')
		product.pop('codigoFabricante')
		product.pop('marca')
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

	
	def products(self):
		try:
			# opening database
			db = Database()
			# getting products from api
			products = api.get_products()
			# opening file with products records
			p_file = open("infra/imported/produtos.json", "r")
			records = json.load(p_file)
			p_file.close()
			# checking every product
			for product in products:
				product = self.filter_product(product)
				# checking if product was imported already
				if product['id'] not in records or records[product['id']] != product:
					if product['id'] in records:
						print(f'UPDATE: {product["id"]}\n')
						print(f'\tOLD: {diff(product, records[product["id"]])}\n')
						print(f'\tNEW: {diff(records[product["id"]], product)}\n')

					records[product['id']] = product
					# transpose colums and rows
					
					p_file = open("infra/imported/produtos.json", "w")
					json.dump(records, p_file)
					p_file.close()
					
					# self._insert_database(table='produto', obj=product)

		except ApiError as e:
			print(e.response)
		# db.close()
		
	def filter_item(self, item):
			item.pop('pesoBruto')
			item.pop('largura')
			item.pop('altura')
			item.pop('profundidade')
			item.pop('descricaoDetalhada')
			item.pop('unidadeMedida')
			item.pop('gtin')
			return item
	
	def filter_order(self, order):
		order.pop('observacoes')
		order.pop('observacaointerna')
		order.pop('numeroOrdemCompra')
		order.pop('parcelas')
		if 'pagamento' in order:
			order.pop('pagamento')
		return order

	def orders(self):
		try:
			# db = Database()
			orders = api.get_orders()
			# opening file with order records
			o_file = open("infra/imported/pedidos.json", "r")
			o_records = json.load(o_file)
			o_file.close()
			# opening file with client records
			c_file = open("infra/imported/clientes.json", "r")
			c_records = json.load(c_file)
			c_file.close()
			# opening file with itens records
			ip_file = open("infra/imported/itens_pedido.json", "r")
			ip_records = json.load(ip_file)
			ip_file.close()
			
			for order in orders:
				# filtering relevant data
				order = self.filter_order(order)
				# splitting cliente
				client = order['cliente']
				order.pop('cliente')
				# inserting idCliente to order 
				order['idCliente'] = client['id']
				# splitting itens
				itens = order['itens']
				order.pop('itens')

				for item in itens:
					# filtering relevant data
					item = self.filter_item(item['item'])
					# referencing item to order id
					cod_item = item['codigo']
					cod_item_order = f"{order['numero']}-{cod_item}"
					item['idPedido'] = order['numero']

					if cod_item_order not in ip_records or ip_records[cod_item_order] != item:
						if cod_item_order in ip_records:
							print(f'UPDATE: {cod_item_order}\n')
							print(f'\tOLD: {diff(item, ip_records[cod_item_order])}\n')
							print(f'\tNEW: {diff(ip_records[cod_item_order], item)}\n')
						
						ip_records[cod_item_order] = item
						ip_file = open("infra/imported/itens_pedido.json", "w")
						json.dump(ip_records, ip_file)
						ip_file.close()
					

				# checking if order was imported already
				if order['numero'] not in o_records or o_records[order['numero']] != order:
					if order['numero'] in o_records:
						print(f'UPDATE: {order["numero"]}\n')
						print(f'\tOLD: {diff(order, o_records[order["numero"]])}\n')
						print(f'\tNEW: {diff(o_records[order["numero"]], order)}\n')
					
					o_records[order['numero']] = order
					o_file = open("infra/imported/pedidos.json", "w")
					json.dump(o_records, o_file)
					o_file.close()
				# checking if client was imported already
				if client['id'] not in c_records or c_records[client['id']] != client:
					if client['id'] in c_records:
						print(f'UPDATE: {client["id"]}\n')
						print(f'\tOLD: {diff(client, c_records[client["id"]])}\n')
						print(f'\tNEW: {diff(c_records[client["id"]], client)}\n')

					c_records[client['id']] = client
					c_file = open("infra/imported/clientes.json", "w")
					json.dump(c_records, c_file)
					c_file.close()
					# self._insert_database(table='pedido', obj=order)

		except ApiError as e:
			print(e.response)
		# db.close(


	def receivable(self):
		try:
			#db = Database()
			accounts_r = api.get_accounts_receivable()

			# opening file with account_r records
			tr_file = open ("infra/imported/contas_receber.json", "r")
			records = json.load(tr_file)
			tr_file.close()
			for account_r in accounts_r:
				# checking if account_r was imported already
				if account_r['id'] not in records or records[account_r['id']] != account_r:
					if account_r['id'] in records:
						print(f'UPDATE: {account_r["id"]}\n')
						print(f'\tOLD: {diff(account_r, records[account_r["id"]])}\n')
						print(f'\tNEW: {diff(records[account_r["id"]], account_r)}\n')

					records[account_r['id']] = account_r
					o_file = open("infra/imported/contas_receber.json", "w")
					json.dump(records, o_file)
					o_file.close()
			 # checking every account_r

		except ApiError as e:
			print(e.response)
	
	
	
