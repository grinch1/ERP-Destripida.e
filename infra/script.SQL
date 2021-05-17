-- CREATE STATEMENTS --
CREATE DATABASE `destripida`;

CREATE TABLE `cliente` (
  `idCliente` bigint NOT NULL,
  `nome` varchar(45) COLLATE utf8_bin NOT NULL,
  `cpf` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `rg` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `endereco` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `numero` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `complemento` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `cidade` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `bairro` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `cep` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `uf` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `celular` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `fone` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE KEY `idCliente_UNIQUE` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `item` (
  `idItem` varchar(15) COLLATE utf8_bin NOT NULL,
  `descricao` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `quantidade` int NOT NULL,
  `valorunidade` double NOT NULL,
  `codProduto` varchar(45) COLLATE utf8_bin NOT NULL,
  `idPedido` bigint NOT NULL,
  PRIMARY KEY (`idItem`),
  UNIQUE KEY `idItem_UNIQUE` (`idItem`),
  KEY `fk_item_produto1_idx` (`codProduto`),
  KEY `fk_item_pedido1_idx` (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `pedido` (
  `idPedido` bigint NOT NULL,
  `idCliente` bigint NOT NULL,
  `desconto` double DEFAULT NULL,
  `data` date DEFAULT NULL,
  `vendedor` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `valorfrete` double DEFAULT NULL,
  `totalprodutos` double DEFAULT NULL,
  `totalvenda` double DEFAULT NULL,
  `situacao` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `pagamento` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `dataSaida` date DEFAULT NULL,
  PRIMARY KEY (`idPedido`),
  UNIQUE KEY `idPedido_UNIQUE` (`idPedido`),
  KEY `fk_pedido_cliente1_idx` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE `produto` (
  `idProduto` bigint NOT NULL,
  `codigo` varchar(45) COLLATE utf8_bin NOT NULL,
  `descricao` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `situacao` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `unidade` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `preco` double NOT NULL,
  `precoCusto` double NOT NULL,
  `dataInclusao` date DEFAULT NULL,
  `dataAlteracao` date DEFAULT NULL,
  `nomeFornecedor` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `marca` varchar(45) COLLATE utf8_bin NOT NULL,
  `idFabricante` bigint NOT NULL,
  `estoqueMinimo` int DEFAULT NULL,
  `estoqueMaximo` int DEFAULT NULL,
  `estoqueAtual` int DEFAULT NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE KEY `idProduto_UNIQUE` (`idProduto`),
  UNIQUE KEY `codigo_UNIQUE` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- INSERT STATEMENTS --

INSERT INTO `destripida`.`cliente`
(`idCliente`, `nome`, `cpf`, `rg`, `endereco`, `numero`, `complemento`, 
`cidade`, `bairro`, `cep`, `uf`, `email`, `celular`, `fone`)
VALUES
(<{idCliente: }>, <{nome: }>, <{cpf: }>, <{rg: }>, 
<{endereco: }>, <{numero: }>, <{complemento: }>, <{cidade: }>, 
<{bairro: }>, <{cep: }>, <{uf: }>, <{email: }>, <{celular: }>, <{fone: }>);

INSERT INTO `destripida`.`item`
(`idItem`, `descricao`, `quantidade`, `valorunidade`, `codProduto`, `idPedido`)
VALUES
(<{idItem: }>, <{descricao: }>, <{quantidade: }>, <{valorunidade: }>, <{codProduto: }>, <{idPedido: }>);

INSERT INTO `destripida`.`pedido`
(`idPedido`, `idCliente`, `desconto`, `data`, `vendedor`, `valorfrete`, 
`totalprodutos`, `totalvenda`, `situacao`, `pagamento`,  `dataSaida`)
VALUES
(<{idPedido: }>, <{idCliente: }>, <{desconto: }>, <{data: }>, <{vendedor: }>, 
<{valorfrete: }>, <{totalprodutos: }>, <{totalvenda: }>, <{situacao: }>, <{pagamento: }>,  <{dataSaida: }>);

INSERT INTO `destripida`.`produto`
(`idProduto`, `codigo`, `descricao`, `situacao`, `unidade`, `preco`, 
`precoCusto`, `dataInclusao`, `dataAlteracao`, `nomeFornecedor`, `marca`, 
`idFabricante`, `estoqueMinimo`, `estoqueMaximo`, `estoqueAtual`)
VALUES
(<{idProduto: }>, <{codigo: }>, <{descricao: }>, <{situacao: }>, <{unidade: }>, 
<{preco: }>, <{precoCusto: }>, <{dataInclusao: }>, <{dataAlteracao: }>, 
<{nomeFornecedor: }>, <{marca: }>, <{idFabricante: }>, <{estoqueMinimo: }>, 
<{estoqueMaximo: }>, <{estoqueAtual: }>);

-- UPDATE STATEMENTS --

UPDATE `destripida`.`cliente`
SET
`idCliente` = <{idCliente: }>,
`nome` = <{nome: }>,
`cpf` = <{cpf: }>,
`rg` = <{rg: }>,
`endereco` = <{endereco: }>,
`numero` = <{numero: }>,
`complemento` = <{complemento: }>,
`cidade` = <{cidade: }>,
`bairro` = <{bairro: }>,
`cep` = <{cep: }>,
`uf` = <{uf: }>,
`email` = <{email: }>,
`celular` = <{celular: }>,
`fone` = <{fone: }>
WHERE `idCliente` = <{expr}>;

UPDATE `destripida`.`item`
SET
`idItem` = <{idItem: }>,
`descricao` = <{descricao: }>,
`quantidade` = <{quantidade: }>,
`valorunidade` = <{valorunidade: }>,
`codProduto` = <{codProduto: }>,
`idPedido` = <{idPedido: }>
WHERE `idItem` = <{expr}>;

UPDATE `destripida`.`pedido`
SET
`idPedido` = <{idPedido: }>,
`idCliente` = <{idCliente: }>,
`desconto` = <{desconto: }>,
`data` = <{data: }>,
`vendedor` = <{vendedor: }>,
`valorfrete` = <{valorfrete: }>,
`totalprodutos` = <{totalprodutos: }>,
`totalvenda` = <{totalvenda: }>,
`situacao` = <{situacao: }>,
`dataSaida` = <{dataSaida: }>
WHERE `idPedido` = <{expr}>;

UPDATE `destripida`.`produto`
SET
`idProduto` = <{idProduto: }>,
`codigo` = <{codigo: }>,
`descricao` = <{descricao: }>,
`situacao` = <{situacao: }>,
`unidade` = <{unidade: }>,
`preco` = <{preco: }>,
`precoCusto` = <{precoCusto: }>,
`dataInclusao` = <{dataInclusao: }>,
`dataAlteracao` = <{dataAlteracao: }>,
`nomeFornecedor` = <{nomeFornecedor: }>,
`marca` = <{marca: }>,
`idFabricante` = <{idFabricante: }>,
`estoqueMinimo` = <{estoqueMinimo: }>,
`estoqueMaximo` = <{estoqueMaximo: }>,
`estoqueAtual` = <{estoqueAtual: }>
WHERE `codigo` = <{expr}>;
