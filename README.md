
# Mapa Interativo de Apicultura - Pernambuco

Este projeto consiste em um mapa interativo desenvolvido em Python com Flask para visualização de dados da apicultura no estado de Pernambuco. A aplicação apresenta informações sobre apicultores, produção de mel, cooperativas e a participação de mulheres no setor.

**Este é o projeto final da pós-graduação em Desenvolvimento Web Full Stack da Unipê.**  
**Estudante: Kleber Barros**

## Como Executar o Projeto

### Passos para Configuração

1. **Clonar o repositório**:
   
   Execute o comando abaixo para clonar o repositório no seu ambiente local:

   ```bash
   git clone https://github.com/kleberbarros9/mapa-iterativo---python-posweb.git
   ```

2. **Instalar dependências**:

   Navegue para o diretório do projeto e instale as dependências necessárias com:

   ```bash
   pip install -r requirements.txt
   ```

3. **Executar a aplicação**:

   Execute o script principal para iniciar o servidor Flask:

   ```bash
   python app.py
   ```

4. **Acessar o aplicativo no navegador**:

   Abra seu navegador e vá para o endereço:

   [http://localhost:5000/](http://localhost:5000/)

   Isso abrirá a página principal do Mapa Interativo de Apicultura.

## Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

```
project/
│
├── PE_UF_2022/
│   ├── PE_UF_2022.shp     # Arquivo shapefile com os limites geográficos de Pernambuco
│   ├── PE_UF_2022.shx     # Índice do shapefile
│   ├── PE_UF_2022.dbf     # Dados associados ao shapefile
│   └── ...                # Outros arquivos do shapefile
│
├── public/
│   ├── images/
│   │   ├── img1.jpg       # Imagem de exemplo para o carrossel
│   │   ├── img2.jpg       # Imagem de exemplo para o carrossel
│   │   ├── img3.jpg       # Imagem de exemplo para o carrossel
│   ├── index.html         # Página principal da aplicação
│   ├── devs.html          # Página sobre a equipe de desenvolvimento
│   ├── destaques.html     # Página sobre apicultoras em destaque
│   ├── script.js          # Scripts JavaScript para interatividade
│   └── styles.css         # Arquivo de estilos CSS para a aplicação
│
├── app.py                 # Script Python principal para rodar o servidor Flask
├── data.py                # Script para converter shapefiles para o formato GeoJSON
└── requirements.txt       # Arquivo com as dependências do projeto
```

## Funcionalidades

- **Mapa Interativo**: Exibição de um mapa interativo com informações detalhadas sobre cada município.
- **Estatísticas**: Painel com informações de produção, apicultores e cooperativas.
- **Destaque para Apicultoras**: Seção dedicada à valorização das mulheres na apicultura.
- **Notícias e Cooperativas**: Últimas notícias e informações sobre cooperativas ativas no estado.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para a construção do backend.
- **Flask**: Framework web utilizado para a construção do servidor.
- **Leaflet.js**: Biblioteca JavaScript para criação de mapas interativos.
- **Bootstrap**: Framework CSS para estilização responsiva.
- **HTML/CSS/JavaScript**: Construção do frontend e interatividade.

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de fornecer uma visão ampla sobre a apicultura no estado de Pernambuco, destacando as principais cooperativas, a participação de mulheres e os números de produção e exportação de mel.

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests no [repositório oficial](https://github.com/kleberbarros9/mapa-iterativo---python-posweb.git) para melhorias ou correções.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
