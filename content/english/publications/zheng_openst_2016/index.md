---
title: "On-Chip System Call Tracing: A Feasibility Study and Open Prototype"
date: 2016-10-01
publishDate: 2016-10-01T00:00:00Z
lastmod: 2020-06-05T08:21:22.249814Z
authors:
  [
    "Chenghyu Zheng",
    "Mila Dalla Preda",
    "Jorge Granjal",
    "Stefano Zanero",
    "Federico Maggi",
  ]
publication_types: ["1"]
abstract: "Several tools for program tracing and introspection exist. These tools can be used to analyze potentially malicious or untrusted programs. In this setting, it is important to prevent that the target program determines whether it is being traced or not. This is typically achieved by minimizing the code of the introspection routines and any artifact or side-effect that the program can leverage. Indeed, the most recent approaches consist of lightly instrumented operating systems or thin hypervisors running directly on bare metal.  Following this research trend, we investigate the feasibility of transparently tracing a Linux/ARM program without modifying the software stack, while keeping the analysis cost and flexibility compatible with state of the art emulation- or bare-metal-based approaches. As for the typical program tracing task, our goal is to reconstruct the stream of system call invocations along with the respective un-marshalled arguments.  We propose to leverage the availability of on-chip debugging interfaces of modern ARM systems, which are accessible via JTAG. More precisely, we developed OpenST, an open-source prototype tracer that allowed us to analyze the performance overhead and to assess the transparency with respect to evasive, real-world malicious programs. OpenST has two tracing modes: In-kernel dynamic tracing and external tracing. The in-kernel dynamic tracing mode uses the JTAG interface to ``hot-patch'' the system calls at runtime, injecting introspection code. This mode is more transparent than emulator based approaches, but assumes that the traced program does not have access to the kernel memory where the introspection code is loaded. The external tracing mode removes this assumption by using the JTAG interface to manage hardware breakpoints.  Our tests show that OpenST's greater transparency comes at the price of a steep performance penalty. However, with a cost model, we show that OpenST scales better than the state of the art, bare-metal-based approach, while remaining equally stealthy to evasive malware."
featured: false
location: "Philadelphia, US"
pages: "73-81"
publication: "IEEE Conference on Communications and Network Security (CNS)"
---
