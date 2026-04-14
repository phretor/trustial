---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "AndRadar: Mobile app Marketplace Monitoring and Reputation Analysis"
summary: ""
author: "Federico Maggi"
categories: ["Mobile", "Malware"]
date: 2014-06-07T11:25:36+02:00
featured: false
draft: false
aliases:
  - /diary/2014/06/07/andradar/

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

The main goal of this project is to provide a dashboard to analyze and monitor the spreading of Android malware in marketplaces. AndRadar uses lightweight fingerprints to lookup malware samples without the need to download them from the markets.

<!--more-->

Once a matching app is found, AndRadar tracks its page, developer, and any kind of meta data associated to it. AndRadar’s data is then crunched into a set of indicators that summarize, for example, the efficiency of a malware author in publishing its app, the speed of the market in responding to threats, etc., and provide an overall reputation of each developer, market and app. By combining data coming from different marketplaces, AndRadar can track spreading campaigns also across markets. No such tool like AndRadar exists so far, so we released it to the public.

The (unmaintained) web application is at: [http://andradar.hosting.necst.it](http://andradar.hosting.necst.it)
