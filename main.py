from produto import ProdutoNacional, ProdutoImportado
from funcionario import FuncionarioCLT, FuncionarioPJ

# Lista de produtos
produtos = [
    ProdutoNacional("Monitor", 800.0, 10),
    ProdutoImportado("Notebook", 3500.0, 4, 0.20),
    ProdutoNacional("Fone", 150.0, 30)
]

# Lista de funcionários
funcionarios = [
    FuncionarioCLT("Luciana", 3200),
    FuncionarioPJ("Rafael", 100, 60)
]

# Exibir detalhes dos produtos + notas fiscais
print("\n")
for p in produtos:
    p.exibir_detalhes()
    p.emitir_nota()
    print(f"Preço final: R${p.preco_final():.2f}")
    print("-" * 40)

# Calcular pagamentos dos funcionários
print("\n")
for f in funcionarios:
    print(f"{f.nome} receberá R${f.calcular_pagamento():.2f}")
print("-" * 40)

# Simular venda e reposição
print("\n")
produto_venda = produtos[0]  # Monitor
produto_venda.vender(3)      # Vender 3 monitores
produto_venda.repor(5)       # Repor 5 monitores
