# DevOps Monitoring Platform

Uma plataforma de monitoramento que exibe informações de saúde do sistema (CPU e memória) em tempo real, utilizando Flask como framework web.

## Objetivo do Projeto

Criar uma plataforma que monitore a saúde de sistemas, infraestrutura e aplicações em tempo real, permitindo que administradores e desenvolvedores visualizem métricas e recebam alertas sobre o estado de seus serviços. O projeto pode ser usado por startups, pequenas empresas, ou equipes DevOps para monitorar seus ambientes.

## Funcionalidades

## Funcionalidades

- Monitoramento do uso de CPU e memória.
- Interface web simples e intuitiva.
- Containerização com Docker para portabilidade.
- Alertas em tempo real via email ou Slack.
- Dashboard interativo usando Grafana.
- Armazenamento e visualização de logs com ELK Stack.
- Visualização histórica de métricas.
- Autenticação de usuário para acesso ao dashboard.
- Suporte a múltiplas aplicações.
- API RESTful para coleta de dados de monitoramento.
- Configuração de métricas personalizadas.
- Relatórios automáticos agendados.
- Análise de performance para otimização de recursos.
- Integração com Docker para monitoramento de contêineres.
- Implementação de health checks para serviços monitorados.


## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **psutil**: Biblioteca para obter informações sobre o uso do sistema.
- **Docker**: Para containerização da aplicação.

### Ferramentas Utilizáveis no Projeto

- **GitHub**: Controle de versão, issues, gerenciamento de projeto.
- **Terraform**: Provisionamento de infraestrutura na AWS.
- **AWS (EC2, RDS, S3)**: Servidores de aplicação, armazenamento de dados e logs.
- **Docker**: Containerização de aplicações e serviços.
- **Kubernetes**: Orquestração e gerenciamento de contêineres.
- **Helm**: Gerenciamento de pacotes no Kubernetes.
- **Prometheus**: Monitoramento de métricas da aplicação.
- **Grafana**: Visualização de métricas e criação de dashboards.
- **Jenkins / GitHub Actions**: Automação de CI/CD.
- **Ansible**: Automação de configuração e gerenciamento de servidores.
- **SonarQube**: Análise da qualidade do código.
- **ELK Stack**: Agregação e análise de logs.

## Por que esse projeto é útil?

Este projeto ajuda equipes de desenvolvimento, operações e empresas a monitorar, gerenciar e escalar suas aplicações de maneira eficiente. Ele oferece uma solução completa de monitoramento em tempo real, escalabilidade automática e alertas proativos, o que é essencial para manter a saúde de sistemas e aplicações que atendem a clientes.

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