# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — it's a documentation/coursework repository (Link School of Business) built entirely in Portuguese Markdown. There is no build, lint, or test tooling; there is no source code to run. The work product is the Markdown content itself, produced through iterative AI prompting.

The subject is a real operational problem at Agência Samba (an experience/events agency, part of Holding Clube): after the agency wins a client pitch, there's no standardized handoff between the Creative team and the Account team to turn a creative concept into a cost estimate — leading to slow, inconsistent budgeting cycles (ranging from weeks to four months).

## Repository structure

- [`problema.md`](problema.md) — the root problem statement (who suffers, current state, desired change, success criteria). This is the anchor document; every other file either provides context for it or works toward solving it.
- [`contexto/`](contexto/) — background files that must be treated as ground truth before proposing or revising anything:
  - [`sobre-mim.md`](contexto/sobre-mim.md) — who the author is, their role at Samba, and how they prefer to collaborate (build reasoning in stages — problem → personas/flow → MVP info → architecture/code — rather than jumping straight to a solution).
  - [`negocio.md`](contexto/negocio.md) — what Samba sells, to whom, and its (partially unconfirmed) business model.
  - [`cliente.md`](contexto/cliente.md) — who buys, why, and open questions about churn/complaints.
  - [`processo-precificacao.md`](contexto/processo-precificacao.md) — the current, living output: the standardized pricing process (Creative → Account handoff) that gets iterated on. Treat this file as the "vigente" (current) version to refine, not to regenerate from scratch.
- [`prompts/`](prompts/) — the versioned history of the prompt used to generate/refine `processo-precificacao.md` (V1 → V2 → V3 → Final). `promptFinal.md` is the reusable prompt intended to be re-run in future rounds without manual editing.

## Key conventions

- **Language**: all content is written in Brazilian Portuguese. Match that unless told otherwise.
- **"Não confirmado internamente"**: several files explicitly flag facts that are inferred or hypothesized rather than verified with Samba internally. Preserve this distinction — never quietly convert an unconfirmed hypothesis into a stated fact when editing these files.
- **Cross-linking**: files reference each other with relative Markdown links (e.g. `[negocio.md](negocio.md)`, `[problema.md](../problema.md)`). Keep these links valid and use the same pattern when adding new context.
- **Iterative refinement, not regeneration**: `processo-precificacao.md` is meant to be revised in place, version over version — each revision documents what changed and why (see its own "O que mudou em relação à versão anterior" section) rather than being rewritten from a blank slate.
- **Symbolic values only**: cost ranges in examples use symbolic tiers (`$` to `$$$$`), never real Samba figures. Do not invent real costs, prices, or margins.
- **Scope discipline**: the process explicitly avoids turning the Creative team into a finance team and avoids proposing complex tooling — solutions should work with the team/tools Samba already has.

## Working in this repo

- When asked to revise the pricing process, read `problema.md`, `contexto/negocio.md`, `contexto/cliente.md`, and the current `contexto/processo-precificacao.md` first, then treat the current process version as the baseline to refine — don't discard it.
- When asked to iterate on the prompt itself, follow the pattern in `prompts/`: each new version documents a critique of the prior version (what was ambiguous, missing, redundant, or conflicting) before producing the revised prompt.
- Follow the collaboration style in `contexto/sobre-mim.md`: build up understanding in stages (problem → personas/flow → MVP definition → architecture/code) rather than jumping straight to implementation, and prefer structured, detailed context over terse answers.
