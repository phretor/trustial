---
title: "A Comprehensive Black-box Methodology for Testing the Forensic Characteristics of Solid-state Drives"
date: 2013-12-01
publishDate: 2013-12-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.399456Z
authors: ["Gabriele Bonetti", "Marco Viglione", "Alessandro Frossi", "Federico Maggi", "Stefano Zanero"]
publication_types: ["1"]
abstract: "Solid-state drives (SSDs) are inherently different from traditional drives, as they incorporate data-optimization mechanisms to overcome their limitations (such as a limited number of program-erase cycles, or the need of blanking a block before writing). The most common optimizations are wear leveling, trimming, compression, and garbage collection, which operate transparently to the host OS and, in certain cases, even when the disks are disconnected from a computer (but still powered up). In simple words, SSD controllers are designed to hide these internals completely, rendering them inaccessible if not through direct acquisition of the memory cells. These optimizations have a significant impact on the forensic analysis of SSDs. The main cause is that memory cells could be pre-emptively blanked, whereas a traditional drive sector would need to be explicitly rewritten to physically wipe off the data. Unfortunately, the existing literature on this subject is sparse and the conclusions are seemingly contradictory. In this paper we propose a generic, practical, test-driven methodology that guides researchers and forensics analysts through a series of steps that assess the \"forensic friendliness\" of a SSD. Given a drive of the same brand and model of the one under analysis, our methodology produces a decision that helps an analyst to determine whether or not an expensive direct acquisition of the memory cells is worth the effort, because the extreme optimizations may have rendered the data unreadable or useless. We apply our methodology to three SSDs produced by top vendors (Samsung, Corsair, and Crucial), and provide a detailed description of how each step should be conducted."
featured: false
location: "New York, NY, USA"
pages: "269--278"
series: "ACSAC '13"
isbn: "978-1-4503-2015-3"
publication: "Proceedings of the 29th Annual Computer Security Applications Conference"
url_pdf: "http://doi.acm.org/10.1145/2523649.2523660"
---

