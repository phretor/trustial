---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Banksealer: Automatic Banking Fraud Detection"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: []
categories: ["Fraud", "Malware", "Anomaly Detection"]
date: 2016-06-05T17:34:12+02:00
featured: false
draft: false
aliases:
  - /diary/2016/06/05/banksealer/

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

We started this project because we wanted to analyze banking and credit-card
transactions and, with as little knowledge as possible, predict whether new
ones are fraudulent or not (e.g., due to a banking trojan working on the
victim’s computer, made by a cyber criminal with stolen credentials).

<!--more-->

BankSealer is based on lightweight statistical learning on feature models
(e.g., amount, timestamp, recipient country, description) extracted by each
transaction. BankSealer is currently deployed at one of the largest Italian
banks and has been proven effective at detecting frauds, to the point that my
co-authors have created a startup out of it!

Banksealer is now a fintech startup: [https://banksealer.com](https://banksealer.com)
