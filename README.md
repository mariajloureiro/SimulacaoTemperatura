# Redundância e Tolerância a Falhas em Sistemas IoT 🌡️☁️

Repositório destinado à entrega da atividade prática da disciplina de **Sistemas Distribuídos Aplicados à Internet das Coisas**.

## Sobre a Atividade
O objetivo deste trabalho foi desenvolver um ecossistema IoT simulado em **Python** para demonstrar, de forma prática, os conceitos de **redundância** e **tolerância a falhas por replicação**. O sistema simula o envio de dados de sensores para um gateway, que por sua vez garante a persistência das informações em duas instâncias de armazenamento, permitindo a disponibilidade dos dados mesmo após uma falha simulada no arquivo principal.

> *Aviso Acadêmico:* Este projeto foi desenvolvido para fins estritamente educacionais, visando a compreensão de arquiteturas de sistemas distribuídos e alta disponibilidade.

## O que foi entregue neste repositório:
- **Simulador de Sensores:** Script que gera dados de temperatura, umidade e luminosidade.
- **Gateway de Dados:** Lógica central que recebe as leituras e executa a replicação em arquivos de dados primários e backup.
- **Teste de Tolerância a Falhas:** Simulação de corrupção/falha do arquivo principal para demonstração da integridade do backup.
- **Logs de Persistência:** Arquivos gerados durante a execução para registro das métricas.

## Tecnologias e Bibliotecas Utilizadas:
- **Linguagem:** Python 3.x
- **`random`**: Para geração de dados randômicos dos sensores.
- **`time`**: Para controle de intervalos e geração de timestamps.
- **`os`**: Para manipulação do sistema de arquivos e verificação de existência dos nós de dados.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Execute o script principal:
   ```bash
   python Sensor.py

## Integrantes:
- Maria Júlia Loureiro
- Rafaela Riganti
- Sophia Marcelino
