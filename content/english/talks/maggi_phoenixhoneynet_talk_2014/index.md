---
title: "Tracking and Characterizing Botnets Using Automatically Generated Domains"
date: 2014-05-14
publishDate: 2014-05-14T00:00:00Z
lastmod: 2020-06-05T09:07:15.376016Z
authors: ["Federico Maggi"]
publication_types: ["3"]
abstract: "Modern botnets rely on domain-generation algorithms (DGAs) to build resilient command-and-control infrastructures. Recent works focus on recognizing automatically generated domains (AGDs) from DNS traffic, which potentially allows to identify previously unknown AGDs to hinder or disrupt botnets' communication capabilities. The state-of-the-art approaches require to deploy low-level DNS sensors to access data whose collection poses practical and privacy issues, making their adoption problematic. We propose a mechanism that overcomes the above limitations by analyzing DNS traffic data through a combination of linguistic and IP-based features of suspicious domains. In this way, we are able to identify AGD names, characterize their DGAs and isolate logical groups of domains that represent the respective botnets. Moreover, our system enriches these groups with new, previously unknown AGD names, and produce novel knowledge about the evolving behavior of each tracked botnet. We used our system in real-world settings, to help researchers that requested intelligence on suspicious domains and were able to label them as belonging to the correct botnet automatically. Additionally, we ran an evaluation on 1,153,516 domains, including AGDs from both modern (e.g., Bamital) and traditional (e.g., Conficker, Torpig) botnets. Our approach correctly isolated families of AGDs that belonged to distinct DGAs, and set automatically generated from non-automatically generated domains apart in 94.8 percent of the cases."
featured: false
location: "Warsaw, Poland"
howpublished: "Invited Talk"
event: "Honeynet Workshop"
---
