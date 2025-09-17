---
title: "All Your Face Are Belong to Us: Breaking Facebook's Social Authentication"
date: 2012-12-03
publishDate: 2012-12-03T00:00:00Z
lastmod: 2020-06-05T08:21:22.421328Z
authors: ["Jason Polakis", "Marco Lancini", "Georgios Kontaxis", "Federico Maggi", "Sotiris Ioannidis", "Angelos Keromytis", "Stefano Zanero"]
publication_types: ["1"]
abstract: "Two-factor authentication is widely used by high-value services to prevent adversaries from compromising accounts using stolen credentials. Facebook has recently released a two-factor authentication mechanism, referred to as Social Authentication, which requires users to identify some of their friends in randomly selected photos. A recent study has provided a formal analysis of social authentication weaknesses against attackers inside the victim's social circles. In this paper, we extend the threat model and study the attack surface of social authentication in practice, and show how any attacker can obtain the information needed to solve the challenges presented by Facebook. We implement a proof-of-concept system that utilizes widely available face recognition software and cloud services, and evaluate it using real public data collected from Facebook. Under the assumptions of Facebook's threat model, our results show that an attacker can obtain access to (sensitive) information for at least 42% of a user's friends that Facebook uses to generate social authentication challenges. By relying solely on publicly accessible information, a casual attacker can solve 22% of the social authentication tests in an automated fashion, and gain a significant advantage for an additional 56% of the tests, as opposed to just guessing. Additionally, we simulate the scenario of a determined attacker placing himself inside the victim's social circle by employing dummy accounts. In this case, the accuracy of our attack greatly increases and reaches 100% when 120 faces per friend are accessible by the attacker, even though it is very accurate with as little as 10 faces."
featured: false
location: "New York, NY, USA"
pages: "399--408"
isbn: "978-1-4503-1312-4"
publication: "Proceedings of the Annual Computer Security Applications Conference (ACSAC)"
---

