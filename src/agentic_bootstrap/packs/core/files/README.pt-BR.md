# Guia rápido

Este pack ajuda qualquer agente capaz a descobrir, estruturar, documentar e
evoluir um projeto sem amarrá-lo a um player ou stack específica.

## Comece aqui

1. Peça ao agente para ler `START_HERE.md`.
2. Confirme `NEW_PROJECT`, `ADOPT_PROJECT` ou `EVOLVE_PROJECT`.
3. Rode o discovery estrutural opcional:

   ```bash
   python3 tools/discover_project.py --target . --format markdown
   ```

4. O agente deve separar fatos, inferências, desconhecidos e propostas.
5. Responda às perguntas de produto e regras de negócio.
6. Aprove decisões materiais antes da geração ou implementação.
7. Rode `python3 tools/context_check.py` antes de encerrar a adoção.

O pack é orientação, não decisão final. Crie somente contextos, diagramas, ADRs
e tooling que resolvam uma necessidade real do projeto.

Players específicos podem usar adapters, skills ou subagents opcionais. A
verdade durável continua nos owners canônicos do repositório.
