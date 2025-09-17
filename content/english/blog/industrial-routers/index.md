---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "The Role of Industrial Routers in Keeping the Future Factory Secure"
subtitle: ""
summary: ""
author: "Federico Maggi"
tags: [Vulnerability, Trend Micro, IIoT, Routers, Industrial]
categories: [Embedded, Industrial, Security]
date: 2017-05-03T12:39:46+02:00
featured: false
draft: false
aliases:
  - /diary/2017/05/03/industrial-routers/

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

Industrial routers play a very crucial role: a single vulnerability can grant
the attacker access to an entire network of critical machines. In this
research, I've looked at how easy it is for a hypothetical attacker to find
and enumerate industrial routers, and the security posture of their vendors.

<!--more-->

Industrial routers aren't just regular routers in a rugged case. They are the
gateway to networks of *machines*, which usually end up interacting with the
physical world. Think about connected vehicles, factories, robots, and so on.

While working on a remote access box (another name for "industrial router"),
during our [industrial robots research](http://robosec.org), we noticed that
the web-admin panel had an authentication-bypass vulnerability. Upon reporting
the [vulnerability to the vendor, which patched it right
away](https://websupport.ewon.biz/support/news/support/ewon-security-enhancement-fw-112s2-0),
we've wondered: are there other vendors? What's the state of security in this
area?

After going through the "Switches Get Stitches" talks ([44CON 2014](https://www.slideshare.net/44Con/switches-getstitches), [31C3 2014](https://media.ccc.de/v/31c3_-_6196_-_en_-_saal_1_-_201412281130_-_switches_get_stitches_-_eireann_leverett), [Black Hat US 2015](https://www.youtube.com/watch?v=urjKkQaspHQ)),
we had some bad feelings about industrial routers too, so we've started to
collect technical resources like manuals and firmware update files, and crafted
Shodan and Censys search strings to see how many of these routers were directly
exposed to a casual attacker.

The first thing that we've noticed was the abundance of technical information
freely available to the public. Don't get me wrong: I'm not advocating in favor
of "security through obscurity" nor "closed source". Once I believe in
openness, I also believe that critical targets like industrial routers (which
are put in front of supposedly critical machinery), shouldn't be *that* easy
for a casual attacker to discover. Ironically, marketing brochures required
a registration, whereas firmware and technical manuals were directly indexed by
search engines and publicly accessible.

Given the security posture of some vendors, we've decided to take a broad look
at all of them, both from a reconnaissance and vulnerability viewpoint.

If you're curious, head over to the [full article](https://blog.trendmicro.com/trendlabs-security-intelligence/compromising-industrial-robots/) on TrendLab's Security Intelligence Blog.
