---
title: "Trellis: Privilege Separation for Multi-User Applications Made Easy"
date: 2016-09-01
publishDate: 2016-09-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.254792Z
authors: ["Andrea Mambretti", "Kaan Onarlioglu", "Collin Mulliner", "William Robertson", "Engin Kirda", "Federico Maggi", "Stefano Zanero"]
publication_types: ["1"]
abstract: "Operating systems provide a wide variety of resource isolation and access control mechanisms, ranging from traditional user-based security models to fine-grained permission systems as found in modern mobile operating systems. However, comparatively little assistance is available for defining and enforcing access control policies within multiuser applications. These applications, often found in enterprise environments, allow multiple users to operate at different privilege levels in terms of exercising application functionality and accessing data. Developers of such applications bear a heavy burden in ensuring that security policies over code and data in this setting are properly expressed and enforced. We present Trellis, an approach for expressing hierarchical access control policies in applications and enforcing these policies during execution. The approach enhances the development toolchain to allow programmers to partially annotate code and data with simple privilege level tags, and uses a static analysis to infer suitable tags for the entire application. At runtime, policies are extracted from the resulting binaries and are enforced by a modified operating system kernel. Our evaluation demonstrates that this approach effectively supports the development of secure multi-user applications with modest runtime performance overhead."
featured: false
location: "Paris, France"
pages: "437--456"
publication: "International Symposium on Research in Attacks, Intrusions and Defenses (RAID)"
---

