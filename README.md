# vital-info-translations

> Translate vetted public-health & safety guidance into low-resource languages.  ·  **Risk tier:** medium  ·  **Status:** proposed (planning)

Translate vetted, life-critical public-health and safety guidance (first aid, maternal/child
health, vaccine info, disaster preparedness, water/sanitation) into low-resource languages.
Extends the existing `health-info-translations` pilot from a single factsheet to a standing,
multi-source, multi-language program.

**Definition of shipped:** A reviewed, correctly-licensed translation set delivered to and adopted by a partner NGO/health authority.

This is an **Elyos** good-deed project. Contributors pull a task, do it with their own coding agent, and open a PR. Platform: https://github.com/jdev1977/elyos

## Planning
- [PROPOSAL.md](./PROPOSAL.md) — why this qualifies as a good deed (Good Deed Definition)
- [PLAN.md](./PLAN.md) — architecture, roadmap & milestones, risks
- [TASKS.md](./TASKS.md) — the full task backlog
- [tasks/](./tasks/) — ready-to-pull task JSON(s)

## Contribute
```bash
elyos browse
elyos pull --task-file tasks/vital-info-translations-sources-001.json --repo Elyos-Projects/vital-info-translations
# do the work with your own agent, then:
elyos submit vital-info-translations-sources-001 --repo Elyos-Projects/vital-info-translations
```

## Licensing & review
- **Licensing:** Content: source-compatible (e.g. WHO terms) / CC-BY where original. Tooling: MIT.
- **Review:** risk tier **medium** — deeds are *delivered, not merged*; a domain reviewer must sign off before merge.

> Status: this project is in **planning** and not yet ratified through Elyos governance; no adopting partner/requestor is secured yet (`verifiedNeed: false` on delivery-dependent tasks).
