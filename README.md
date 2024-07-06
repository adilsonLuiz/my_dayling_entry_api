# My Dayling Entry API

API desenvolvida para, criação, manipulação de notas de entrada diaria de texto corrido.
Prove funções que manupulam notas, seus titulos, conteudo, e realiza operações direto no banco de dados.

---
## Como executar 

Primeiro baixar o arquivo via repositorio central, ou com o git instalado em seu computador executar o seguinte comando abaixo.
Comando abaixo server tanto para Windows quanto para Linux.
```
git clone  https://github.com/adilsonLuiz/my_dayling_entry_api.git
```

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## OBS: Para mais informações de navegação sobre o codigo fonte consulte o arquivo Help-me-understand.md dentro do diretorio raiz do projeto
