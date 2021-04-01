
-- Product Insert
INSERT INTO `destripida`.`produto`
(`idproduto`,
`codigo`,
`descricao`,
`situacao`,
`unidade`,
`preco`,
`precoCusto`,
`dataInclusao`,
`dataAteracao`,
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
<{dataAteracao: }>,
<{nomeFornecedor: }>,
<{marca: }>,
<{idFabricante: }>,
<{estoqueMinimo: }>,
<{estoqueMaximo: }>);




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