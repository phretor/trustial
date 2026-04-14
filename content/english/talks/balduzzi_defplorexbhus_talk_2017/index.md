---
title: "DefPloreX: A Machine Learning Toolkit for Large-scale e-Crime Forensics"
date: 2017-07-27
publishDate: 2017-07-27T00:00:00Z
lastmod: 2020-06-05T09:07:15.215630Z
authors:
  [
    "Marco Balduzzi",
    "Federico Maggi",
    "Vincenzo Ciancaglini",
    "Ryan Flores",
    "Lion Gu",
  ]
publication_types: ["3"]
abstract: 'The security industry as a whole---including operation centers, providers and telcos---loves collecting data. Researchers are not different! A sort of common feeling is that the more data someone collects, the more self-confident he becomes about, say, a threat or another phenomenon. However, large volumes of data imply more processing resources needed, especially in extracting meaningful and useful information if the data is highly unstructured. As a result, manual data analysis is often the only choice, with security professionals like pen-testers, reversers and analysts processing data through tedious repetitive operations.  Given this situation, and our research lab suffering from similar problems, we have spent the first half of 2017 implementing a flexible toolkit based on open-source libraries for efficiently analyzing millions of deface pages and web incidents. Our tool, DefPloreX, uses a combination of machine-learning and visualization techniques to practically turn original unstructured data into meaningful high-level descriptions. Real-time information on incidents, breaches, attacks and vulnerabilities, for example, are efficiently processed and condensed into objects that are easily browsable -- making them suitable for efficient large-scale eCrime forensics and investigations.  DefPloreX ingests plain CSV inputs about web incidents to analyze, explores their resources with headless browsers, extracts features from deface pages, and uploads the resulting data to an Elastic index. Distributed headless browsers are coordinated via Celery. Using Python Panda, NumPy and PyTables, DefPloreX provides offline "views" of the data, allowing easy pivoting and exploration. Our toolkit automatically groups similar deface pages in clusters and organizes web incidents in campaigns. Requiring only one pass, clustering is intrinsically parallel and not memory bound. DefPloreX offers text- and web-based UIs, which can be queried using a simple language for investigations and forensics.'
featured: false
location: "Las Vegas, US"
howpublished: "Peer-reviewed Demo"
event: "Black Hat Arsenal USA"
event_url: "https://www.blackhat.com/us-17/arsenal.html#defplorex-a-machine-learning-toolkit-for-large-scale-ecrime-forensics"
url_video: https://www.youtube.com/watch?v=DILbSXYpiMU
---
