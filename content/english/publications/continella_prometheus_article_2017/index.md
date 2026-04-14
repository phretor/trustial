---
title: "Prometheus: Analyzing WebInject-based information stealers"
date: 2017-05-02
publishDate: 2017-05-02T00:00:00Z
lastmod: 2020-06-07T09:15:30.519180Z
authors:
  [
    "Andrea Continella",
    "Michele Carminati",
    "Mario Polino",
    "Andrea Lanzi",
    "Stefano Zanero",
    "Federico Maggi",
  ]
publication_types: ["2"]
abstract: "Nowadays Information stealers are reaching high levels of sophistication. The number of families and variants observed increased exponentially in the last years. Furthermore, these trojans are sold on underground markets along with automatic frameworks that include web-based administration panels, builders and customization procedures. From a technical point of view such malware is equipped with a functionality, called WebInject, that exploits API hooking techniques to intercept all sensitive data in a browser context and modify web pages on infected hosts. In this paper we propose Prometheus, an automatic system that is able to analyze trojans that base their attack technique on DOM modifications. Prometheus is able to identify the injection operations performed by malware, and generate signatures based on the injection behavior. Furthermore, it is able to extract the WebInject targets by using memory forensic techniques. We evaluated Prometheus against real-world, online websites and a dataset of distinct variants of financial trojans. In our experiments we show that our approach correctly recognizes known variants of WebInject-based malware and successfully extracts the WebInject targets. "
featured: false
pages: "1--21"
publication: "Journal of Computer Security"
---
