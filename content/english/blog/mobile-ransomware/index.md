---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Mobile (Android) Ransomware"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: [android, mobile, ransomware, Black Hat, Trendmicro]
categories: ["Mobile", "Malware", "Ransomware"]
date: 2016-12-08T01:32:15+02:00
featured: false
draft: false
aliases:
  - /diary/2016/12/08/mobile-ransomware/

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
I've started this project while advising a Master student who was interested
in machine learning. As I've been using machine learning since around 2006, I
was immediately hooked by the idea of using it to determine whether an
Android app was trying to lock the target device as part of a ransomware
scheme.

<!--more-->

There are three core characteristics that are unavoidable for any ransomware
scheme, which can be all boiled down to the "business" need of "being noisy"
and evident. It's true right? For the first time we see malware that is no
longer trying to hide. Instead, it needs to loudly announce its presence to the
victim, in order for the business model to work. If the victim is not aware of
what is happening and is not effectively guided to the payment screen, the
infection is useless.

Therefore, any ransomware needs to:

1. encrypt or lock access to important data,
2. announce its presence to the user and,
3. guide them through the payment options.

These three features **have to be implemented** by a ransomware sample, and
thus have to be visible somehow in the code. Around this key observation,
together with the evil genius [Nicolò Andronio](https://www.andronio.me/) (the
aforementioned Master student) and my partner-in-crime
[Stefano](https://twitter.com/raistolo), we devised and open-sourced
[HelDroid](https://github.com/necst/heldroid), a fully automatic APK analyzer
that, using static flow analysis, detects whether an app contains evidence of
ransomware behavior.

Earlier this summer I've joined [Trend Micro](https://www.trendmicro.com)'s
research team, and immediately got my hands onto MARS, its [Mobile App
Reputation Service](https://mars.trendmicro.com/), which allowed me to build
a good retrospective view of how Android ransomware have evolved.

This work granted me a speaking slot at the Black Hat Europe Briefings, where
I had the opportunity to present the results to a room packed with attendees.
Was a great experience!

If you're curious, you can read a summarized version of the research in these
two blog posts:

* [Mobile Ransomware: Pocket-Sized Badness](https://blog.trendmicro.com/trendlabs-security-intelligence/mobile-ransomware-pocket-sized-badness/)
* [Mobile Ransomware: How to Protect Against It](https://blog.trendmicro.com/trendlabs-security-intelligence/mobile-ransomware-protect/)

Here's the [web service (archived)](https://web.archive.org/web/20180216035340/http://ransom.mobi/) in case you want to check it out.
