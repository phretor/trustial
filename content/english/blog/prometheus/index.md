---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Prometheus: Automatic signature generation for WebInject-based banking trojan detection"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: [Webinject]
categories: ["Malware"]
date: 2017-06-12T17:34:19+02:00
featured: false
draft: false

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

The goal of this project is to extract signatures that capture the WebInject behavior of
trojans. WebInject-based trojans are still the most popular e-crime tool.

<!--more-->

Prometheus (formerly Zarathustra) is based on a technique that we call web page
differential analysis, which extracts and generates a model of the differences
between a web page visited from an infected (virtual) machine and the very same
page visited from a clean machine. These differences are unavoidable for the
malware to carry out its functionality, and thus allow to create robust
indicators of compromise. We generalize these differences using custom
heuristics to reduce the chances of false positives.
