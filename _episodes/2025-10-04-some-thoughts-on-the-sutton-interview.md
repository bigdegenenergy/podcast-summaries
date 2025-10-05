---
companies:
- category: unknown
  confidence: medium
  context: rspective than I did during the interview itself. So I wanted to reflect
    on how I understand his role of
  name: So I
  position: 210
- category: unknown
  confidence: medium
  context: d's position. Obviously, he wrote the same essay, The Bitter Lesson. And
    what is this essay about? Well, it's not say
  name: The Bitter Lesson
  position: 513
- category: unknown
  confidence: medium
  context: of true for the RLHF that we do with these LLMs. These RL environments
    are human-furnished playgrounds to t
  name: These RL
  position: 1474
- category: tech
  confidence: high
  context: ome future version of test-time fine-tuning could replicate continual learning
    given that we've already manag
  name: Replicate
  position: 3377
- category: unknown
  confidence: medium
  context: learning, aka do the RL which would lead to AGI. So Ilya Sutskever gave
    a talk a couple of months ago that I thought
  name: So Ilya Sutskever
  position: 3778
- category: unknown
  confidence: medium
  context: nd he compared pre-training data to fossil fuels. And I think this analogy
    actually has remarkable reach.
  name: And I
  position: 3920
- category: unknown
  confidence: medium
  context: ing to collect some well-defined skill or reward. No ML learning regime
    perfectly describes human learnin
  name: No ML
  position: 6158
- category: unknown
  confidence: medium
  context: st short-horizon RL. The episode is a token long. The LLM is making a conjecture
    about the next token based
  name: The LLM
  position: 6563
- category: unknown
  confidence: medium
  context: truth? And I think the answer is, obviously, yes. After RLHFing these pre-trained
    base models, we've gotten them
  name: After RLHFing
  position: 7239
- category: unknown
  confidence: medium
  context: bit, but I'm going to milk it for all its worth. And LLMs being trained
    on outcome-based rewards learn on t
  name: And LLMs
  position: 9095
- category: unknown
  confidence: medium
  context: m to pick up maximum signal from the environment. In Richard's Oak architecture,
    he calls this the transition
  name: In Richard
  position: 9658
- category: tech
  confidence: high
  context: longer than the context limit, then models could meta-learn the same flexibility
    that they already show
  name: Meta
  position: 11027
- category: unknown
  confidence: medium
  context: that agent can selectively do imitation learning. With LLMs, we're going
    the opposite way. We have first made
  name: With LLMs
  position: 11224
- category: ai_theorist
  confidence: high
  context: The person whose position/essay ('The Bitter Lesson') is being critiqued,
    central to the debate on LLM limitations and the need for continual learning.
  name: Richard
  source: llm_enhanced
- category: ai_researcher
  confidence: high
  context: Gave a talk comparing pre-training data to fossil fuels. He is a prominent
    AI researcher and co-founder of OpenAI.
  name: Ilya Sutskever
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned as an example of an AI conditioned on human games (developed
    by DeepMind/Google).
  name: AlphaGo
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned as an AI bootstrapped from scratch, which was better than AlphaGo
    (developed by DeepMind/Google).
  name: AlphaZero
  source: llm_enhanced
date: 2025-10-04 17:45:00 +0000
duration: 12
has_transcript: false
layout: episode
llm_enhanced: true
original_url: https://api.substack.com/feed/podcast/175283310/64bc9b781df688895e748ab6d0d0554b.mp3
processing_date: 2025-10-05 22:47:14 +0000
quotes:
- length: 130
  relevance_score: 4
  text: Now, this is an obvious point in the case of pre-training data, but it's even
    kind of true for the RLHF that we do with these LLMs
  topics: []
- length: 171
  relevance_score: 4
  text: Furthermore, what these LLMs learn from training is not a true world model,
    which would tell you how the environment changes in response to different actions
    that you take
  topics: []
- length: 148
  relevance_score: 4
  text: And this new paradigm will render our current approach with LLMs and their
    special training phase that's super sample and efficient totally obsolete
  topics: []
- length: 121
  relevance_score: 4
  text: So even the imitation learning that humans are doing is not like the supervised
    learning that we do for pre-training LLMs
  topics: []
- length: 139
  relevance_score: 4
  text: By the way, LLMs are clearly developing a deep representation of the world,
    because their training process incentivizes them to develop one
  topics: []
- length: 197
  relevance_score: 3
  text: My main difference with Rich is just that I don't think the concepts he's
    using to distinguish LLMs from true intelligence or animal intelligence are actually
    that mutually exclusive or dichotomous
  topics: []
- length: 199
  relevance_score: 3
  text: '" I also wouldn''t be surprised if some future version of test-time fine-tuning
    could replicate continual learning given that we''ve already managed to accomplish
    this somewhat with in-context learning'
  topics: []
- length: 139
  relevance_score: 3
  text: I use LLMs to teach me about everything from biology to AI to history, and
    they are able to do so with remarkable flexibility and coherence
  topics: []
- length: 290
  relevance_score: 3
  text: The fact that in-context learning emerged spontaneously from the training
    incentive to process long sequences makes me think that if information could just
    flow across windows longer than the context limit, then models could meta-learn
    the same flexibility that they already show in context
  topics: []
- impact_reason: Identifies the fundamental bottleneck of relying solely on human-generated
    data (pre-training and RLHF) for scaling AI capabilities.
  relevance_score: 10
  source: llm_enhanced
  text: Having to learn only from human data, which is an inelastic and hard-to-scale
    resource, is not a scalable way to use compute.
  topic: strategy
- impact_reason: A critical distinction between current LLM capabilities (modeling
    human output) and the requirements for general intelligence (modeling environmental
    dynamics/causality).
  relevance_score: 10
  source: llm_enhanced
  text: Furthermore, what these LLMs learn from training is not a true world model,
    which would tell you how the environment changes in response to different actions
    that you take. Rather, they are building a model of what a human would say next.
  topic: technical
- impact_reason: Directly states the need for architectural breakthroughs beyond current
    transformer models to achieve continual, on-the-job learning, a prerequisite for
    AGI.
  relevance_score: 10
  source: llm_enhanced
  text: LLMs aren't capable of learning on the job, so we'll need some new architecture
    to enable this kind of continual learning.
  topic: predictions
- impact_reason: Quantifies the poor sample efficiency of current RLHF/LLM training
    (one bit per long episode) and contrasts it with biological learning, reinforcing
    the need for better signal extraction mechanisms.
  relevance_score: 10
  source: llm_enhanced
  text: LLMs are learning on the order of one bit per episode, and an episode might
    be tens of thousands of tokens long. Now, obviously, animals and humans are clearly
    extracting more information from interacting with our environment than just the
    reward signal at the end of an episode.
  topic: technical
- impact_reason: A concise summary of the three most critical, fundamental limitations
    of the current LLM paradigm identified through the lens of first-principles critique.
  relevance_score: 10
  source: llm_enhanced
  text: It's the lack of continual learning. It's the abysmal sample efficiency of
    these models. It's their dependence on exhaustible human data.
  topic: technical
- impact_reason: 'A major prediction: current LLMs might achieve AGI first, but the
    *next* generation of systems built by those LLMs will likely adopt the architectural
    principles (continual learning, true world models) advocated by critics like Richard
    Sutton.'
  relevance_score: 10
  source: llm_enhanced
  text: If the LLMs do get to AGI first, which is what I expect to happen, the successor
    systems that they build will almost certainly be based on Richard's vision.
  topic: predictions
- impact_reason: 'A critical strategic concern: current AI progress is bottlenecked
    by the finite amount of high-quality human-generated data available.'
  relevance_score: 10
  source: llm_enhanced
  text: It's their dependence on exhaustible human data.
  topic: limitations/strategy
- impact_reason: This is the core definition of 'The Bitter Lesson,' emphasizing that
    effectiveness must be coupled with scalability in leveraging computational resources,
    a fundamental principle in modern AI development.
  relevance_score: 9
  source: llm_enhanced
  text: The Bitter Lesson says that you want to come up with techniques which most
    effectively and scalably leverage compute.
  topic: strategy
- impact_reason: 'Highlights a massive inefficiency in current LLM deployment: compute
    is spent on inference without learning, contrasting sharply with biological systems.
    This points to a major architectural limitation.'
  relevance_score: 9
  source: llm_enhanced
  text: Most of the compute that's spent on the LLM is used in running it during deployment,
    and yet it's not learning anything during this entire period. It's only learning
    during this special phase that we call training, and so this is obviously not
    an effective use of compute.
  topic: technical
- impact_reason: Provides a powerful analogy justifying the current reliance on massive,
    non-renewable human data sets as a necessary intermediary step toward more advanced
    AI paradigms.
  relevance_score: 9
  source: llm_enhanced
  text: Ilya Sutskever gave a talk a couple of months ago that I thought was super
    interesting. And he compared pre-training data to fossil fuels. And I think this
    analogy actually has remarkable reach. Just because fossil fuels are not a renewable
    resource does not mean that our civilization ended up on a dead-end track by using
    them. In fact, they were absolutely crucial.
  topic: strategy
- impact_reason: Provides concrete evidence (Math Olympiad, coding) that current RLHF
    success relies fundamentally on the prior knowledge embedded during pre-training,
    validating the utility of imitation learning for ground-truth tasks.
  relevance_score: 9
  source: llm_enhanced
  text: Can you solve this unseen math Olympiad question? Can you build this application
    to match the specific feature request? But you couldn't have RLHFed a model to
    accomplish these tasks from scratch, or at least we don't know how to do that
    yet. You needed a reasonable prior over human data in order to kickstart this
    RL process.
  topic: business
- impact_reason: 'Proposes a concrete, architectural idea for shoehorning continual
    learning atop LLMs: using RL to incentivize the model to leverage its own supervised
    learning capabilities (SFT) as a self-teaching tool.'
  relevance_score: 9
  source: llm_enhanced
  text: One could imagine making supervised fine-tuning a tool for the model. So the
    outer loop RL is incentivizing the model to teach itself effectively using supervised
    learning in order to solve problems that don't fit in the context window.
  topic: technical
- impact_reason: Uses the emergence of in-context learning as evidence that architectural
    constraints (like context window limits) are the primary barrier, suggesting that
    relaxing these constraints could unlock meta-learning capabilities akin to continual
    learning.
  relevance_score: 9
  source: llm_enhanced
  text: The fact that in-context learning emerged spontaneously from the training
    incentive to process long sequences makes me think that if information could just
    flow across windows longer than the context limit, then models could meta-learn
    the same flexibility that they already show in context.
  topic: predictions
- impact_reason: Provides a high-level strategic comparison between the natural path
    (Meta-RL -> RL Agent -> Imitation) and the current AI path (Imitation -> RL),
    highlighting the potential mismatch in the current paradigm.
  relevance_score: 9
  source: llm_enhanced
  text: Evolution does meta-RL to make an RL agent, and that agent can selectively
    do imitation learning. With LLMs, we're going the opposite way. We have first
    made this base model that does pure imitation learning, and we're hoping that
    we do enough RL on it to make a coherent agent with goals and self-awareness.
  topic: strategy
- impact_reason: Highlights a fundamental limitation of current LLMs (static knowledge
    cutoff) that prevents them from achieving true intelligence or adaptation.
  relevance_score: 9
  source: llm_enhanced
  text: It's the lack of continual learning.
  topic: limitations
- impact_reason: Points out the massive data requirement (low sample efficiency) for
    training LLMs, contrasting sharply with human learning capabilities.
  relevance_score: 9
  source: llm_enhanced
  text: It's the abysmal sample efficiency of these models.
  topic: technical/limitations
- impact_reason: Offers a nuanced view countering a strict dichotomy, suggesting that
    learning from human data (imitation) is not antithetical to reinforcement learning
    but rather a necessary precursor or complement.
  relevance_score: 8
  source: llm_enhanced
  text: I think imitation learning is continuous with and complementary to RL.
  topic: technical
- impact_reason: Addresses the 'bootstrapping' question head-on, arguing that even
    if a pure, uninitialized AGI is possible, prior imitation learning (like AlphaGo)
    remains highly valuable for reaching superhuman levels quickly.
  relevance_score: 8
  source: llm_enhanced
  text: Will we, or will the first AGI, eventually come up with a general learning
    technique that requires no initialization of knowledge and that just bootstraps
    itself from the very start and outperforms the very best AIs that have been trained
    up to that date? I think the answer to both of these questions is probably yes.
    But does this mean that imitation learning must not play any role whatsoever in
    developing the first AGI or even the first ASI? No.
  topic: predictions
- impact_reason: A counter-argument to the 'no world model' claim, suggesting that
    the complexity of predicting next tokens at scale necessitates the formation of
    rich internal representations of the underlying reality.
  relevance_score: 8
  source: llm_enhanced
  text: By the way, LLMs are clearly developing a deep representation of the world,
    because their training process incentivizes them to develop one.
  topic: technical
- impact_reason: Validates the importance of critiques like Richard Sutton's, even
    if the proposed solution (bootstrapping from scratch) isn't the path taken, because
    the critique correctly identifies current model weaknesses.
  relevance_score: 8
  source: llm_enhanced
  text: Even if Sun's platonic ideal doesn't end up being the path to the first AGI,
    his first-principles critique is identifying some genuine basic gaps these models
    have.
  topic: strategy
- impact_reason: De-emphasizes definitional debates ('world model' vs. 'model of humans')
    in favor of functional utility—the ability to bootstrap learning from ground truth.
  relevance_score: 7
  source: llm_enhanced
  text: Whether you want to call this prior a proper world model or just a model of
    humans, I don't think is that important. And honestly, seems like a semantic debate.
    Because what you really care about is whether this model of humans helps you start
    learning from ground truth, aka become a true world model.
  topic: strategy
source: Unknown Source
summary: '## Podcast Summary: Some Thoughts on the Sutton Interview


  This 11-minute podcast episode provides a detailed reflection and analysis of a
  preceding interview with **Richard Sutton** (implied, referred to as "Sun" and "Rich"),
  focusing on his critique of the current Large Language Model (LLM) paradigm, particularly
  in light of his seminal work, "The Bitter Lesson." The host aims to "steel man"
  Sutton''s position while offering counterpoints based on current LLM capabilities
  and potential future architectures.


  ---


  ### 1. Focus Area

  The discussion centers on the **fundamental limitations of the current LLM training
  paradigm** (pre-training followed by RLHF) when compared to what is required for
  achieving **Artificial General Intelligence (AGI)**, specifically contrasting LLMs''
  reliance on static human data versus the necessity of **continual, on-the-job learning**
  observed in biological agents.


  ### 2. Key Technical Insights

  *   **Inefficiency of Compute Use:** Current LLMs use the vast majority of their
  compute during deployment (inference) where they are not learning. The specialized
  training phase is highly inefficient because it relies on an inelastic resource
  (human data) and only teaches the model *what a human would say next*, not how the
  environment fundamentally changes (a true world model).

  *   **Imitation Learning vs. RL Continuum:** The host argues that imitation learning
  (pre-training) is not categorically separate from Reinforcement Learning (RL); rather,
  pre-trained LLMs serve as an essential, high-quality **prior** that significantly
  kickstarts the RL process, enabling models to achieve ground-truth tasks (like math
  Olympiads) that would be impossible to learn from scratch via RLHF alone.

  *   **The Need for Continual Learning:** The core technical gap identified is the
  lack of **continual learning**—the ability to learn efficiently "on the job." Sutton’s
  vision suggests that future architectures must enable agents to learn on the fly,
  rendering the current, sample-inefficient, discrete training phase obsolete.


  ### 3. Business/Investment Angle

  *   **The Fossil Fuel Analogy for Data:** Pre-training data is likened to **fossil
  fuels**: a crucial, cheap, and convenient intermediary resource that was necessary
  to transition from older systems (water wheels) to the next generation (solar/fusion),
  even if it isn''t renewable or the final state. This implies that current LLMs,
  despite their limitations, are a necessary stepping stone.

  *   **Value of Human Knowledge Accumulation:** The massive accumulation of human
  cultural knowledge (language, science, technology) is analogous to imitation learning
  and is essential for current progress. Investment should recognize that leveraging
  this prior knowledge accelerates capability gains significantly.

  *   **Future Architecture Shift:** The eventual successor systems to current LLMs,
  if built by AGI, will likely adopt architectures aligned with Sutton’s vision, emphasizing
  self-directed learning and high-throughput environmental interaction, suggesting
  a major architectural shift away from static, massive pre-training.


  ### 4. Notable Companies/People

  *   **Richard Sutton (Sun/Rich):** The central figure whose critique frames the
  discussion, emphasizing the need for scalable learning techniques that leverage
  compute effectively and arguing against the current paradigm due to its dependence
  on human data and lack of continual learning.

  *   **Ilya Sutskever:** Mentioned for his analogy comparing pre-training data to
  fossil fuels, supporting the idea that current methods are a crucial, albeit temporary,
  bridge technology.

  *   **AlphaGo/AlphaZero:** Used as examples to show that while bootstrapped systems
  (AlphaZero) can outperform those conditioned on human data (AlphaGo), the human-conditioned
  approach still yields superhuman results and is a viable path.


  ### 5. Future Implications

  The conversation suggests two potential paths:

  1.  **LLM Dominance:** If LLMs reach AGI first, their subsequent systems will likely
  incorporate the continual learning mechanisms advocated by Sutton.

  2.  **Architectural Overhaul:** The fundamental limitations (sample inefficiency,
  lack of world modeling) identified by Sutton are genuine gaps. Future breakthroughs
  will likely involve new architectures that enable high-throughput, continual learning,
  potentially by shoehorning this capability atop current LLMs (e.g., using supervised
  fine-tuning as a tool incentivized by outer-loop RL).


  ### 6. Target Audience

  This episode is most valuable for **AI Researchers, Machine Learning Engineers,
  and Technology Strategists** who are deeply familiar with the mechanics of LLMs
  (pre-training, RLHF, in-context learning) and are engaged in long-term AGI roadmap
  planning.'
tags:
- artificial-intelligence
- ai-infrastructure
- meta
title: Some thoughts on the Sutton interview
topics:
- keywords:
  - ai
  - machine learning
  - deep learning
  - neural networks
  - llm
  - large language model
  mentions: 52
  prominence: 1.0
  topic: artificial intelligence
- keywords:
  - gpu
  - tensor
  - training
  - inference
  - model deployment
  - vector database
  mentions: 11
  prominence: 1.0
  topic: ai infrastructure
---

<!-- Episode automatically generated from analysis data -->
<!-- Processing completed: 2025-10-05 22:47:14 UTC -->
