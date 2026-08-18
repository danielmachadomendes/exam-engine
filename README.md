# Exam Engine

Private examination and readiness assessment platform.

## Purpose

Platform for creating, managing and evaluating certification readiness exams.

## Architecture

- Backend: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Authentication: JWT
- Infrastructure: Docker

## Development

The application is currently under development.

Perfeito. Temos então a base do Exam Engine estável:

✅ FastAPI + Uvicorn  
✅ PostgreSQL  
✅ SQLAlchemy  
✅ Alembic sincronizado (701fb8a68e17 (head))  
✅ Authentication com JWT  
✅ Roles: ADMIN, MANAGER, LEARNER  
✅ Users existentes  
✅ Models de Exam, Topic, Question, Answer, Attempt, etc.  
✅ QuestionType: SINGLE_CHOICE, MULTIPLE_CHOICE, TRUE_FALSE  
✅ Docker Compose funcional  
✅ /docs disponível  
✅ alembic check sem novas operações  
Próximo passo: Question Management API  
  
Agora faz sentido começarmos a transformar os models em funcionalidades reais.  
  
Eu planeio avançar nesta ordem:  
  
Topics API  
- criar topic  
- listar topics  
- editar  
- ativar/desativar  
Questions API  
- criar pergunta  
- listar perguntas  
- obter pergunta  
- editar  
- ativar/desativar  
- associar respostas  
- validação específica para TRUE_FALSE, SINGLE_CHOICE e MULTIPLE_CHOICE  
Exams API  
- criar exame  
- definir número de perguntas  
- passing score  
- time limit  
- associar perguntas  
Exam attempt  
- learner inicia exame  
- responde  
- submete  
- sistema calcula score  
- determina passed  
Results / dashboard  
- histórico do learner  
- resultados  
- performance por topic  
- performance por dificuldade  