---
title: "HelDroid: Dissecting and Detecting Mobile Ransomware"
date: 2015-10-01
publishDate: 2015-10-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.280206Z
authors: ["Niccolò Andronio", "Stefano Zanero", "Federico Maggi"]
publication_types: ["1"]
abstract: "In ransomware attacks, the actual target is the human, as opposed to the classic attacks that abuse the infected devices (e.g., botnet renting, information stealing). Mobile devices are by no means immune to ransomware attacks. However, there is little research work on this matter and only traditional protections are available. Even state-of-the-art mobile malware detection approaches are ineffective against ransomware apps because of the subtle attack scheme. As a consequence, the ample attack surface formed by the billion mobile devices is left unprotected. First, in this work we summarize the results of our analysis of the existing mobile ransomware families, describing their common characteristics. Second, we present HelDroid, a fast, efficient and fully automated approach that recognizes known and unknown scareware and ransomware samples from goodware. Our approach is based on detecting the ``build- ing blocks'' that are typically needed to implement a mobile ransomware application. Specifically, HelDroid detects, in a generic way, if an app is attempting to lock or encrypt the device without the user’s consent, and if ransom requests are displayed on the screen. Our technique works without requiring that a sample of a certain family is available beforehand. We implemented HelDroid and tested it on real-world Android ransomware samples. On a large dataset comprising hundreds of thousands of APKs including goodware, malware, scareware, and ransomware, HelDroid exhibited nearly zero false positives and the capability of recognizing unknown ransomware samples. "
featured: false
location: "Kyoto, Japan"
pages: "382--404"
series: "Lecture Notes in Computer Science"
publication: "International Symposium on Research in Attacks, Intrusions and Defenses (RAID)"
---

