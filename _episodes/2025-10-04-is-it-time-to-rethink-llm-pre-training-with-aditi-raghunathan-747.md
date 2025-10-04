---
companies:
- category: unknown
  confidence: medium
  context: I'd like to thank our friends at Capital One for sponsoring today's episode.
    Capital One's tec
  name: Capital One
  position: 33
- category: unknown
  confidence: medium
  context: ight, everyone. Welcome to another episode of the Twomol AI podcast. I
    am your host, Sam Charrington. Today,
  name: Twomol AI
  position: 1194
- category: unknown
  confidence: medium
  context: episode of the Twomol AI podcast. I am your host, Sam Charrington. Today,
    I'm joined by Aditi Ragunathan. Aditi is
  name: Sam Charrington
  position: 1229
- category: unknown
  confidence: medium
  context: your host, Sam Charrington. Today, I'm joined by Aditi Ragunathan. Aditi
    is an assistant professor of computer scie
  name: Aditi Ragunathan
  position: 1267
- category: unknown
  confidence: medium
  context: is an assistant professor of computer science at Carnegie Mellon University.
    Before we get going, be sure to take a moment to
  name: Carnegie Mellon University
  position: 1340
- category: unknown
  confidence: medium
  context: 'CML 2025. That paper is called "Roll the Dice and Look Before You Leap:
    Going Beyond the Creative Limits of Next Token P'
  name: Look Before You Leap
  position: 1772
- category: unknown
  confidence: medium
  context: 's called "Roll the Dice and Look Before You Leap: Going Beyond the Creative
    Limits of Next Token Prediction." Bu'
  name: Going Beyond
  position: 1794
- category: unknown
  confidence: medium
  context: 'e Dice and Look Before You Leap: Going Beyond the Creative Limits of Next
    Token Prediction." But more broadly, your'
  name: Creative Limits
  position: 1811
- category: unknown
  confidence: medium
  context: 'ore You Leap: Going Beyond the Creative Limits of Next Token Prediction."
    But more broadly, your lab has been really digg'
  name: Next Token Prediction
  position: 1830
- category: unknown
  confidence: medium
  context: ed to understand to better make use of AI models. And I'm excited to talk
    to those with you. To get us st
  name: And I
  position: 2045
- category: unknown
  confidence: medium
  context: 't got you excited about AI and machine learning.


    So I guess in my undergrad, I was always excited by co'
  name: So I
  position: 2226
- category: unknown
  confidence: medium
  context: d as an example, I was starting with a colleague, Graham Neubig, who kind
    of asked me this question several month
  name: Graham Neubig
  position: 7628
- category: tech
  confidence: high
  context: be a little in some direction by minimizing some gradient steps in a direction,
    that introduces so much noi
  name: Gradient
  position: 13192
- category: unknown
  confidence: medium
  context: 'e where the optimal could be.


    This is the paper "Overtrained Language Models Are Harder to Fine-Tune." We''ll
    link to all the papers that'
  name: Overtrained Language Models Are Harder
  position: 18751
- category: unknown
  confidence: medium
  context: here people had all these defense ideas, but then Karli Ne would break
    all of them. And so it kind of felt l
  name: Karli Ne
  position: 20200
- category: unknown
  confidence: medium
  context: 'might care about?


    So that inspired this work on Memorization Sinks, which is kind of taking the
    same idea or assumpt'
  name: Memorization Sinks
  position: 23114
- category: ai_application
  confidence: high
  context: Deployed a multi-agentic AI called ChatConcierge for simplifying car shopping,
    using self-reflection and layered reasoning.
  name: Capital One
  source: llm_enhanced
- category: ai_research
  confidence: high
  context: Aditi Ragunathan is an assistant professor of computer science there.
  name: Carnegie Mellon University
  source: llm_enhanced
- category: ai_research
  confidence: medium
  context: Where Aditi attended talks on adversarial examples that shaped her thinking
    about model failures.
  name: Stanford
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned as the recent release that scores high on benchmarks but has
    lacking user experience.
  name: GPT-5
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Discussed in the context of being harder to fine-tune compared to Llama
    2, despite strong benchmark performance.
  name: Llama 3
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned in comparison to Llama 3 regarding fine-tuning difficulty.
  name: Llama 2
  source: llm_enhanced
date: 2025-10-04 03:53:06 +0000
duration: 58
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
  confidence: high
  source: llm_enhanced
  text: ''
  type: general
- actionable: false
  confidence: medium
  source: llm_enhanced
  text: ''
  type: general
- actionable: false
  confidence: medium
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
  confidence: high
  source: llm_enhanced
  text: ''
  type: general
- actionable: false
  confidence: medium
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
original_url: https://pscrb.fm/rss/p/traffic.megaphone.fm/MLN5916308473.mp3?updated=1758046985
processing_date: 2025-10-04 03:53:06 +0000
quotes:
- length: 254
  relevance_score: 4
  text: So if you take a small model and keep training on a lot of data, we see that
    eventually the model that has been trained on more data, that you've thrown more
    compute at, is worse as a starting point for fine-tuning than an earlier checkpoint
    that you had
  topics: []
- length: 272
  relevance_score: 4
  text: And we found that the smallest size model, 1B, I believe, that was trained
    on three trillion tokens, is actually worse than the model that was trained on
    fewer tokens after we do this kind of fine-tuning or post-training on very realistic
    benchmarks that people care about
  topics: []
- length: 153
  relevance_score: 4
  text: 'So this was kind of an exciting result that shows that we might need to sort
    of rethink pre-training: how do we get a good starting point for fine-tuning'
  topics: []
- length: 130
  relevance_score: 4
  text: And in the limit, if the fine-tuning matches the pre-training, then we just
    get back the usual things go down as we show more data
  topics: []
- length: 111
  relevance_score: 4
  text: But another important use case of all of these post-training or fine-tuning
    methodologies is safety in some way
  topics: []
- length: 114
  relevance_score: 3
  text: What we found, what the community has found, is in general, the more data
    you train on, all of these numbers go up
  topics: []
- length: 62
  relevance_score: 3
  text: Yes, for the quantization result, that's exactly what we found
  topics: []
- length: 169
  relevance_score: 3
  text: I think if you are using a really—I guess what we found is the one billion
    model size, which again, you might want to use for efficiency reasons—if it's
    trained beyond 2
  topics: []
- length: 161
  relevance_score: 3
  text: And then people realize that you can't actually do too well because then you
    have to change everything a lot, and that destroys a lot of information in the
    model
  topics: []
- length: 121
  relevance_score: 3
  text: There's nothing in the training objective—you're just passing gradients to
    all the parameters—so there's nothing about it
  topics: []
- impact_reason: Highlights a real-world, deployed example of multi-agentic AI solving
    a complex, multi-step business task (car shopping), moving beyond theoretical
    discussion.
  relevance_score: 9
  source: llm_enhanced
  text: Capital One's tech team isn't just talking about multi-agentic AI, they already
    deployed one. It's called ChatConcierge and it's simplifying car shopping.
  topic: business/predictions
- impact_reason: Details the specific advanced capabilities (self-reflection, layered
    reasoning, API integration) that enable the multi-agent system to handle complex
    workflows, relevant for advanced AI deployment.
  relevance_score: 9
  source: llm_enhanced
  text: Using self-reflection and layered reasoning with live API checks, it doesn't
    just help buyers find a car they love, it helps schedule a test drive, get pre-approved
    for financing, and estimate trade-in value.
  topic: technical/business
- impact_reason: 'This is a core critique of current LLM development: the over-reliance
    on benchmarks leading to models that fail in real-world, slightly shifted deployment
    scenarios.'
  relevance_score: 10
  source: llm_enhanced
  text: We measure performance on a benchmark and if that's all we care about, it
    seems like we can do really well because if you collect data that looks like the
    data you want to do well on, you can just throw a lot of compute at it, but does
    that actually solve the task if we just test it in a slightly different way that
    is also meaningful from a deployment perspective?
  topic: strategy/safety
- impact_reason: A concise statement summarizing the current imbalance in AI progress—capability
    is soaring while reliability remains stagnant.
  relevance_score: 9
  source: llm_enhanced
  text: And maybe it's also sobering that it's not that we have actually pushed the
    reliability as we have pushed the capability of these models.
  topic: strategy
- impact_reason: Directly links the lack of fundamental understanding of LLMs to brittle
    safety guardrails and potential societal risks (toxicity, manipulation).
  relevance_score: 10
  source: llm_enhanced
  text: And I think the part that's also concerning is when this lack of understanding
    becomes a real issue, when people think about getting models to be safe in some
    way... And a lot of our guardrails around these things are very brittle, and we
    currently don't have a way to do better because we don't really understand these
    systems.
  topic: safety
- impact_reason: Confirms a widely felt industry sentiment regarding the discrepancy
    between advertised intelligence (benchmarks) and practical utility, using a current
    model release as evidence.
  relevance_score: 9
  source: llm_enhanced
  text: This growing gap between benchmark performance and the experience of using
    these models, I think, is kind of a growing concern and one that we're hearing
    a lot of at this particular moment of time, I think because of the recent release
    of GPT-5...
  topic: strategy
- impact_reason: 'A highly impactful, counter-intuitive finding: more pre-training
    compute can actively degrade a model''s utility as a starting point for downstream
    fine-tuning.'
  relevance_score: 10
  source: llm_enhanced
  text: So if you take a small model and keep training on a lot of data, we see that
    eventually the model that has been trained on more data, that you've thrown more
    compute at, is worse as a starting point for fine-tuning than an earlier checkpoint
    that you had.
  topic: technical/business
- impact_reason: Emphasizes the significance of the previous finding, showing that
    the negative effect of over-training is not saturation but active degradation,
    even with good data.
  relevance_score: 9
  source: llm_enhanced
  text: This was actually a really striking result because it's one of the first realistic
    cases where more compute in a very non-contrived setting, like on high-quality
    data, more compute is actually making your model worse, not just that it saturates,
    but it's actively worse.
  topic: technical
- impact_reason: 'A critical strategic warning for AI labs: optimizing the pre-training
    phase alone is insufficient if it compromises adaptability in the crucial fine-tuning
    phase.'
  relevance_score: 9
  source: llm_enhanced
  text: And our current push towards just doing what we're doing now by improving
    this pre-training or the first step of this process, or really optimizing that,
    doesn't mean it's going to be good after doing your fine-tuning or post-training.
  topic: strategy
- impact_reason: Provides a theoretical explanation (brittleness due to learning overly
    complex patterns) for why over-trained models fail during fine-tuning or adversarial
    attacks (forgetting/catastrophic interference).
  relevance_score: 8
  source: llm_enhanced
  text: The model is forced to learn more and more complex things, which is good because
    it's fitting the data, but then that also means that the model is brittle in some
    way, that if you try to push the model to be a little in some direction by minimizing
    some gradient steps in a direction, that introduces so much noise or kind of breaks
    the model and causes a lot of forgetting.
  topic: technical/safety
- impact_reason: This describes 'catastrophic overtraining' as a U-shaped phenomenon
    where excessive fine-tuning data eventually degrades performance, which is a critical
    practical limit for practitioners.
  relevance_score: 9
  source: llm_enhanced
  text: And then at some point, the model gets so brittle that whatever it learns
    from the more data kind of just is overcome by its brittleness, and so we start
    seeing this jump. So there is a point where more data starts hurting you, so it's
    like a U-shaped kind of situation.
  topic: technical
- impact_reason: Provides a concrete, actionable guideline regarding the pre-training
    data volume limit (2.5-3T tokens) for smaller (1B) models before they become too
    brittle for effective fine-tuning.
  relevance_score: 9
  source: llm_enhanced
  text: if you are using a really—I guess what we found is the one billion model size,
    which again, you might want to use for efficiency reasons—if it's trained beyond
    2.5 trillion tokens, or maybe even 3 trillion tokens, because we didn't have too
    much granularity in the public checkpoints, I would say that maybe that's a point
    where you don't want to use that model unless you're sure that you don't want
    to change the model too much.
  topic: business/strategy
- impact_reason: Directly links unlearning research to critical safety and alignment
    use cases, framing unlearning as a necessary component of post-training safety
    procedures.
  relevance_score: 8
  source: llm_enhanced
  text: The alignment work is actually trying to teach the model post-hoc what is
    good and what is bad. And similarly, we might try to unlearn harmful knowledge
    or unlearn private information, and so on.
  topic: safety
- impact_reason: Challenges the common assumption in unlearning research that harmful
    or private information is neatly localized in specific neurons, explaining why
    many current unlearning methods fail.
  relevance_score: 10
  source: llm_enhanced
  text: What we show is that that actually is not true—that there's no reason in how
    we have framed these models that encourages or that should allow this information
    to be disentangled in this nice way.
  topic: technical
- impact_reason: Introduces the core concept of 'Memorization Sinks'—proactively designing
    training to enforce knowledge localization, contrasting it with the passive failure
    of standard training to achieve this.
  relevance_score: 10
  source: llm_enhanced
  text: So instead of waiting for it to happen by magic, we are like, let's try to
    actually enforce that by design. And we find in our paper, both in experiments
    and analysis, that normal training does not actually lead to this assumption to
    be true...
  topic: technical
- impact_reason: 'Explains the mechanism of Memorization Sinks: isolating unique document
    information into dedicated, non-updated neurons for easy removal/isolation.'
  relevance_score: 9
  source: llm_enhanced
  text: The stuff that's very specific to a particular document is in these memorization
    neurons, and since those are not updated on any other documents, that information
    is sort of preserved, disentangled, kept aside.
  topic: technical
- impact_reason: 'Provides a clear, practical outcome of the Memorization Sinks architecture:
    selective removal of specific knowledge (e.g., private data) by dropping out specific
    neurons at inference time.'
  relevance_score: 9
  source: llm_enhanced
  text: And the stuff that's very specific to a particular document is in these memorization
    neurons, and since those are not updated on any other documents, that information
    is sort of preserved, disentangled, kept aside. And at test time, you can just
    drop out these memorization neurons, and then you're good to go.
  topic: technical/safety
- impact_reason: 'Highlights the fundamental inductive bias problem: standard gradient
    descent does not inherently prioritize knowledge disentanglement necessary for
    effective unlearning.'
  relevance_score: 8
  source: llm_enhanced
  text: There's nothing in the training objective—you're just passing gradients to
    all the parameters—so there's nothing about it. There is some separation that
    seems to emerge, but it's not perfect because it doesn't have to be; it's not
    trained to be.
  topic: technical
- impact_reason: 'A crucial constraint for the Memorization Sinks approach: effective
    targeted unlearning requires pre-defining the categories or abstractions (e.g.,
    topic, document) whose information needs isolation.'
  relevance_score: 7
  source: llm_enhanced
  text: We need to know that abstraction that we might want to remove later.
  topic: strategy
- impact_reason: Addresses the scaling concern of Memorization Sinks by suggesting
    that orthogonality in high-dimensional subspaces can substitute for a massive
    increase in the number of dedicated neurons, offering a practical optimization.
  relevance_score: 7
  source: llm_enhanced
  text: We do need to—so the models have to be a little bit bigger in this way because
    we do need more neurons. But one other kind of nice trick is we don't need them
    to have completely separate neurons; we just need to make sure that the neurons
    are somewhat orthogonal.
  topic: technical
source: The TWIML AI Podcast (formerly This Week in Machine Learning & Artificial
  Intelligence)
summary:
- key_takeaways:
  - Benchmark performance often decouples from real-world utility, as models optimized
    for benchmarks can fail spectacularly under slight distribution shifts.
  - 'Catastrophic Overtraining: Models trained on excessive data (high token-to-parameter
    ratio) can become worse starting points for fine-tuning than earlier checkpoints,
    even when trained on high-quality data.'
  - This overtraining effect is observed in both fine-tuning for specific tasks and
    in efficiency-driven quantization, where increased pre-training data makes the
    resulting model more brittle.
  - The brittleness caused by overtraining leads to catastrophic forgetting or poor
    adaptation when the model is pushed in new directions (e.g., via fine-tuning or
    quantization noise).
  - Current unlearning and safety alignment methods often fail because the assumption
    that harmful or private knowledge is neatly localized in specific neurons is generally
    false in standard LLMs.
  - Memorization Sinks propose an architectural modification during pre-training to
    explicitly encourage the disentanglement of document-specific knowledge into dedicated
    'sink' neurons, enabling targeted removal (unlearning) without destroying shared
    knowledge.
  overview: This episode features Aditi Raghunathan discussing the critical limitations
    of current LLM pre-training paradigms, particularly the over-reliance on benchmark
    performance which masks failures in real-world deployment and fine-tuning. Her
    research highlights that models optimized purely for massive pre-training data
    can become brittle, leading to 'catastrophic overtraining' where increased compute
    actively degrades adaptability for downstream tasks like safety alignment or personalization.
    The discussion explores novel approaches, such as 'Memorization Sinks,' designed
    to enforce disentanglement during training to enable reliable unlearning and better
    model customization.
  themes:
  - Limitations of Current LLM Pre-training and Scaling Laws
  - Benchmark Inadequacy vs. Deployment Robustness
  - Catastrophic Overtraining and Model Brittleness
  - Adaptability and Fine-Tuning Challenges
  - Unlearning, Safety Alignment, and Knowledge Isolation
  - Architectural Interventions for Better Model Control (Memorization Sinks)
tags:
- artificial-intelligence
- ai-infrastructure
- generative-ai
title: 'Is It Time to Rethink LLM Pre-Training? with Aditi Raghunathan - #747'
topics:
- keywords:
  - ai
  - machine learning
  - deep learning
  - neural networks
  - llm
  - large language model
  mentions: 71
  prominence: 1.0
  topic: artificial intelligence
- keywords:
  - gpu
  - tensor
  - training
  - inference
  - model deployment
  - vector database
  mentions: 21
  prominence: 1.0
  topic: ai infrastructure
- keywords:
  - generative ai
  - genai
  - chatgpt
  - gpt
  - claude
  - text generation
  - image generation
  mentions: 1
  prominence: 0.1
  topic: generative ai
---

<!-- Episode automatically generated from analysis data -->
<!-- Processing completed: 2025-10-04 03:53:06 UTC -->
