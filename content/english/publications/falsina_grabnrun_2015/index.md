---
title: "Grab 'n Run: Secure and Practical Dynamic Code Loading for Android Applications"
date: 2015-12-01
publishDate: 2015-12-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.266242Z
authors:
  [
    "Luca Falsina",
    "Yanick Fratantonio",
    "Stefano Zanero",
    "Christopher Kruegel",
    "Giovanni Vigna",
    "Federico Maggi",
  ]
publication_types: ["1"]
abstract: "Android introduced the dynamic code loading (DCL) mechanism to allow for code reuse, to achieve extensibility, to enable updating functionalities or to boost application start- up performance. In spite of its wide adoption by developers, implementing DCL in a secure way is challenging, leading to serious vulnerabilities such as remote code injection. Previous academic and community attempts at solving this problem are unfortunately either impractical or incomplete, or in some cases exhibit vulnerabilities. In this paper, we propose, design, implement and test Grab 'n Run, a novel code verification protocol and a series of supporting libraries, APIs, and components, that address the problem by abstracting away from the developer challenging implementation details. Grab 'n Run is designed to be practical: among its tools, it provides a drop-in library, which requires no modifications to the Android framework or the underlying Dalvik/ART runtime, is very similar to the native API, and most code can be automatically rewritten to use it. Grab 'n Run also contains an application rewriting tool, which allows easy porting of existing applications to use the secure API of its library. We evaluate Grab 'n Run library with a user study, obtaining impressive results in vulnerability reduction, ease of use and speed of development. We also show that the performance overhead introduced by our library is negligible. The library is released as free software."
featured: false
location: "Los Angeles, USA"
pages: "201--210"
series: "ACSAC '15"
isbn: "978-1-4503-3682-6"
publication: "Proceedings of the 31st Annual Computer Security Applications Conference"
---
