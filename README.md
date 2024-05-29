# Motorhome Travel App

## Descrição

Este projeto é um aplicativo web e mobile para viajantes de motorhome. O objetivo é fornecer informações detalhadas sobre campings, pontos de paragem e melhores rotas, criação de usuários, armazenamento de informações, classificações e depoimentos. O aplicativo é projetado para melhorar a experiência de viagem, oferecendo mapas interativos e dados úteis para os viajantes.

## Funcionalidades
- Mapas Interativos: Encontre campings próximos e visualize as melhores rotas.
- Informações de Camping: Detalhes sobre campings, incluindo amenidades, preços e disponibilidade.
- Criação de Usuários: Cadastro e gerenciamento de perfis de usuários.
- Armazenamento de Informações: Salve preferências, rotas favoritas e histórico de viagens.
- Classificação e Depoimentos: Avalie campings e leia avaliações de outros viajantes.
- Banco de Dados: Tabelas para armazenar informações de usuários, campings, rotas e depoimentos.


## Estrutura do Projeto

motorhome-travel-app/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database.py
│   │   └── main.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
├── mobile/
│   ├── android/
│   ├── ios/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
├── .gitignore
├── README.md
└── requirements.txt
└── requirements.txt

## Tecnologias Utilizadas

## Backend
- Framework: FastAPI
- Banco de Dados: PostgreSQL
- ORM: SQLAlchemy

## Frontend
- Linguagem: JavaScript
- Biblioteca: React

## Mobile
- Linguagem: JavaScript
- Framework: React Native

## Configuração do Ambiente

# Pré-requisitos

- Node.js
- Python 3.x
- PostgreSQL

## Passos para Configuração

1. Clone o Repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/motorhome-travel-app.git
cd motorhome-travel-app

2. Configuração do Backend:

bash
Copiar código
cd backend
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn app.main:app --reload

3. Configuração do Frontend:

bash
Copiar código
cd frontend
npm install
npm start

4. Configuração do Mobile:

bash
Copiar código
cd mobile
npm install
npm run android  # Para Android
npm run ios      # Para iOS

## Banco de Dados

## Tabelas

- Usuários:

   - id (PK)
   - nome
   - email
   - senha (hash)
   - data_criacao

- Campings:

    - id (PK)
    - nome
    - localizacao
    - descricao
    - preco
    - disponibilidade

- Rotas:

    - id (PK)
    - nome
    - pontos_interesse
    - distancia
    - tempo_estimado

- Depoimentos:

    - id (PK)
    - usuario_id (FK)
    - camping_id (FK)
    - nota
    - comentario
    - data

## Contribuição
1. Fork o projeto
2. Crie uma nova branch (__git checkout -b feature/nova-funcionalidade__)
3. Commit suas alterações (__git commit -am 'Adiciona nova funcionalidade__)
4. Push para a branch (__git push origin feature/nova-funcionalidade__)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato
Para dúvidas ou sugestões, entre em contato via email@example.com.<br>

#

Agradecemos por contribuir e usar o Motorhome Travel App! Boas viagens! 🚐✨