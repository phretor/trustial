---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Droydseuss: Android Malware Tracking and Intelligence"
description: "We wanted to create a malware tracker similar to ZeusTracker, but for mobile bankers."
author: "Federico Maggi"
tags: []
categories: [Malware, Mobile]
date: 2016-02-05T17:34:04+02:00
featured: false
draft: false
aliases:
  - /diary/2016/02/05/droydseuss

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

We wanted to create a malware tracker similar to ZeusTracker, but for mobile bankers. So we built a tool, DroydSeuss, which uses static analysis to extract relevant C&C endpoints (e.g., phone number, web URLs) and monitors them by running each sample in a sandbox on a daily basis.

<!--more-->

On top of this, DroydSeuss attaches meta data to both C&C endpoints and malware samples (e.g., country, code feature) that are used to mine association rules. These rules are automatically extracted and can tell useful information such as “there is a group of malware samples that seem to be coming from the same author spreading in a certain country”.

We made the tool public and immediately attracted other researcher’s attention. Thanks to the data feed produced by DroydSeuss we were able to find (and confirm) one malware campaign spreading against Chinese and Korean bank customers and to discover a strange, rare sample that was using Baidu as a C&C.

_(Update: Jun 6th, 2020)_ We decided not to maintain the web service anymore. We only keep the URL here for hystorical reasons: [http://droydseuss.necst.it](http://droydseuss.necst.it)

## References
