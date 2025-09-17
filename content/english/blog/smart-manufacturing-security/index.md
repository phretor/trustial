---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Smart Manufacturing Security"
subtitle: ""
summary: ""
tags: []
categories: [Operational Technology Security]
date: 2020-06-08T07:19:15+02:00
lastmod: 2020-06-08T07:19:15+02:00
featured: false
draft: false
image: featured.jpg
projects: []
---

How do we secure a smart manufacturing system, or a smart factory? Recent incidents such as the [ransomware infection that halted production at a major semiconductor foundry in 2018](https://thehackernews.com/2018/08/tsmc-wannacry-ransomware-attack.html) have already shown the impact of IT-to-OT lateral movement. Moreover, while smart manufacturing systems are isolated from other networks, there is a trend toward less isolation between IT and OT systems.

<!--more-->

My personal advise is to **learn how to think as an attacker**. Knowing the current threats and countermeasures is indispensable, but you need to **run an extra mile** and strive to think about _other_ ways that such a complex system can get compromised.

In this series of brief videos, I'll go through a recent paper that I worked on: a collaborative research between [Trend Micro Research](https://trendmicro.com) and [Politecnico di Milano](https://polimi.it).

## Ep. 1: Introduction to Smart Manufacturing Security

In this video we start by taking a look at how a smart manufacturing system actually looks like, using the system that we have used during our research.
Although it's an educational lab, it uses the same equipment used in real modern factories.

{{< youtube 7q7eun--K30 >}}<br />

There are 7 stations, each controlled by a dedicated PLC and an HMI for the operator to interact with the system, for maintenance or troubleshooting for example. The goal of the plant is to produce cell phones (actually, toy cell phones) with a case and a printed circuit board inside. The whole system is controlled by a so-called MES (or manufacturing execution system) which is a scheduling software that make sure that each PLC receives the right control command at the right time, and that all the parts needed to produce an item are available.

The SIEMENS equipment (such as the HMIs and PLCs) communicate via S7, which is a proprietary control protocol by SIEMENS. The MES and other components communicate via Modbus and OPC Unified Architecture, which is an open machine-to-machine protocol for industrial automation
There's a lot of "backstage" work done by the engineers who setup these systems, which is normally carried out by the so-called "engineering workstation": it's a computer with industrial automation programming software installed, normally directly connected to all the machines.

Although the trend is towards more and more connected smart manufacturing systems, we're assuming a conservative scenario, in which none of these systems is directly reachable from the Internet.

We conclude the video with the questions that we wanted to answer with this research:

1. **Under which conditions are certain attacks possible, and what is their impact?** Of course even a simple ransomware or any other "traditional" IT attacks can have repercussions on the OT environment, even if that wasn't the primary goal of the attacker. But we're more interested in attacks against the specific smart-manufacturing technology
2. **Are there any overlooked attack vectors that could make the attacker's job easier?** We're interested in non-mainstream opportunities, or techniques that attackers could use to "fly under the radar" or that we think they'll use in the future.
3. **What is the security impact of the current software-development practices, including the use of open libraries, with complex interdependencies?** We'll see how a missing check in a library included in the firmware of an industrial device may lead to full compromise of the entire manufacturing plant.
4. **What is the cybersecurity awareness level of the technical personnel who engineer, program, and operate in smart manufacturing environments?** While it's undeniable that the priorities of a perfectly functioning OT system are in contrast with the priorities of a perfectly secure IT system, one of the goals of this research was to understand exactly why this is the case, and what the cybersecurity industry can do about it.

## Ep. 2: Malicious Industrial Software Extensions

In this video we focus on the engineering workstation (EWS), which is a crucial endpoint used to program the logic of a smart manufacturing plant. It's essential in any smart factory station, it should never be exposed or reachable from a public network, but we show that even if not directly reachable, an attacker can still find ways to access it.

{{< youtube jiyb6BKx_TA >}}<br />

In this second episode I show you how future smart factories could be infected via malicious software extensions, a new way to deliver software for industrial automation. Malicious software extensions and future industrial "app stores" represent a relevant but overlooked attack vector for smart factory environments.

Thanks to our research ABB's RobotApps Store has fixed an upload bypass vulnerability that would have allowed anyone to upload (malicious) software extensions that could cripple into the engineering workstation, a critical endpoint used to program industrial machines such as robots.

## Extra Episode: Lateral Movements via Industrial Automation Scripts

In this video we focus on two questions: What if a perfectly patched industrial manufacturing machine can still harbor for vulnerabilities where no one is looking? What if the powerful programming languages used to program these machines can go beyond simple movement instructions, and actually allow threat actors to hide malware into the logic?

{{< youtube g2h2EQWan3E >}}<br />

In this unplanned, extra episode you can see the entire picture, from entry point (already glanced at in the second episode) to vulnerability exploitation and complete system compromise.

And of course we conclude with an overview of the short-, medium-, and long-term remediation approaches.

## Upcoming Videos

In the following videos we'll see:

- how an attacker can access a smart manufacuring system through a trojanized IoT library,
- then we'll see how a weak mobile HMI could facilitate the job of an attacker,
