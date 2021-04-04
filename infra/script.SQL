
-- Product Insert
INSERT INTO `destripida`.`produto`
(`idProduto`,
`codigo`,
`descricao`,
`situacao`,
`unidade`,
`preco`,
`precoCusto`,
`dataInclusao`,
`dataAlteracao`,
`nomeFornecedor`,
`marca`,
`idFabricante`,
`estoqueMinimo`,
`estoqueMaximo`)
VALUES
(<{idproduto: }>,
<{codigo: }>,
<{descricao: }>,
<{situacao: }>,
<{unidade: }>,
<{preco: }>,
<{precoCusto: }>,
<{dataInclusao: }>,
<{dataAlteracao: }>,
<{nomeFornecedor: }>,
<{marca: }>,
<{idFabricante: }>,
<{estoqueMinimo: }>,
<{estoqueMaximo: }>);

--Product Update
UPDATE `destripida`.`produto`
SET
`codigo` = <{codigo: }>,
`idProduto` = <{idProduto: }>,
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
`estoqueMaximo` = <{estoqueMaximo: }>
WHERE `codigo` = <{expr}>;


-- Client Insert
INSERT INTO `destripida`.`cliente`
(`idcliente`,
`nome`,
`cpf`,
`rg`,
`endereco`,
`numero`,
`complemento`,
`cidade`,
`bairro`,
`cep`,
`uf`,
`email`,
`celular`,
`fone`)
VALUES
(<{idcliente: }>,
<{nome: }>,
<{cpf: }>,
<{rg: }>,
<{endereco: }>,
<{numero: }>,
<{complemento: }>,
<{cidade: }>,
<{bairro: }>,
<{cep: }>,
<{uf: }>,
<{email: }>,
<{celular: }>,
<{fone: }>);



-- Item Insert
INSERT INTO `destripida`.`item`
(`iditem`,
`codigo`,
`descricao`,
`quantidade`,
`valorunidade`,
`un`)
VALUES
(<{iditem: }>,
<{codigo: }>,
<{descricao: }>,
<{quantidade: }>,
<{valorunidade: }>,
<{un: }>);