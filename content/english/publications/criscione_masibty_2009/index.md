---
title: "Integrated Detection of Attacks Against Browsers, Web Applications and Databases"
date: 2009-11-09
publishDate: 2009-11-09T00:00:00Z
lastmod: 2020-06-05T08:21:22.513710Z
authors:
  ["Claudio Criscione", "Federico Maggi", "Guido Salvaneschi", "Stefano Zanero"]
publication_types: ["1"]
abstract: "Anomaly-based techniques were exploited successfully to implement protection mechanisms for various systems. Recently, these approaches have been ported to the web domain under the name of ``web application anomaly detectors'' (or firewalls) with promising results. In particular, those capable of automatically building specifications, or models, of the protected application by observing its traffic (e.g., network packets, system calls, or HTTP requests and responses) are particularly interesting, since they can be deployed with little effort. Typically, the detection accuracy of these systems is significantly influenced by the model building phase (often called training), which clearly depends upon the quality of the observed traffic, which should resemble the normal activity of the protected application and must be also free from attacks. Otherwise, detection may result in significant amounts of false positives (i.e., benign events flagged as anomalous) and negatives (i.e., undetected threats). In this work we describe Masibty, a web application anomaly detector that have some interesting properties. First, it requires the training data not to be attack-free. Secondly, not only it protects the monitored application, it also detects and blocks malicious client-side threats before they are sent to the browser. Third, Masibty intercepts the queries before they are sent to the database, correlates them with the corresponding HTTP requests and blocks those deemed anomalous. Both the accuracy and the performance have been evaluated on real-world web applications with interesting results. The system is almost not influenced by the presence of attacks in the training data and shows only a negligible amount of false positives, although this is paid in terms of a slight performance overhead."
featured: false
isbn: "978-0-7695-3983-6"
publication: "Proceedings of the European Conference on Network Defense (EC2ND)"
---
