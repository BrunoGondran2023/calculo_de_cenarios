Financial Scenarios Module
Descrição
Este módulo fornece uma função para calcular cenários otimistas e pessimistas com base em dados financeiros históricos. Ele é útil para análise de investimentos, gestão de riscos e planejamento financeiro.

Instalação
Você pode instalar o módulo usando o pip:

pip install financial_scenarios


import numpy as np
from financial_scenarios import calcular_cenarios

# Defina seus dados financeiros como um array numpy ou importação externa.

Exemplo:<br>
vetor = np.array([1.31, 1.34, 1.42, 1.4, 1.42, 1.4, 1.47, 1.45, 1.48, 1.42,
                  1.34, 1.34, 1.35, 1.35, 1.36, 1.32, 1.24, 1.22, 1.27, 1.26])

# Calcule os cenários otimistas e pessimistas
otimista, pessimista = calcular_cenarios(vetor)

# Exiba os resultados
if otimista is not None:
    print(f'Cenário otimista: {round(otimista * 100, 1)}%\nCenário pessimista: {round(pessimista * 100, 1)}%')
else:
    print("Não há dados suficientes para calcular os cenários.")


# Contribuições:<br>

Contribuições são bem-vindas! Para contribuir com este módulo, siga estas etapas:

- Faça um fork do repositório.<br>
- Crie uma nova branch com a sua feature (git checkout -b minha-feature).<br>
- Faça commit das suas alterações (git commit -am 'Adicionando nova feature').<br>
- Faça push para a branch (git push origin minha-feature).<br>
- Crie um novo Pull Request.<br>

# Autor:<br>
Bruno Gondran

# Licença:<br>
Este módulo é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.<br>
https://github.com/BrunoGondran2023/calculo_de_cenarios/blob/main/license.md
