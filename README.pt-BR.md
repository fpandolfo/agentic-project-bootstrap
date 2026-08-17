# Agentic Project Bootstrap

Bootstrap open source, nativo do repositório e independente de player para
desenvolvimento agentic disciplinado.

Ele não fornece IDE, modelo ou serviço hospedado. Em vez disso, prepara um
repositório novo ou existente com contexto durável, owners canônicos,
validação proporcional e gates de decisão humana.

> Estado: `0.2.0-alpha.1`. O contrato de plan/apply já é funcional e testado;
> packs e upgrades ainda estão evoluindo.

## Fluxo

```text
manifesto -> plano -> aprovação humana do fingerprint -> apply -> verify
```

- `init` e `adopt` criam manifestos sem alterar o projeto-alvo;
- `plan` gera um artefato completo e revisável;
- `apply` exige aprovação explícita e recusa conflitos;
- arquivos do usuário nunca são sobrescritos silenciosamente;
- remoções nunca são automáticas;
- o gate de entrega procura vazamentos comuns de privacidade e segredos;
- Kiro, Codex e outros players são adaptadores opcionais.

## Uso rápido

Requisitos: Python 3.11+ e Git.

```bash
python3 agentic.py doctor

python3 agentic.py init \
  --name "Meu Produto" \
  --description "Descrição curta orientada a resultado." \
  --stack "TBD — descobrir antes da implementação" \
  --packs core,generic-agent,github,codex \
  --output /tmp/meu-produto.agentic.json

python3 agentic.py plan \
  --target /caminho/do/projeto \
  --manifest /tmp/meu-produto.agentic.json \
  --output /tmp/meu-produto.plan.json

python3 agentic.py apply \
  --plan /tmp/meu-produto.plan.json \
  --approve <fingerprint>

python3 agentic.py verify --target /caminho/do/projeto
```

O objetivo é permitir execução agentic com produto, risco e aceite ainda sob
responsabilidade humana. Veja o [README principal](README.md) para contrato,
packs, limites e contribuição.
