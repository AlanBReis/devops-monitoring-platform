# DevOps Monitoring Platform

Uma plataforma de monitoramento que exibe informações de saúde do sistema (CPU e memória) em tempo real, utilizando Flask como framework web.

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

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Para Git Bash no Windows

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

## Execução da Aplicação
1. Execute a aplicação:

   ```bash
   python main.py

2. Acesse a aplicação em seu navegador:
 
   ```bash   
   http://localhost:5000

   
## Dockerização
 Para rodar a aplicação em um contêiner Docker, execute os seguintes comandos:  

1. Construa a imagem Docker:
   ```bash
   docker build -t devops-monitoring-app .

2. Execute o container:
   ```bash
   docker run -p 5000:5000 devops-monitoring-app

## Contribuição
Se você deseja contribuir com este projeto, fique à vontade para abrir um pull request ou criar uma issue.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.