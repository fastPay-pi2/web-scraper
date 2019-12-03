# Web Scraper

O Web Scraper tem a função de coletar produtos para popular nosso banco de dados da [API de Produtos](https://github.com/fastPay-pi2/products-api). Os dados coletados serão armazenados apenas para fins de demonstração do protótipo com dados reais.


## Como executar

### Clone o repositório

```shell
$ git clone https://github.com/fastPay-pi2/web-scraper
```

### Baixe as dependências

Recomendamos a criação de um **virtualenv** para baixar as dependências do sistema. Certifique-se de possuir o **virtualenv** instalado no seu pc.

```shell
$ cd web-scraper/
$ virtualenv env -p python3
$ source env/bin/activate
$ pip install -r requirements.txt
```

Para que o scraper interprete o Javascript dinâmico usado pelas páginas web, foi utilizada uma ferramenta chamada **Splash**. Mais informações podem ser encontradas em [The Scraping Blog](https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash). Para executar o splash:

```shell
$ docker pull scrapinghub/splash
$ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
```

### Inicie o scraper

```shell
$ cd fastpay_scraper/
$ scrapy crawl fast_spider -o all_prods.jl
```
