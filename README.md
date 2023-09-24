# Projeto .NET com ECS Fargate e AWS CDK

Este é um projeto que combina uma REST API em .NET, um aplicativo da web em .NET e uma infraestrutura gerenciada pela AWS Cloud Development Kit (CDK) usando Fargate para hospedar os serviços .NET na Amazon Elastic Container Service (ECS). O objetivo principal deste projeto é alcançar um badge de .NET bem-sucedido com ECS Fargate.

## Conteúdo

- [Arquitetura](#arquitetura)
- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Implantação](#implantação)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Arquitetura

A arquitetura do projeto envolve os seguintes componentes principais:

1. **Weather API**: Uma API RESTful construída em .NET para fornecer serviços.

2. **Weather Site**: Um aplicativo web construído em .NET que consome a API REST.

3. **Infra**: A infraestrutura é definida como código usando o AWS CDK em Python. Ela provisiona recursos necessários, como clusters do ECS Fargate, Load Balancers e outras dependências.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- .NET SDK: [Download .NET](https://dotnet.microsoft.com/download)
- AWS CLI: [Instruções de instalação](https://aws.amazon.com/cli/)
- AWS CDK: [Instruções de instalação](https://aws.amazon.com/cdk/)
- Python: [Download Python](https://www.python.org/downloads/)

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```

2. Configure suas credenciais AWS:

   ```bash
   aws configure
   ```

3. Dentro da pasta `infrastructure`, execute o seguinte comando para implantar a infraestrutura AWS usando o CDK:

   ```bash
   cd infra
   cdk deploy
   ```

## Implantação

1. Construa e implante a REST API e o aplicativo da web .NET de acordo com as instruções específicas do projeto.

2. Atualize o Load Balancer criado pela infraestrutura AWS CDK com os grupos de destino corretos.

3. Acesse o aplicativo da web através do Load Balancer público para verificar se a implantação está funcionando corretamente.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você encontrar problemas ou tiver sugestões, abra uma issue ou envie um pull request.

## Licença

Este projeto é licenciado sob a licença [MIT](LICENSE).
```

Você pode copiar e colar este Markdown no arquivo README.md do seu projeto, personalizando-o conforme necessário.