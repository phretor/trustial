---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Dnsmasq and CVE-2017-1449*: A Reality Check and Remediation Practices"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: ["Trend Micro", Measurement, Vulnerability, DNS]
categories: ["CVE", "Security"]
date: 2017-10-07T15:09:24+02:00
featured: false
draft: false
aliases:
  - /diary/2017/10/09/dnsmasq/

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image: featured.jpg

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Many vulnerabilities in one shot, yet several pre-conditions for a target to
be actually exploitable. Here's simple flowchart to check whether your
Dnsmasq deployments are vulnerable.

<!--more-->

[Dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) is the de-facto tool
to implement DNS and DHCP services in small servers and embedded devices. Being
Dnsmasq user, when [Google Security researchers disclosed the CVE-2017-14491 to
14496
series](https://security.googleblog.com/2017/10/behind-masq-yet-more-dns-and-dhcp.html),
I quickly checked whether my installation was vulnerable.

Turned out that, despite I found a vast amount of devices running a vulnerable
version of Dnsmasq, the chain of pre-conditions for these vulnerabilities to be
exploitable are not super trivial. So I decided to write them down in
a flowchart.

You can read [the full blog post here](http://blog.trendmicro.com/trendlabs-security-intelligence/dnsmasq-reality-check-remediation-practices/)!
