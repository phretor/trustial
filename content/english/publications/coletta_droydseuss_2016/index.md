---
title: "DroydSeuss: A Mobile Banking Trojan Tracker - Short Paper"
date: 2016-02-01
publishDate: 2016-02-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.261504Z
authors: ["Alberto Coletta", "Victor Van der Veen", "Federico Maggi"]
publication_types: ["1"]
abstract: "After analyzing several Android mobile banking trojans, we observed the presence of repetitive artifacts that describe valuable information about the distribution of this class of malicious apps. Motivated by the high threat level posed by mobile banking trojans and by the lack of publicly available analysis and intelligence tools, we automated the extraction of such artifacts and created a malware tracker named DroydSeuss. DroydSeuss first processes applications both statically and dynamically, extracting relevant strings that contain traces of communication endpoints. Second, it prioritizes the extracted strings based on the APIs that manipulate them. Finally, DroydSeuss correlates the endpoints with descriptive metadata from the samples, providing aggregated statistics, raw data, and cross-sample information that allow researchers to pinpoint relevant groups of applications. We connected DroydSeuss to the VirusTotal daily feed, consuming Android samples that perform banking-trojan activity. We manually analyzed its output and found supporting evidence to confirm its correctness. Remarkably, the most frequent itemset unveiled a campaign currently spreading against Chinese and Korean bank customers.  Although motivated by mobile banking trojans, DroydSeuss can be used to analyze the communication behavior of any suspicious application."
featured: false
series: "Lecture Notes in Computer Science (LNCS)"
publication: "Financial Cryptography and Data Security"
---
