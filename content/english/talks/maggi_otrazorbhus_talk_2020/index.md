---
title: "OTRazor: Static Code Analysis for Vulnerability Discovery in Industrial Automation Scripts"
date: 2020-08-05
publishDate: 2020-06-05T00:00:00Z
lastmod: 2020-06-07T14:31:32.581445Z
authors: ["Federico Maggi", "Marcello Pogliani", "Davide Quarta", "Stefano Zanero", "Marco Balduzzi"]
publication_types: ["3"]
abstract: "In this talk, we delve into industrial robot programming, focusing on the security issues arising from the design and implementation choices of these platforms.  Industrial robot manufacturers provide proprietary, domain-specific programming languages to operate these complex machines. Mostly focused on movement instructions, such programming languages also provide access to low-level system resources like files and network access, and some even allow dynamic code loading. While useful, these features can lead to unsafe programming patterns such as input-validation vulnerabilities or malware-like functionalities, especially if the underlying environment provides no resource isolation like those found in modern operating systems.  After describing the technical features of the languages by eight leading manufacturers, we'll share several cases of vulnerable and malicious usage. We'll then present a static code analyzer that we created and patented, to scan robotic programs and discover unsafe code patterns. Our evaluation on 50 automation programs show that unsafe patterns are indeed found in real-world code, and that static source code analysis is an effective defense tool in the short term.  We conclude by discussing the remediation steps that can be adopted by developers and vendors to mitigate such issues in the medium and long term."
featured: false
location: "Las Vegas, US"
howpublished: "Peer-reviewed Talk"
event: "Black Hat Briefings USA"
event_url: "https://www.blackhat.com/us-20/briefings/schedule/index.html#otrazor-static-code-analysis-for-vulnerability-discovery-in-industrial-automation-scripts-19523"
url_video: https://www.youtube.com/watch?v=PhiuMbVMN_k
---

