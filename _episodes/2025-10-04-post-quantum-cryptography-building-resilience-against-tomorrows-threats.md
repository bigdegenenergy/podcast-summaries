---
companies:
- category: unknown
  confidence: medium
  context: tual server to support post-quantum cryptography. Currently I have a web
    server sitting behind my Big IP. This
  name: Currently I
  position: 96
- category: unknown
  confidence: medium
  context: . Currently I have a web server sitting behind my Big IP. This is my Big
    IP. This is the virtual server I
  name: Big IP
  position: 144
- category: tech
  confidence: high
  context: Mentioned as the device sitting in front of the web server, used for configuration.
  name: Big IP
  source: llm_enhanced
- category: tech
  confidence: high
  context: Mentioned as the provider of the standard certificate currently in use.
  name: Let's Encrypt
  source: llm_enhanced
date: 2025-10-04 01:13:34 +0000
duration: 1
has_transcript: false
insights:
- actionable: false
  confidence: high
  source: llm_enhanced
  text: ''
  type: general
- actionable: false
  confidence: high
  source: llm_enhanced
  text: ''
  type: general
- actionable: false
  confidence: medium
  source: llm_enhanced
  text: ''
  type: general
layout: episode
llm_enhanced: true
original_url: https://www.youtube.com/watch?v=fubxB0uxMHM
processing_date: 2025-10-04 01:13:34 +0000
quotes:
- impact_reason: This highlights the critical distinction between existing encryption
    and the new post-quantum cryptography (PQC) handshake, which is the core focus
    of the transition.
  relevance_score: 9
  source: llm_enhanced
  text: We're still using the same encryption for the traffic. But the handshake is
    now using the post-quantum encryption.
  topic: technology
- impact_reason: This succinctly identifies the primary technical change required
    for PQC adoption—modifying the handshake protocol.
  relevance_score: 9
  source: llm_enhanced
  text: The difference when we move to post-quantum will be the handshake algorithm
    is going to be different.
  topic: technology
- impact_reason: This outlines the necessary prerequisite steps (enabling TLS 1.3
    and defining specific cipher rules/groups) for implementing PQC in a modern infrastructure
    setup.
  relevance_score: 8
  source: llm_enhanced
  text: First of all we need to enable TLS1.3. In order to enable TLS1.3 we need to
    define a cipher rule and a cipher group.
  topic: technology
- impact_reason: A direct instruction on the core configuration change needed to achieve
    PQC readiness.
  relevance_score: 8
  source: llm_enhanced
  text: We need to add the post-quantum algorithms.
  topic: technology
- impact_reason: This speaks to efficient configuration management in enterprise environments,
    suggesting leveraging existing profiles rather than starting from scratch when
    adopting new standards like PQC.
  relevance_score: 7
  source: llm_enhanced
  text: We can use inherited capabilities from there. And then we're going to add
    our own settings for this particular configuration.
  topic: business
- impact_reason: This points out a common configuration hurdle when upgrading security
    protocols—the need to explicitly manage and sometimes disable older settings to
    enable newer ones (TLS 1.3).
  relevance_score: 7
  source: llm_enhanced
  text: You'll see that there's no tls1.3 as an option here. We need to disable that.
  topic: technology
- impact_reason: Emphasizes the creation of a distinct, specialized configuration
    object required for the new security standard.
  relevance_score: 6
  source: llm_enhanced
  text: We now have a new SSL client profile.
  topic: technology
- impact_reason: Provides context on the infrastructure setup (using a load balancer/proxy
    like F5 Big-IP), which is common in enterprise tech deployments facing security
    upgrades.
  relevance_score: 6
  source: llm_enhanced
  text: Currently I have a web server sitting behind my Big IP.
  topic: technology
- impact_reason: Indicates that the foundational elements (like standard certificates)
    do not necessarily need replacement when adopting PQC handshakes, focusing the
    effort on the protocol layer.
  relevance_score: 6
  source: llm_enhanced
  text: This certificate is just a standard Let's Encrypt certificate.
  topic: technology
- impact_reason: Shows that the transition to PQC is primarily a protocol/handshake
    upgrade rather than a complete overhaul of the PKI infrastructure, which is a
    positive business implication.
  relevance_score: 5
  source: llm_enhanced
  text: We also can see that we have a certificate. The certificate is valid and this
    certificate is just a standard Let's Encrypt certificate.
  topic: business
source: AI/ML Channel UCtVHX3fmQVjVgj_cGRIxRSg
summary:
- key_takeaways:
  - The transition to Post-Quantum Cryptography (PQC) primarily involves updating
    the TLS handshake protocol, specifically moving from TLS 1.2 to TLS 1.3.
  - Implementing PQC requires defining a new cipher rule that explicitly incorporates
    the necessary post-quantum algorithms.
  - A new cipher group must be created, referencing the PQC-enabled cipher rule, to
    bundle these new cryptographic suites.
  - A new SSL client profile must be configured, based on the existing profile, to
    enable TLS 1.3 and assign the newly created PQC cipher group.
  - The virtual server configuration must then be updated to utilize this new PQC-enabled
    SSL client profile.
  - Successful implementation is verified by observing that the connection now utilizes
    TLS 1.3, incorporating the quantum-safe handshake, even if the bulk data encryption
    remains unchanged.
  overview: This session provides a practical, step-by-step guide on migrating a standard
    TLS 1.2 web server configuration to one that supports post-quantum cryptography
    (PQC) using a Big IP device. The core process involves enabling TLS 1.3 and defining
    new cipher rules and groups that incorporate PQC algorithms to secure the handshake
    against future quantum threats. Although the underlying traffic encryption remains
    the same initially, the critical handshake mechanism is successfully upgraded
    to a quantum-resistant standard.
  themes:
  - Post-Quantum Cryptography (PQC) Implementation
  - TLS Protocol Migration (TLS 1.2 to TLS 1.3)
  - Network Security Configuration (Big IP)
  - Cipher Suite Management
  - Building Cryptographic Resilience
tags: []
title: 'Post-Quantum Cryptography: Building Resilience Against Tomorrow’s Threats'
---

<!-- Episode automatically generated from analysis data -->
<!-- Processing completed: 2025-10-04 01:13:34 UTC -->
