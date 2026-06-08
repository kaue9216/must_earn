# MUST EARN

## Trabalho de Raciocínio Algorítmico – PUCPR

### Integrantes

* Diego Woellner
* Gabriel Dudeck
* Heitor Rechi
* Kauê Ogibowski
* Leonardo Alquate

  
---

# Sobre o Projeto

**Must Earn** é um jogo de simulação financeira desenvolvido em Python utilizando a biblioteca PyQt5. O objetivo do jogador é administrar seus recursos financeiros, manter sua qualidade de vida e realizar investimentos estratégicos para acumular riqueza ao longo do tempo.

O jogo foi desenvolvido como projeto da disciplina de **Raciocínio Algorítmico** da **Pontifícia Universidade Católica do Paraná (PUCPR)**, aplicando conceitos fundamentais de programação, estruturas de dados, orientação a objetos, eventos gráficos e lógica computacional.

---

# Objetivo e Guia do Jogo

O jogador inicia sua jornada com um capital inicial de **R$ 1.500,00** e deve tomar decisões financeiras diariamente.

- Insira o nome do jogador na tela de inicio.
- Com seus **R$ 1.500,00** de capital inicial:
- Escolha seus investimentos entre Big Techs, Fintechs e Criptomoedas
- Acompanhe os indicadores de sobrevivência (aluguel, comida e remédio)
- Tome decisões estratégicas para aumentar seu patrimônio


Durante cada rodada é necessário:

* Investir em diferentes ativos financeiros;
* Gerenciar recursos básicos de sobrevivência;
* Interpretar notícias do mercado;
* Adaptar-se aos cenários econômicos;
* Maximizar o patrimônio acumulado.

 # Regras do Jogo

- O jogador perde se qualquer indicador de sobrevivência chegar a zero.
- O jogador precisa equilibrar investimentos e gastos diários.
- Eventos aleatórios afetam o mercado financeiro diariamente.
- O desempenho final é baseado no patrimônio acumulado.

O jogador vence ao atingir uma situação financeira favorável e manter seus indicadores básicos estáveis. Caso algo diferente como algum indicador essencial chegue a zero, ocorre o Game Over.

---

# História do Jogo

Em um futuro dominado pela cultura dos investimentos, o conceito de simplesmente guardar dinheiro deixou de existir.

As grandes corporações transformaram completamente a economia e criaram uma nova regra social:

> Investir é obrigatório. Crescer é obrigatório.

Nesse cenário, o jogador precisa sobreviver e prosperar em um mercado extremamente dinâmico, onde notícias econômicas impactam diretamente o valor dos investimentos.

---

# Mecânicas Principais

## Sistema de Investimentos

O jogo possui três categorias de ativos:

### Big Techs

Empresas de tecnologia consolidadas.

### Fintechs

Empresas financeiras inovadoras.

### Criptomoedas

Ativos digitais com alta volatilidade.

Cada categoria possui três níveis de risco:

| Sigla | Risco         |
| ----- | ------------- |
| C     | Conservador   |
| I     | Intermediário |
| A     | Arrojado      |

O jogador escolhe quanto investir em cada ativo antes de iniciar o dia.

---

## Cenários Econômicos

O mercado sofre alterações diariamente através de cenários aleatórios.

Foram implementados oito cenários:

1. Big Techs sobem, Fintechs estáveis e Cripto cai.
2. Big Techs estáveis, Fintechs caem e Cripto sobe.
3. Big Techs caem, Fintechs sobem e Cripto estável.
4. Big Techs sobem, Fintechs sobem e Cripto cai.
5. Big Techs sobem, Fintechs caem e Cripto sobe.
6. Big Techs caem, Fintechs sobem e Cripto sobe.
7. Todos os ativos sobem.
8. Todos os ativos caem.

Cada cenário modifica os investimentos através de porcentagens aleatórias, simulando oscilações reais de mercado.

---

## Sistema de Sobrevivência

Além de investir, o jogador deve administrar três necessidades básicas:

### Aluguel

Representa sua condição de moradia.

### Comida

Representa sua alimentação.

### Remédio

Representa sua saúde.

Ao final de cada rodada esses indicadores diminuem.

Caso qualquer um deles chegue a zero, o jogador perde a partida.

---

## Sistema de Gastos Diários

Ao final de cada dia o jogador pode utilizar seu dinheiro para recuperar seus indicadores.

Cada melhoria custa:

* R$ 400 para Aluguel
* R$ 400 para Comida
* R$ 400 para Remédio

Isso força o jogador a equilibrar investimentos e qualidade de vida.

---

## Sistema de Histórico

A cada rodada são armazenadas informações sobre:

* Nível de aluguel
* Nível de comida
* Nível de remédio
* Saldo financeiro
* Pontuação acumulada

Esses dados são registrados para acompanhamento da evolução do jogador.

---

## Sistema de Pontuação

A pontuação é calculada com base no dinheiro acumulado ao longo da partida.

Quanto maior o patrimônio construído pelo jogador, maior será sua pontuação final.

---

# Loja de Melhorias

O jogo também possui itens especiais que podem ser adquiridos para fornecer benefícios permanentes.

Exemplos:

* Kitnet
* Casa Própria
* SUS
* Omega 3
* Promoção no Trabalho
* Colete Puffer
* Videogame
* Carro Esportivo
* Macaco Digital

Esses itens alteram atributos do jogador e ampliam seus limites máximos de sobrevivência.

---

# Interface Gráfica

O projeto foi desenvolvido utilizando a biblioteca PyQt5.

Principais telas:

### Tela de Login

Permite inserir o nome do jogador.

### Tela Principal

Exibe:

* Saldo atual
* Indicadores de sobrevivência
* Jornal de notícias
* Área de investimentos

### Tela de Gastos Diários

Permite recuperar recursos essenciais.

### Tela de Vitória

Exibida quando o jogador alcança o objetivo do jogo.

### Tela de Derrota

Exibida quando algum indicador essencial chega a zero.

---

# Conceitos de Programação Utilizados

Durante o desenvolvimento foram aplicados diversos conceitos estudados na disciplina:

## Estruturas de Dados

* Listas
* Dicionários

## Programação Orientada a Objetos

* Classes
* Objetos
* Encapsulamento

## Manipulação de Eventos

* Botões
* Entradas de dados
* Janelas gráficas

## Modularização

Separação do sistema em múltiplos arquivos:

* player.py
* acoesv2.py
* histórico.py
* textos.py
* telas gráficas

## Geração Aleatória

Utilização do módulo Random para criar cenários econômicos dinâmicos.

---

# Tecnologias Utilizadas

* Python 3
* PyQt5
* Random
* Programação Orientada a Objetos

---

# Como Executar

## Instalar dependências

```bash
pip install PyQt5
```

## Executar o jogo

```bash
python must_earn_gui.py
```

---

# Considerações Finais

O projeto Must Earn permitiu aplicar na prática os conceitos de lógica de programação e raciocínio algorítmico estudados durante a disciplina.

Além do desenvolvimento técnico, o jogo explora temas de educação financeira, tomada de decisão, análise de risco e planejamento de recursos, tornando a experiência divertida e educativa.

---

**PUCPR – Pontifícia Universidade Católica do Paraná**
**Disciplina: Raciocínio Algorítmico**
**Projeto: Must Earn**
