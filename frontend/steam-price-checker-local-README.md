
# Steam Price Checker Local

Este projeto permite consultar os preços atuais de jogos da tua **Steam Wishlist** usando os IDs dos jogos.  
Ele gera um ficheiro JSON com o nome do jogo, preço atual e a data da consulta.

O projeto é composto por:

- **Backend:** FastAPI (`main.py`) que consulta a Steam Web API
- **Frontend:** HTML/JS (`frontend/index.html`) que envia os IDs e gera o ficheiro JSON

---

## Estrutura do Projeto

```
steam-price-checker-local/
 ├── main.py           # Backend FastAPI
 └── frontend/
     └── index.html    # Frontend para interação com o backend
```

---

## Requisitos

- Python 3.10 ou superior
- pip
- Navegador moderno (Chrome, Edge, Firefox)

---

## Passos para correr localmente

1. **Clona ou descompacta o projeto**

```bash
git clone <repositório-ou-descompacta-o-zip>
cd steam-price-checker-local
```

2. **Cria um ambiente virtual (opcional, mas recomendado)**

```bash
python -m venv venv
```

Ativa o ambiente:

- **Windows:**  
```bash
venv\Scripts\activate
```

- **Mac/Linux:**  
```bash
source venv/bin/activate
```

3. **Instala dependências**

```bash
pip install fastapi uvicorn requests
```

4. **Corre o backend FastAPI**

```bash
uvicorn main:app --reload
```

- O backend vai correr em: `http://127.0.0.1:8000`

5. **Abrir o frontend**

- Abre o ficheiro `frontend/index.html` no navegador.
- Cola os IDs da tua wishlist Steam (um por linha).
- Clica **Gerar JSON**.
- Vai ser descarregado um ficheiro `steam_prices.json` com os preços atuais.

---

## Estrutura do JSON de saída

O ficheiro `steam_prices.json` terá a seguinte estrutura:

```json
[
    {
        "id": 620,
        "name": "Portal 2",
        "price": 9.99,
        "currency": "EUR",
        "date_checked": "2025-11-19 12:00:00"
    },
    {
        "id": 730,
        "name": "CS:GO",
        "price": 0,
        "currency": "FREE",
        "date_checked": "2025-11-19 12:00:05"
    }
]
```

---

## Notas

- O backend usa a Steam Web API pública (`store.steampowered.com/api/appdetails`).  
- Jogos gratuitos aparecem com `price: 0` e `currency: FREE`.  
- Recomenda-se correr o backend em `localhost` para testes antes de fazer deploy online.  

---

## Possíveis melhorias

- Adicionar histórico de preços (armazenar em CSV ou SQLite)  
- Parallelizar requisições para listas grandes  
- Criar frontend moderno usando React ou TailwindCSS  
- Deploy online usando Render, Vercel ou outro serviço

---

## Autor

- Desenvolvido por Nuno Cordeiro
