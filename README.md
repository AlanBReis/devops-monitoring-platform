# DevOps Monitoring Platform

Uma plataforma de monitoramento que exibe informações de saúde do sistema (CPU e memória) em tempo real, utilizando Flask como framework web.

![em execução](/images/image.png)

## Objetivo do Projeto

Criar uma plataforma que monitore a saúde de sistemas, infraestrutura e aplicações em tempo real, permitindo que administradores e desenvolvedores visualizem métricas sobre o estado de seus serviços.


## Funcionalidades

- Monitoramento do uso de CPU e memória.
- Interface web simples e intuitiva.
- Containerização com Docker para portabilidade.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **psutil**: Biblioteca para obter informações sobre o uso do sistema.
- **Docker**: Para containerização da aplicação.


## Pré-requisitos

Antes de começar, verifique se você tem os seguintes itens instalados:

- [Python 3.6 ou superior](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) (apenas no Windows, para compilar dependências)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/devops-monitoring-platform.git
   cd devops-monitoring-platform

## Dockerização
 Para rodar a aplicação em um contêiner Docker, execute os seguintes comandos:  

1. Construa a imagem Docker:
   ```bash
   docker build -t devops-monitoring-app .

2. Execute o container:
   ```bash
   docker run -p 5000:5000 devops-monitoring-app

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.