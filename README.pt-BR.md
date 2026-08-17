# Agentic Project Bootstrap

Aponte qualquer agente de código capaz para um único arquivo e ofereça a ele
uma forma disciplinada de descobrir, estruturar, documentar e evoluir um projeto
junto com você.

Não depende de modelo, IDE, agente, conta ou instalação específica. Este é um
pack portátil de orientação: ajuda o agente a encontrar evidências, fazer boas
perguntas, propor opções e preservar contexto durável. O humano continua sendo
o responsável pelo produto e pelas decisões.

> Estado: `0.2.0-alpha.2`. O onboarding agent-first e o discovery read-only já
> são funcionais; os contratos de extensão e aplicação ainda estão evoluindo.

## Comece com um prompt

Clone ou baixe este repositório e diga ao seu agente:

```text
Leia /caminho/agentic-project-bootstrap/START_HERE.md.

Use o modo ADOPT_PROJECT no meu repositório atual. Comece com discovery somente
leitura. Não implemente nem modifique arquivos ainda.

Separe fatos, inferências, desconhecidos e propostas. Pergunte sobre intenção de
produto e regras de negócio que o repositório não consegue provar. Depois
proponha os contextos, diagramas, ADRs, tooling e plano de entrega mínimos para
minha aprovação.
```

Para uma ideia nova, use `NEW_PROJECT` e descreva o resultado desejado. Há mais
exemplos em [PROMPTS.md](PROMPTS.md).

## Como funciona

```text
LER -> DESCOBRIR -> PERGUNTAR -> PROPOR -> APROVAR -> GERAR -> OPERAR
```

1. `START_HERE.md` estabelece o modo, os limites e o primeiro retorno esperado.
2. `tools/discover_project.py` gera um inventário estrutural sem ler conteúdo.
3. `CAPABILITIES.md` mostra o que a suíte pode ajudar a produzir.
4. Um playbook guia projeto novo, existente ou já compreendido.
5. O agente inspeciona seletivamente as evidências relevantes.
6. O humano decide produto, regras de negócio, risco e aceite.
7. O agente gera somente os artefatos aprovados e úteis naquele momento.
8. O repositório preserva contexto para a próxima sessão limpa.

## Discovery estrutural seguro

Python 3.11+ é necessário apenas para os scripts auxiliares opcionais.

```bash
python3 tools/discover_project.py \
  --target /caminho/do/projeto \
  --format markdown
```

O script inventaria nomes e estrutura. Ele não lê conteúdo, não executa comandos
do projeto, não segue links simbólicos e ignora diretórios comuns de dependências,
cache e build. Candidatos sensíveis são informados somente pelo caminho.

## Modos

| Modo | Quando usar | Resultado principal |
|---|---|---|
| `NEW_PROJECT` | ideia ou repositório vazio | fundação mínima aprovada |
| `ADOPT_PROJECT` | código, docs ou histórico existente | verdade recuperada e adoção em etapas |
| `EVOLVE_PROJECT` | projeto entendido recebendo mudança | slice coerente e contexto alinhado |

## O que a suíte orienta

- discovery de produto e regras de negócio;
- contextos canônicos e índice de ownership;
- opções de arquitetura e tradeoffs;
- diagramas Mermaid;
- ADRs;
- feature slices, edge cases e gates humanos;
- estratégia de testes, qualidade e entrega;
- auditoria de contexto e handoff entre sessões;
- skills e subagents específicos como adaptadores opcionais.

Templates são pontos de partida, não uma obrigação de gerar todos os documentos.

## Papéis

```text
Humano: propósito, prioridades, regras de negócio, risco e aceite
Agente: discovery, opções, implementação, testes, documentação e evidências
Repositório: verdade canônica, decisões, guardrails e memória durável
```

Uma proposta do agente não é decisão final.

## CLI opcional

O fluxo determinístico continua disponível para quem quiser aplicação de packs
com plano revisável, proteção de conflitos e aprovação por fingerprint:

```text
manifesto -> plano -> aprovação humana -> apply -> verify
```

Ele é uma ferramenta auxiliar, não um requisito de entrada.

Licensed under Apache-2.0.
