---
title: "Leveraging Flawed Tutorials for Seeding Large-Scale Web Vulnerability Discovery"
date: 2017-08-01
publishDate: 2017-08-01T00:00:00Z
lastmod: 2020-06-05T09:09:58.869480Z
authors: ["Tommi Unruh", "Bhargava Shastry", "Malte Skoruppa", "Federico Maggi", "Konrad Rieck", "Jean-Pierre Seifert", "Fabian Yamaguchi"]
publication_types: ["1"]
abstract: "The Web is replete with tutorial-style content on how to accomplish programming tasks. Unfortunately, even top-ranked tutorials suffer from severe security vulnerabilities, such as cross-site scripting (XSS), and SQL injection (SQLi). Assuming that these tutorials influence real-world software development, we hypothesize that code snippets from popular tutorials can be used to bootstrap vulnerability discovery at scale. To validate our hypothesis, we propose a semi-automated approach to find recurring vulnerabilities starting from a handful of top-ranked tutorials that contain vulnerable code snippets. We evaluate our approach by performing an analysis of tens of thousands of open-source web applications to check if vulnerabilities originating in the selected tutorials recur. Our analysis framework has been running on a standard PC, analyzed 64,415 PHP codebases hosted on GitHub thus far, and found a total of 117 vulnerabilities that have a strong syntactic similarity to vulnerable code snippets present in popular tutorials. In addition to shedding light on the anecdotal belief that programmers reuse web tutorial code in an ad hoc manner, our study finds disconcerting evidence of insufficiently reviewed tutorials compromising the security of open-source projects. Moreover, our findings testify to the feasibility of large-scale vulnerability discovery using poorly written tutorials as a starting point."
featured: false
location: "Vancouver, BC"
publication: "Proceedings of the 11th USENIX Workshop on Offensive Technologies (WOOT 17)"
tags: ["workshop"]
url_pdf: "https://www.usenix.org/conference/woot17/workshop-program/presentation/unruh"
---

