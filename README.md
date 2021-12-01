
## 1. Configuración de Ambiente

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`mkdir features`

`mkdir features/steps`

## 2. Crear archivo feature 

`touch search_in_duckduckgo.feature`

### 2.1 agregar el contenido del feature

```
Feature: Buscar contenido en duckduckgo
  As an user,
  I want to get answers for search terms via a REST API,
  So that my app can get answers anywhere.
```