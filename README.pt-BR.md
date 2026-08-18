# Agentic Project Bootstrap

Aponte qualquer agente de código capaz para um único arquivo e ofereça a ele
uma forma disciplinada de descobrir, estruturar, documentar e evoluir um projeto
junto com você.

Não depende de modelo, IDE, agente, conta ou instalação específica. Este é um
pack portátil de orientação: ajuda o agente a encontrar evidências, fazer boas
perguntas, propor opções e preservar contexto durável. O humano continua sendo
o responsável pelo produto e pelas decisões.

> Estado: release candidate `0.2.0-alpha.3`. O onboarding agent-first e o discovery read-only já
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

A orientação legível diretamente no repositório é o produto principal e não
exige instalação. As releases também incluem um wheel Python para a CLI
opcional; use o wheel anexado à release correspondente e confira o checksum
publicado antes de instalar.

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

## Evidências de entregas reais

A [biblioteca de cases](case-studies/) extrai processo reutilizável de entregas
privadas bem-sucedidas sem publicar identidade, domínio de negócio, dados,
infraestrutura ou histórico dos repositórios de origem.

- **Project Relay** aborda um produto Flutter e Kotlin/Spring conduzido por
  agentes, com contratos, CI, containers, regressão visual e validação em device.
- **Project Aurora** aborda um site comercial conduzido por agentes, do discovery
  e direção visual até produção, indexação e handoff.

Os nomes e cenários são fictícios. Cada case diferencia evidência verificada em
fonte privada, resultado relatado pelo owner e ilustração sintética. A fronteira
de publicação está em
[Learning From Real Projects](docs/guides/REAL_PROJECT_LEARNING.md).

## Filosofia de design

O método aplica explicitamente ideias de John Ousterhout em *A Philosophy of
Software Design*. Os agentes são orientados a reduzir carga cognitiva e
amplificação de mudanças, esconder informação, preferir módulos profundos com
interfaces pequenas e evitar wrappers rasos ou owners duplicados. Consulte a
[filosofia de design](docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md).

Esta é uma aplicação prática das ideias do livro à entrega conduzida por agentes,
sem alegação de afiliação ou endosso do autor.

## Papéis

```text
Humano: propósito, prioridades, regras de negócio, risco e aceite
Agente: discovery, opções, implementação, testes, documentação e evidências
Repositório: verdade canônica, decisões, guardrails e memória durável
```

Uma proposta do agente não é decisão final.

## Ownership e upgrades na alpha

Depois da adoção, os arquivos gerados pertencem ao repositório consumidor. Esta
alpha não atualiza, remove nem reverte esses arquivos automaticamente. Um novo
planejamento classifica modificações locais e conflitos, mas não funciona como
um force-update oculto. Trate mudanças upstream como propostas e adote somente
o que o owner do projeto aprovar.

## CLI opcional

O fluxo determinístico continua disponível para quem quiser aplicação de packs
com plano revisável, proteção de conflitos e aprovação por fingerprint:

```text
manifesto -> plano -> aprovação humana -> apply -> verify
```

Ele é uma ferramenta auxiliar, não um requisito de entrada.

Licensed under Apache-2.0.
