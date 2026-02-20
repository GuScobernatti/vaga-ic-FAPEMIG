# Extração de Características em Sinais de Corrente

Este desafio técnico faz parte do processo seletivo para concessão de bolsa de Iniciação
Científica (FAPEMIG). Deverá ser desenvolvido um algoritmo para processamento
e análise de sinais temporais, conforme especificações descritas no documento enviado pelo Dr. Giovani.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido inteiramente em **Python**, focando no ecossistema de Data Science e Engenharia, cujas bibliotecas utilizadas foram:

- **Pandas:** Para leitura dos arquivos `.csv`, manipulação das séries temporais e geração da tabela estatística vetorializada.
- **NumPy:** Para manipulação de arrays e busca de índices (`argmax`, `argmin`, fatiamento).
- **SciPy (`scipy.signal`):** Para detecção avançada de picos (`find_peaks`).
- **Matplotlib:** Para a geração e exportação dos gráficos individuais e de dispersão.
- **Glob:** Para lidar com a manipulação de múltiplos arquivos automaticamente. Evitando setar todos os nomes dos arquivos em variáveis diferentes ou numa lista e já tornando o código responsivo para a possível adição de mais arquivos.

## 📂 Estrutura do Projeto

Para que o script funcione corretamente, a estrutura de diretórios deve seguir o padrão abaixo:

```text
/GustavoLuiz
│
├── /codigo/
│   ├── main.py                  # Script principal de execução
│   ├── features_processment.py  # Funções matemáticas de extração (F1 a F6)
│   └── tabela_estatistica.csv   # Tabela gerada automaticamente (Item 4.3)
│
├── /dados/                      # Pasta contendo os 10 arquivos .csv brutos
│
├── /graficos/
│   ├── /dispersao/              # Gráfico de dispersão gerado (Item 4.2)
│   └── /sinais_individuais/     # Gráficos individuais gerados (Item 4.1)
│
├── README.md                    # Documentação do projeto
└── .gitignore                   # Arquivos/pastas não versionados pelo git ao github
```

---

## ⚙️ Pré-requisitos e Instalação

Antes de executar, certifique-se de ter o Python instalado e instale as dependências executando o comando abaixo no seu terminal:

```bash
pip install pandas numpy scipy matplotlib
```

---

## 🚀 Como Executar

1. Abra o terminal da IDE.
2. Navegue até a pasta `codigo`:

```bash
cd GustavoLuiz/codigo
```

3. Execute o script principal:

```bash
python main.py
```

4. **Resultado:** O terminal imprimirá a tabela estatística e os arquivos gerados serão salvos automaticamente nas suas respectivas pastas.

---

## 🧠 Metodologia e Processamento de Sinais

- Primeiramente, foi utilizado o conceito de clean code. Separando cada função por suas respectivas funcionalidades e todas elas em um arquivo `features_processment.py`. Cada função cuida da sua respectiva feature e o arquivo `main.py` faz o processamento bruto, todas as execuções e renderizações necessárias.

Lidar com dados reais de sensores exige tratamento de ruído. A seguinte lógica matemática foi aplicada:

1. Atenuação de Ruído: Foi aplicada uma Média Móvel (Rolling Mean) ao sinal bruto. Isso impede que picos falsos causados por algum tipo de ruído interfiram na detecção e que o gráfico fique muito espalhado. O algoritmo pensa no sinal suavizado (mais linear), mas plota os pontos sobre o sinal original.

2. Delimitação do Pulso (F1 e F6): Encontrados calculando 2% da corrente máxima absoluta. Utilizou-se fatiamento de arrays para garantir que o F6 só fosse procurado após a ocorrência do pico máximo de regime.

3. Picos Intermediários (F2 e F4): O F4 (Regime) foi extraído via máximo global (np.argmax). O F2 foi localizado utilizando a função find_peaks do pacote SciPy, configurada com parâmetros de height e prominence atrelados à proporção da corrente máxima, ignorando flutuações menores (micro-picos).

4. Vales (F3): Encontrado através do mínimo global (np.argmin) no intervalo estrito (fatiado) entre os índices do F2 e do F4.

---

#### Obrigado pela oportunidade de participar do processo. Foi muito gratificante e passível de novos conhecimentos adquiridos.

- Gustavo Luiz Scobernatti de Almeida - 2025003202.
- Contatos:
  - **WhatsApp:** 33984630077;
  - **GitHub:** https://github.com/GuScobernatti;
  - **E-mail institucional:** d2025003202@unifei.edu.br;
  - **E-mail pessoal:** gustavo.scobernatti26@gmail.com
