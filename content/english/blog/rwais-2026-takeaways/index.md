---
title: "My Takeaways from The Real World AI Security Conference at Stanford"
description: "Highlights and key signals from the first edition of RWAIS 2026, covering agent security, confidential computing for agents, and AI-driven vulnerability discovery at scale."
summary: "The security industry is catching up fast to AI agents. Most current work focuses on securing agents rather than using AI for security. Here are my takeaways from the first Real World AI Security conference at Stanford."
author: "Federico Maggi"
tags: ["ai-security", "agent-security", "conference-notes"]
categories: ["AI Security"]
date: 2026-06-26T00:00:00-07:00
lastmod: 2026-06-26T00:00:00-07:00
featured: false
draft: false
image: featured.png
---

Here are my takeaways from the [The Real World AI Security conference 2026](https://seclab.stanford.edu/RealWorldAIsec/). It's the first edition but, given the energy, I expect it to be way bigger next year! Organizers at the [Stanford Security Lab](https://seclab.stanford.edu) did a great job. There were folks taking Caltrain from the nearby Confidential Computing Summit 2026 to check RWAIS out!

The conference had a good balance between academics, practitioners, founders, and hackers.

The industry is moving fast on AI agents, with applications already looking into 2-3 years from now, when agents will be more connected to the physical world. I've spoken with founders about a market of gateways to connect agents to legacy systems which are currently running many critical real-world applications. The security industry is catching up very fast. I've heard more about "how to secure agents" than "how to use agents *for* security."

What follows is my summary and the key signals I took away from the talks.

I'm leaving the quotes anonymous because I don't know if the speakers want to be quoted. The recordings will be made public, so you'll be able to track down who said what.

## Takeaways

- Most current security work focuses on securing AI agents rather than using AI for security.
- Security teams and startups are building sandboxes, gateways, and policy enforcement layers for agent tool use and external service calls.
- Agent exploitation is a major concern, including attacks beyond prompt injection and the possibility of agentic worms spreading across systems.
- Agents should be treated more like potential malicious insiders than ordinary software.
- Zero trust principles are necessary because we must accept that some agents are compromised, in the same way we accept some humans are insider attackers.
- Model guardrails are useful as a first layer but should not be trusted for final security decisions.
- As with malware, detonation chambers for agents are a must-have investment for containment, observability, and behavior analysis of agents—interactions with tools, networks, filesystems, and hosts.
- Using agents for vulnerability discovery requires realistic staging environments that replicate target systems.
- Confidential/attested environments for verifiable agent computation are seen as a major but underdeveloped need: confidential computing will need to support provable computation, encrypted execution, and future use cases such as financial transactions.
- While AI-assisted vulnerability discovery and PoC is as advanced as a swarm of capable hackers able to explore uncharted territories of any code and systems, AI-assisted patching remains an unresolved problem.
- Human-only capture-the-flag competitions may become important for preserving human creative security work.

## Defending from agents before securing with agents

The main themes were **securing agents**, studying their **behavior** and **containing their actions** (e.g., tool use) in controlled environments, and anticipating exploitation techniques including prompt injection at scale, agent worms, and tool misuse in more sophisticated ways.

The threats to AI agents are not limited to prompt bugs. They affect confidentiality, integrity, and availability: the attack surface includes memory, configuration, tools, browser sessions, and cross-agent interactions, making this ordinary security engineering with AI-shaped failure modes.

> "The threat model is no longer just 'can the model be tricked into saying something bad?' It is increasingly 'can the agent be manipulated into taking actions across systems?'"

The practical takeaway here was that we should treat AI agents like potentially compromised insiders. That pushes teams toward zero trust, stronger containment, better observability, and realistic staging environments for security testing. This means not relying on model guardrails alone. I think of model guardrails as the equivalent of client-side validation in webapps: it's weak, a necessary convenience, but not sufficient for security assurance. Users and administrators must be conscious that agents do take weird paths.

A third major "silent" thread in the hallway con was **confidential and attested environments for agentic computation**. Confidential computing and proof of computation (e.g., this boot chain is reproducible and I can verify it) have been around for quite a while, but the realization that agents can do more stuff for us, faster than deterministic compute, and that they will be connected to the physical world to process confidential data and run critical systems...it's acting as a catalyst to accelerate the deployment of confidential compute, verifiable agent work, and *true* sandboxes (i.e., not `cgroup` based :-P).

## Securing with agents: the new, global security game

As I said, using AI for security wasn't the biggest theme, but it's a theme that is being heavily discussed and debated among security folks.

What I take away from the conference is that the **biggest transformation that language models bring to cybersecurity** is not (yet) a new kind of reasoning (e.g., exploits we won't be able to understand), it's the **scale**. Security tasks that were once feasible only for a single human can now be applied to millions of items, and offense benefits more than defense because exploit success is easier to verify than defense robustness.

> "Quantity has a quality of its own."

The same week, although not part of the conference, two major initiatives were launched. [Patch the Planet: a Daybreak initiative to support open source maintainers \| OpenAI](https://openai.com/index/patch-the-planet/) (best punchline ever, love it!), an initiative built with [Trail of Bits](https://trailofbits.com/patch-the-planet/) to help maintainers secure critical open-source software. The Linux Foundation launched [Akrites](https://akrites.org/), a coordinated effort backed by AWS, Anthropic, Chainguard, Cisco, Citi, Google, IBM, JPMorganChase, Microsoft, NVIDIA, OpenAI, Red Hat, and others to address exactly this problem. Akrites creates a shared SIRT and standardized disclosure process to fix upstream before exploits hit.

## Closing thoughts

AI agents are moving into production faster than the ecosystem is securing them. The big gap is still a trustworthy _infrastructure_ for running agents safely and repeatably. We don't have that at scale.

The interesting work now is not just building agents, but building the infrastructure around them for containment, observability, and zero trust boundaries. Most of all: we need realistic but controlled test environments to let the agents run wild and confirm the vulns that other agents claim. This brings me back to the times when the first malware sandboxes started to appear **PoC||GTAO = PoC or Get That Agent Out** is a necessary step in the prioritization game. [Vulnerability Reports Are Not Special Anymore](https://words.filippo.io/vuln-reports/), and they get less special w/o a reproducible proof and careful threat modeling.

This is a great time to be working in security.
