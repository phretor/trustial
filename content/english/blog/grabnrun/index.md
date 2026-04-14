---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Grab 'n Run: Secure dynamic code loading for Android"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: ["DCL"]
categories: ["Mobile", "Security"]
date: 2015-08-05T17:34:45+02:00
featured: false
draft: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

A simple and effective Java Library that you can easily add to your Android
projects to perform secure dynamic class loading operations.

<!--more-->

The standard
[DexClassLoader](https://developer.android.com/reference/dalvik/system/DexClassLoader.html) is not secure, so one single mistake could open the application (and, therefore,
the entire device) to serious security vulnerabilities, such as remote code
execution. The main goal of Grab's Run is to offer an alternative to the native
Android APIs, and its design enforces that even the most inexperienced
developer cannot perform well-known, serious mistakes.

Check out the source code: [github.com/lukeFalsina/Grab-n-Run](https://github.com/lukeFalsina/Grab-n-Run)
