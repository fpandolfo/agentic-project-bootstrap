# Guia rápido

Este pacote prepara um repositório para desenvolvimento **agent-first**, sem amarrar o projeto ao Codex, Kiro ou a uma stack específica.

## Uso

1. Descompacte na raiz do repositório.
2. Inicialize os placeholders:

```bash
python tools/init_bootstrap.py \
  --name "Meu Projeto" \
  --slug "meu-projeto" \
  --description "Descrição curta do objetivo." \
  --stack "TBD"
```

3. Abra no Codex/Kiro.
4. Envie ao agent o prompt sugerido em `BOOTSTRAP.md`.
5. O agent deve fazer discovery antes de criar código de produto.
6. Rode `python tools/context_check.py`.

A estrutura existe para criar um sistema óbvio: owner canônico, leitura proporcional, pouco contexto e fechamento verificável. Remova ou una arquivos que deixarem de agregar valor.
