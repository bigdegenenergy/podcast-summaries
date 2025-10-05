---
companies:
- category: unknown
  confidence: medium
  context: If you're familiar with the Retrieval Space, M-Tub is a pretty popular
    benchmark for embeddin
  name: Retrieval Space
  position: 28
- category: unknown
  confidence: medium
  context: ight, everyone. Welcome to another episode of the Twinmal AI podcast. I
    am your host, Sam Charrington. Today,
  name: Twinmal AI
  position: 519
- category: unknown
  confidence: medium
  context: pisode of the Twinmal AI podcast. I am your host, Sam Charrington. Today,
    I'm joined by Kelly Hong. Kelly is a rese
  name: Sam Charrington
  position: 555
- category: unknown
  confidence: medium
  context: your host, Sam Charrington. Today, I'm joined by Kelly Hong. Kelly is a
    researcher at Chroma. Kelly, welcome
  name: Kelly Hong
  position: 593
- category: tech
  confidence: high
  context: '''m joined by Kelly Hong. Kelly is a researcher at Chroma. Kelly, welcome
    to the podcast. Thank you so much'
  name: Chroma
  position: 630
- category: unknown
  confidence: medium
  context: ing about a project you recently published called Generative Benchmarking.
    That one really resonated with me for a few reas
  name: Generative Benchmarking
  position: 835
- category: unknown
  confidence: medium
  context: ojects around it, going deeper into the research. And I would come across
    Chroma a lot because I would us
  name: And I
  position: 1637
- category: unknown
  confidence: medium
  context: 'rom school and working here basically full time.


    And Chroma does come up, particularly in the context of vect'
  name: And Chroma
  position: 2077
- category: unknown
  confidence: medium
  context: larly in the context of vector databases and RAG. And RAG continues to
    be a topic of interest for folks lis
  name: And RAG
  position: 2159
- category: unknown
  confidence: medium
  context: make a decision on which embedding model to use. But I think with these
    methods of generative benchmarki
  name: But I
  position: 6330
- category: tech
  confidence: high
  context: case. For example, we were working with data from Weights & Biases for
    technical support bots. So, it's basically li
  name: Weights & Biases
  position: 10299
- category: unknown
  confidence: medium
  context: that and the way that we are generating queries. Because I think these
    two parts combined kind of make up wh
  name: Because I
  position: 11797
- category: tech
  confidence: high
  context: see a list of actual queries from users; you can replicate them. But I
    think maybe one distinction there wou
  name: Replicate
  position: 17279
- category: unknown
  confidence: medium
  context: working with production data was that we saw that Jina AI's model performed
    slightly worse than OpenAI's te
  name: Jina AI
  position: 19991
- category: tech
  confidence: high
  context: hat Jina AI's model performed slightly worse than OpenAI's text-embedding-3-large
    model, which actually co
  name: Openai
  position: 20037
- category: unknown
  confidence: medium
  context: 'il? How does that process work?


    Yeah, of course. For EvalGen, you basically need a set of criteria. So, in our'
  name: For EvalGen
  position: 25018
- category: tech
  confidence: high
  context: 'xact same query that would appear in the original Hugging Face dataset.


    The example you give for that is from t'
  name: Hugging Face
  position: 40714
- category: ai_application
  confidence: high
  context: The company where Kelly Hong is a researcher, working on vector databases
    and research around retrieval (RAG).
  name: Chroma
  source: llm_enhanced
- category: ai_research
  confidence: high
  context: A popular benchmark for embedding models in the Retrieval Space, frequently
    cited when releasing new models.
  name: M-Tub
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: The source of the data (technical support bot logs and documentation) used
    for the generative benchmarking case study.
  name: Weights & Biases
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned for their embedding model, 'text-embedding-3-large', which was
    compared against Jina AI's model.
  name: OpenAI
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: Mentioned for their embedding model which performed slightly worse than
    OpenAI's on real-world data, despite better public benchmark scores. Also mentioned
    for their evaluation tool, AirBench.
  name: Jina AI
  source: llm_enhanced
- category: ai_infrastructure
  confidence: high
  context: Mentioned for their '3 large model' embedding model, which performed best
    in the speaker's evaluation on technical documentation.
  name: Voyage
  source: llm_enhanced
- category: ai_infrastructure
  confidence: high
  context: An existing tool/framework by Jina AI for creating custom evaluation sets,
    similar in motivation to the speaker's work.
  name: AirBench
  source: llm_enhanced
- category: ai_infrastructure
  confidence: medium
  context: Mentioned in reference to the 'Hugging Face dataset' (likely referring
    to a dataset hosted or curated by them, such as the Wikipedia dataset example).
  name: Hugging Face
  source: llm_enhanced
- category: ai_application
  confidence: high
  context: The speaker mainly used 'Claude' when testing different LLMs for query
    generation, indicating it is an accessible LLM platform.
  name: Claude
  source: llm_enhanced
date: 2025-04-23 22:09:00 +0000
duration: 54
has_transcript: false
layout: episode
llm_enhanced: true
original_url: https://pscrb.fm/rss/p/traffic.megaphone.fm/MLN1226891394.mp3?updated=1745421739
processing_date: 2025-10-05 22:35:13 +0000
quotes:
- length: 106
  relevance_score: 6
  text: A lot of people just use it for RAG, where you retrieve relevant documents
    and then you have an LLM output
  topics: []
- length: 80
  relevance_score: 5
  text: And Chroma does come up, particularly in the context of vector databases and
    RAG
  topics: []
- length: 174
  relevance_score: 4
  text: We noticed there were a few documents in there that were talking about funding
    news or just content that wasn't relevant to any kind of developer using this
    technical chatbot
  topics:
  - funding
- length: 173
  relevance_score: 4
  text: I was thinking about this process and its applicability to my favorite use
    case, which is I have a bunch of podcast transcripts, and I want to create a RAG
    chatbot for those
  topics: []
- length: 234
  relevance_score: 4
  text: 'This is how evaluation typically works for evaluating an embedding model:
    you have a query-document pair, you embed your document corpus, you embed your
    queries, and then you see whether you retrieve that document in the top K results'
  topics:
  - valuation
- length: 66
  relevance_score: 4
  text: In the report, you talked about LLM as judge and alignment in this
  topics: []
- length: 178
  relevance_score: 4
  text: For example, when we were first using an LLM judge to filter documents, we
    compared that to ground truth labels, and I think it only got around 46% alignment,
    which is pretty bad
  topics: []
- length: 113
  relevance_score: 4
  text: So, I think a lot of people just blindly use an LLM judge without any alignment,
    just assuming that it is aligned
  topics: []
- length: 140
  relevance_score: 4
  text: But I think we're too far from that right now, and we do need some level of
    human alignment to actually confidently put the LLM judge to use
  topics: []
- length: 92
  relevance_score: 4
  text: A lot of people just tend to focus only on the LLM output, just like, "Is
    it performing well
  topics: []
- length: 92
  relevance_score: 4
  text: If you can make that better, maybe your LLM output performance will increase
    a lot more, too
  topics: []
- length: 191
  relevance_score: 4
  text: So, if you have RAG, look at what documents are actually being retrieved and
    try to figure out what's going on from there, rather than just looking at the
    output and seeing what the vibes are
  topics: []
- length: 143
  relevance_score: 4
  text: One thing that comes up a lot in RAG systems is that if you have a lot of
    distractors in your LLM prompt, it leads to very degraded performance
  topics: []
- length: 118
  relevance_score: 4
  text: 'Because ultimately, this is what matters to a developer building a RAG application:
    which embedding model should I use'
  topics: []
- length: 107
  relevance_score: 4
  text: And we also have some human alignment in the whole LLM judge process where
    you're filtering document chunks
  topics: []
- length: 131
  relevance_score: 4
  text: I don't think there has been, or at least from what I've seen, there hasn't
    been a lot of work in LLM alignment on multiple parties
  topics: []
- length: 73
  relevance_score: 4
  text: So, I think multi-party LLM alignment will be interesting to see for sure
  topics: []
- length: 297
  relevance_score: 4
  text: Yeah, I guess thinking about it more, you could argue that maybe the case
    is that a lot of the core LLM alignment work is fundamentally multi-party in a
    sense that if you think about instruction following, you want to follow the developer's
    instructions, but you also want to be useful to the user
  topics: []
- length: 222
  relevance_score: 3
  text: And I would come across Chroma a lot because I would use it in my projects,
    but I also saw that they did a lot of good research around chunking strategies,
    embedding adopters, just ways to make your retrieval system better
  topics: []
- length: 93
  relevance_score: 3
  text: So, it's basically like this chatbot where you can talk to the Weights & Biases
    documentation
  topics: []
- length: 156
  relevance_score: 3
  text: For example, a lot of users using a technical chatbot like the one that Weights
    & Biases has, they probably wouldn't be asking queries in complete sentences
  topics: []
- length: 244
  relevance_score: 3
  text: And I think one of the key things we saw when working with production data
    was that we saw that Jina AI's model performed slightly worse than OpenAI's text-embedding-3-large
    model, which actually conflicted with the M-Tub score in their release
  topics: []
- length: 93
  relevance_score: 3
  text: '" and then they might change prompting, but maybe the problem is just in
    the retrieval itself'
  topics: []
- length: 142
  relevance_score: 3
  text: So, if you fed that document/chunk into the LLM, it would generate the exact
    same query that would appear in the original Hugging Face dataset
  topics: []
- impact_reason: Raises the critical issue of data leakage and memorization in public
    benchmarks, invalidating performance claims.
  relevance_score: 10
  source: llm_enhanced
  text: And a lot of this data has probably been seen by embedding models before,
    so you don't really know if you're testing for true retrieval or if they're just
    doing this based off of memorization.
  topic: safety/technical
- impact_reason: Justifies the necessity of the document filtering step—ensuring the
    evaluation set reflects the actual domain of the application.
  relevance_score: 10
  source: llm_enhanced
  text: We first want to filter out those documents because they're not reflective
    of what users will actually ask about. And the main goal with generative benchmarking
    is to create a benchmark that's representative of your true use case.
  topic: technical/strategy
- impact_reason: Provides empirical evidence that performance on public benchmarks
    (like M-Tub) does not guarantee superior performance on specific, real-world RAG
    use cases, highlighting model divergence.
  relevance_score: 10
  source: llm_enhanced
  text: I think we've seen some pretty distinct differences between embedding models.
    And I think one of the key things we saw when working with production data was
    that we saw that Jina AI's model performed slightly worse than OpenAI's text-embedding-3-large
    model, which actually conflicted with the M-Tub score in their release.
  topic: technical/predictions
- impact_reason: A concise summary of the previous point, serving as a major cautionary
    note for practitioners choosing embedding models based only on leaderboards.
  relevance_score: 10
  source: llm_enhanced
  text: So, in spite of performing better on the public benchmarks, it performs worse
    on real-world data.
  topic: technical/strategy
- impact_reason: Provides a stark warning against 'blindly' using LLM judges, quantifying
    the initial misalignment (46%) with human judgment, underscoring the necessity
    of alignment processes.
  relevance_score: 10
  source: llm_enhanced
  text: Because if we just blindly use an LLM judge, it's not guaranteed to judge
    in the way that humans do. For example, when we were first using an LLM judge
    to filter documents, we compared that to ground truth labels, and I think it only
    got around 46% alignment, which is pretty bad.
  topic: safety/technical
- impact_reason: Provides a concrete metric demonstrating the massive impact of prompt
    tuning on LLM judge performance (46% to 70s), underscoring the volatility and
    importance of prompt engineering in evaluation.
  relevance_score: 10
  source: llm_enhanced
  text: it would range quite a bit. So, as we said in the report, it improved from
    46% to around the 70s. So, that's a pretty big difference just based on how you're
    prompting the LLM judge. So, yeah, we noticed that LLMs are very sensitive to
    prompting.
  topic: technical
- impact_reason: 'Draws a critical distinction between generative benchmarking approaches:
    EvalGen prioritizes representativeness of production data over mere query diversity,
    a key strategic difference in RAG evaluation.'
  relevance_score: 10
  source: llm_enhanced
  text: I think for RAGs and AirBench, they focused a lot on generating a diverse
    set of queries. They don't really put much focus on how representative it is of
    your actual production data. So, I think that was the main difference we had.
  topic: strategy
- impact_reason: 'Highlights a significant challenge in enterprise AI: performance
    degradation in highly specialized domains where chunk differentiation is difficult,
    signaling a key area for future research.'
  relevance_score: 10
  source: llm_enhanced
  text: We noticed that retrieval performance drops a lot when you're working with
    these very domain-specific datasets... it's very hard to differentiate between
    different chunks. So, I think one area that could be interesting to explore is
    how can we improve performance in these very domain-specific use cases...
  topic: technical
- impact_reason: 'Offers crucial strategic advice for RAG builders: do not over-focus
    on the LLM output; systematically debug the retrieval component first, as poor
    retrieval guarantees poor final output.'
  relevance_score: 10
  source: llm_enhanced
  text: I think one of the important things is understanding how important retrieval
    is in the context of your entire AI system. A lot of people just use it for RAG,
    where you retrieve relevant documents and then you have an LLM output. A lot of
    people just tend to focus only on the LLM output... but maybe the problem is just
    in the retrieval itself.
  topic: strategy
- impact_reason: 'Identifies a major gap between academic/benchmark evaluation and
    real-world deployment: real user queries are ambiguous, leading to lower relevance
    scores than expected from polished datasets.'
  relevance_score: 10
  source: llm_enhanced
  text: A lot of real user queries are very ambiguous. And a lot of the polished datasets
    that you see, the query-document pairs are highly relevant, so it's very obvious
    that a query matches the documents. Whereas in the real world, maybe a query is
    only relevant to the first sentence of a chunk.
  topic: strategy/predictions
- impact_reason: Warns against misleading benchmark results derived from 'naive' query
    generation, emphasizing that high scores on synthetic data do not translate to
    real-world performance robustness.
  relevance_score: 10
  source: llm_enhanced
  text: We tested this out with a naive query generation method as well, where we
    wouldn't give any example queries, we wouldn't give it any context; we would literally
    just feed in the chunk and tell the LLM to generate a query. And in those cases,
    oftentimes it would generate pretty relevant queries, more relevant queries than
    the real production queries. And we noticed a performance increase by a lot, which
    if you're just looking at the numbers, it looks good, but it's not really reflective
    of what you'll actually see in production.
  topic: safety/strategy
- impact_reason: Quantifies the importance of human oversight in the judging component
    of evaluation (46% alignment without it), showing that unguided LLM judges are
    unreliable proxies for human judgment.
  relevance_score: 10
  source: llm_enhanced
  text: And we also have some human alignment in the whole LLM judge process where
    you're filtering document chunks. So, if we didn't have that, as we saw initially,
    we only had 46% alignment; that's not very reflective of how you would want to
    evaluate your system.
  topic: safety/technical
- impact_reason: Introduces the novel concept of 'multi-party LLM alignment'—aligning
    the model simultaneously to the end-user (via queries) and the system creator
    (via judge instructions)—suggesting a new research frontier.
  relevance_score: 10
  source: llm_enhanced
  text: 'It''s interesting that you''re going for multi-party alignment, and it makes
    me curious about whether there''s specific research on how to align an LLM not
    just to a particular party but to two parties in this case: the user that''s issuing
    queries... but then you''re also aligning to the creator of the system and their
    input to the LLM as judge part.'
  topic: safety/predictions
- impact_reason: Highlights the over-reliance and potential pitfalls of using public
    benchmarks (like M-Tub) to judge model superiority without considering context
    or limitations.
  relevance_score: 9
  source: llm_enhanced
  text: If you're familiar with the Retrieval Space, M-Tub is a pretty popular benchmark
    for embedding models. If you see the release of any new model, you'll probably
    see something like, "Oh, our model achieved this score on M-Tub. We outperformed
    this other model on M-Tub." And people would just kind of take that score and
    assume, "Okay, this model is better just because it did better on this benchmark."
  topic: safety/strategy
- impact_reason: A direct, strong critique of the current state of evaluation in the
    embedding/retrieval space, signaling the need for better methods.
  relevance_score: 9
  source: llm_enhanced
  text: But there are so many problems with these public benchmarks.
  topic: safety/strategy
- impact_reason: 'Defines the core mission of generative benchmarking: moving from
    subjective ''vibes'' to systematic debugging.'
  relevance_score: 9
  source: llm_enhanced
  text: We wanted people to be able to systematically debug their AI systems. So,
    that's kind of where generative benchmarking came about.
  topic: strategy
- impact_reason: 'Provides a concise definition of the proposed solution: custom,
    data-centric evaluation sets.'
  relevance_score: 9
  source: llm_enhanced
  text: At the high level, generative benchmarking is essentially generating a custom
    eval set based on your own data.
  topic: technical
- impact_reason: Lays out the specific, novel architecture of their proposed evaluation
    pipeline.
  relevance_score: 9
  source: llm_enhanced
  text: 'This is broken down into two main steps: we first do document filtering,
    and then we do the actual query generation.'
  topic: technical
- impact_reason: Provides crucial, real-world insights into user query patterns (vagueness,
    statement format) that evaluation systems must mimic for realism.
  relevance_score: 9
  source: llm_enhanced
  text: a lot of users using a technical chatbot like the one that Weights & Biases
    has, they probably wouldn't be asking queries in complete sentences. It's more
    like statements, which you typically see in a lot of chatbot applications. People
    are very vague with their queries; it's not super comprehensive.
  topic: technical/strategy
- impact_reason: Highlights a critical difference between idealized benchmark queries
    and real-world user behavior in chatbot applications, emphasizing the need to
    model vague, non-grammatical inputs.
  relevance_score: 9
  source: llm_enhanced
  text: People are very vague with their queries; it's not super comprehensive. So,
    we want to reflect that as well.
  topic: strategy/technical
- impact_reason: 'Details a specific technique in query generation: using real-world,
    vague example queries to train the generator to mimic actual user input styles,
    moving beyond polished benchmark data.'
  relevance_score: 9
  source: llm_enhanced
  text: We also give it some example queries as well. And that's mainly for the purposes
    of steering the LLM to generate queries in a realistic style. So, like I mentioned
    before, a lot of people who use these chatbot applications, the queries are very
    vague; they're not formed as a complete question with a question mark and everything.
  topic: technical
- impact_reason: Strong critique of relying solely on public benchmarks for RAG evaluation,
    stressing that production data reflects unpolished, real-world user intent.
  relevance_score: 9
  source: llm_enhanced
  text: We're trying to model what you would actually see in production, which is
    pretty different from the public datasets that I spoke about earlier. Because
    I think yeah, in these public datasets, a lot of questions are very well-formed
    and polished.
  topic: strategy/technical
- impact_reason: Identifies 'missing context' in chunks as a common RAG failure mode
    and suggests contextual rewriting as a high-impact, albeit expensive, optimization
    strategy.
  relevance_score: 9
  source: llm_enhanced
  text: We noticed a lot of chunks were missing context, which is a pretty common
    problem in a lot of these RAG applications. You can just chunk up documents, but
    some chunks might just not be very valuable if they don't have any context on
    where they came from. And trying to fix problems like those actually boosts retrieval
    performance a lot.
  topic: technical
- impact_reason: Challenges the reliance on ranking metrics like NDCG in RAG evaluation,
    arguing that for LLM context windows, simple retrieval (Recall@K) is sufficient,
    simplifying evaluation.
  relevance_score: 9
  source: llm_enhanced
  text: 'We mostly looked at Recall@K, just because there are other scores that are
    used in a lot of these retrieval research papers, like people use NDCG. But one
    thing that has been brought up is that the ranking of chunks in the context of
    an LLM doesn''t really matter. It doesn''t affect the performance of an LLM if
    you have the relevant chunk at the beginning versus at the end. So, we don''t
    look at NDCG. We just look at recall, which is: was it retrieved? Was there a
    relevant document retrieved or not?'
  topic: technical
- impact_reason: Introduces a specific, named framework (EvalGen) for aligning LLM
    judges, addressing the critical issue of trusting automated evaluation metrics.
  relevance_score: 9
  source: llm_enhanced
  text: Alignment is a very important part of this work. We specifically use this
    framework called EvalGen, which is basically a framework for aligning an LLM judge
    to human preferences.
  topic: safety/technical
- impact_reason: A strong strategic warning about the current state of LLM evaluation
    tools, emphasizing that human alignment is non-negotiable for reliable automated
    judging.
  relevance_score: 9
  source: llm_enhanced
  text: So, I think a lot of people just blindly use an LLM judge without any alignment,
    just assuming that it is aligned. But I think we're too far from that right now,
    and we do need some level of human alignment to actually confidently put the LLM
    judge to use.
  topic: safety/strategy
- impact_reason: Quantifies the extreme sensitivity of LLM judges to prompt wording
    and criteria selection, showing a significant performance swing (46% to 70%+)
    based purely on prompting adjustments.
  relevance_score: 9
  source: llm_enhanced
  text: We noticed it was pretty sensitive because we were just iterating on three
    criteria. And based on how we were wording those criteria or how we were maybe
    taking one out and adding in another, it would range quite a bit. So, as we said
    in the report, it improved from 46% to around the 70s. So, that's a pretty big
    difference just based on how you're prompting the LLM judge.
  topic: technical
- impact_reason: Highlights the tight coupling between the evaluation framework (EvalGen)
    and the quality of the LLM judge's alignment, emphasizing that prompt engineering
    is central to reliable evaluation.
  relevance_score: 9
  source: llm_enhanced
  text: Yes, we noticed that the prompting strategies through using EvalGen. I guess
    they both kind of go hand in hand because EvalGen is essentially evaluating how
    well the prompting strategy allows your LLM judge to be aligned with your premises.
  topic: technical
- impact_reason: 'Offers a practical data efficiency insight: high-quality evaluation
    can be achieved by manually labeling a very small fraction (200 out of 13,000
    chunks) of the total data when using an LLM judge.'
  relevance_score: 9
  source: llm_enhanced
  text: We had around 13,000 documents, and out of those, we would manually label
    200, which is a pretty small percentage; it doesn't require that much human labeling.
  topic: business
- impact_reason: Positions generative benchmarking as a crucial tool for bootstrapping
    evaluation when historical query data is unavailable, lowering the barrier to
    entry for RAG system testing.
  relevance_score: 9
  source: llm_enhanced
  text: If you don't have a set of queries that you can test your retrieval system
    on, we would generate that for you. All you need is just a set of documents that
    you're using for your retrieval system, which people already have.
  topic: business
- impact_reason: Provides a real-world example of how rigorous, data-specific evaluation
    (using EvalGen) led to a concrete change in production tooling (switching embedding
    models), validating the tool's utility.
  relevance_score: 9
  source: llm_enhanced
  text: For us, previously we just used OpenAI's small model, but after looking at
    this, it actually performed—it was one of the worst-performing models out of the
    ones that we tested. So, yeah, I think from now on, we'll probably go with something
    like Voyage's model, which works pretty well on technical documentation like this.
  topic: business
- impact_reason: Advocates for component-level debugging over holistic 'vibe checks,'
    promoting a systematic engineering approach to complex AI pipelines.
  relevance_score: 9
  source: llm_enhanced
  text: I think there is a more systematic approach to this, and one of the best ways
    to start off is looking at the outputs of each component of your system. So, if
    you have RAG, look at what documents are actually being retrieved and try to figure
    out what's going on from there, rather than just looking at the output and seeing
    what the vibes are.
  topic: strategy
- impact_reason: Identifies 'distractors' (irrelevant retrieved context) as a major
    cause of performance degradation in LLM outputs, linking back to the necessity
    of precise retrieval.
  relevance_score: 9
  source: llm_enhanced
  text: One thing that comes up a lot in RAG systems is that if you have a lot of
    distractors in your LLM prompt, it leads to very degraded performance.
  topic: technical
- impact_reason: 'Provides a key indicator for detecting potential data leakage or
    memorization in LLMs during evaluation: consistent, verbatim query generation
    matching known benchmark datasets.'
  relevance_score: 9
  source: llm_enhanced
  text: Yes, like the LLM could have asked about anything, but if you see constant
    patterns of identically generated queries, then I think that's a pretty good sign
    that the LLM has seen this dataset before.
  topic: safety/technical
- impact_reason: Directly addresses and debunks the 'easy button' misconception surrounding
    generative benchmarking, stressing that it is not fully automated.
  relevance_score: 9
  source: llm_enhanced
  text: No, and I think that's a very common misconception that people have. If you
    just hear 'generative benchmarking,' you might just think that I just need to
    press a button, and then it generates an eval for me, but that's definitely not
    the case.
  topic: strategy
- impact_reason: Stresses the necessity of a 'human in the loop' for reliable generative
    evaluation, specifically mentioning the role of providing context/examples to
    steer LLM behavior toward realism.
  relevance_score: 9
  source: llm_enhanced
  text: We do need some human in the loop to actually make this process more reliable
    in terms of how aligned it is to human judgment. And this takes form in a few
    ways. One is the context and example queries that are provided; that helps steer
    the LLM in a way to generate realistic queries.
  topic: safety/strategy
- impact_reason: Provides a philosophical framework suggesting that standard instruction-following
    alignment is inherently multi-party (developer vs. user utility), framing the
    discussion within established LLM alignment theory.
  relevance_score: 9
  source: llm_enhanced
  text: I guess thinking about it more, you could argue that maybe the case is that
    a lot of the core LLM alignment work is fundamentally multi-party in a sense that
    if you think about instruction following, you want to follow the developer's instructions,
    but you also want to be useful to the user.
  topic: safety/strategy
- impact_reason: Identifies a fundamental, persistent challenge in the AI/ML lifecycle,
    especially compared to deterministic software systems.
  relevance_score: 8
  source: llm_enhanced
  text: how difficult it is to systematically evaluate AI systems.
  topic: strategy
- impact_reason: Clearly articulates the core difference between traditional software
    testing and AI system evaluation (deterministic vs. probabilistic), which drives
    the need for new evaluation paradigms.
  relevance_score: 8
  source: llm_enhanced
  text: If you think about this analogy with software systems, it's very easy to evaluate
    them. You have these very simple quotas, you run them, and then you get a deterministic
    output. But if you have AI systems, all your outputs are probabilistic.
  topic: technical
- impact_reason: A relatable and honest admission about the common, unscientific starting
    point for many developers building AI/RAG systems, emphasizing the need for rigor.
  relevance_score: 8
  source: llm_enhanced
  text: I think initially when I started building out in this space, I would just
    evaluate based off of vibes, which is really bad.
  topic: business/strategy
- impact_reason: 'Pinpoints a major failure mode of public benchmarks: lack of fidelity
    to real-world, messy production data.'
  relevance_score: 8
  source: llm_enhanced
  text: The datasets are also very clean and polished, whereas in the real world,
    the data is very messy.
  topic: safety/strategy
- impact_reason: Positions generative benchmarking as an accessible entry point for
    evaluation, especially for teams lacking historical query logs.
  relevance_score: 8
  source: llm_enhanced
  text: It's kind of helping people with the first step if they don't have a golden
    dataset to start with.
  topic: business/strategy
- impact_reason: 'Outlines the ideal feedback loop for RAG evaluation: starting with
    synthetic data and continuously refining it with real user interaction.'
  relevance_score: 8
  source: llm_enhanced
  text: The eventual goal there is for people to continue iterating on that dataset.
    If they have incoming user queries, hopefully they use that to align their golden
    dataset even further...
  topic: strategy
- impact_reason: Details the input requirements and output goal for generative benchmarking
    in the context of RAG systems.
  relevance_score: 8
  source: llm_enhanced
  text: And we do this for retrieval specifically, so you can kind of think of it
    as, "Okay, the user inputs a set of documents, gives us some context on what their
    application is," and then from that, we generate queries to test your retrieval
    system on.
  topic: technical
- impact_reason: Highlights the two key innovations that separate their method from
    naive synthetic generation.
  relevance_score: 8
  source: llm_enhanced
  text: I think that's definitely one of the core differentiators. I say that and
    the way that we are generating queries.
  topic: technical
- impact_reason: Explains the role of 'context injection' (similar to system prompts)
    in guiding both document relevance filtering and query generation for tailored
    evaluation.
  relevance_score: 8
  source: llm_enhanced
  text: The context is basically what your RAG application is for. So, for example,
    in the case of Weights & Biases, the context would be something like, "This is
    a technical support bot for Weights & Biases."
  topic: technical
- impact_reason: Provides a nuanced RAG strategy, arguing that filtering must occur
    at the chunk level even when the source document is entirely relevant, citing
    examples like boilerplate text (e.g., goodbyes).
  relevance_score: 8
  source: llm_enhanced
  text: I guess just to clarify, we're doing both chunk filtering and document filtering.
    So, we would filter for chunks as well because I think in a lot of cases, even
    if the document is relevant—for example, in the case of podcast transcripts, all
    documents are relevant—but there are probably chunks that wouldn't be good to
    generate a query from. For example, say you have the end of a podcast where you're
    saying goodbye or something. You probably don't want to retrieve that.
  topic: technical
- impact_reason: 'Outlines the core components required for advanced LLM alignment
    frameworks: defined criteria (relevance, completeness) and manually labeled ground
    truth data.'
  relevance_score: 8
  source: llm_enhanced
  text: For EvalGen, you basically need a set of criteria. So, in our example, we
    just use criteria like relevance—is this relevant to our context? We use completeness,
    which is just how is the overall quality of this LLM judge? I think there's one
    other criteria as well. But yeah, basically, you would write out these criteria,
    and then you would also have ground truth labels for your documents.
  topic: technical
- impact_reason: Explains the thresholding mechanism used to convert the LLM judge's
    evaluation into a binary quality label, linking it back to the ground truth for
    alignment scoring.
  relevance_score: 8
  source: llm_enhanced
  text: If it passed two out of the three criteria, then we would just mark it as
    a good quality document. So, that's how we got the LLM judge labels. And once
    we had those labels, we would compare them with our ground truth, and that's how
    we get the alignment score.
  topic: technical
- impact_reason: 'Identifies a powerful secondary benefit of generative benchmarking:
    identifying and proactively addressing gaps in the underlying knowledge base.'
  relevance_score: 8
  source: llm_enhanced
  text: Also, it could help in determining if you have any information gaps in your
    document corpus. If users are asking about this one topic but your document corpus
    isn't able to answer that, then people can proactively act upon that and fix it
    before more users run into that problem.
  topic: strategy
- impact_reason: Provides a concrete example of how distractors cause semantic confusion
    in the LLM, reinforcing the idea that retrieval quality directly impacts the LLM's
    ability to follow instructions.
  relevance_score: 8
  source: llm_enhanced
  text: So, then the LLM might get distracted, and it might focus on how it might
    mistake maybe a function for filtering a collection when you were really asking
    about creating it. And we noticed this comes up pretty often, so that's why we
    think retrieval is pretty important because your LLM can get very distracted by
    which documents are retrieved.
  topic: technical
- impact_reason: 'Offers practical advice on setting the retrieval ''K'' value: prioritize
    minimizing distractors over adhering to a fixed number, requiring empirical testing
    based on the specific dataset.'
  relevance_score: 8
  source: llm_enhanced
  text: I think you want as few distractors as possible. There's no one number that
    I would recommend to you, so I think you really just have to look at your data,
    test out different K-values, different numbers of documents to retrieve.
  topic: technical
- impact_reason: Provides actionable evaluation methodology for RAG tuning, suggesting
    the use of different Recall metrics (K values) to understand performance trade-offs
    based on the specific application needs.
  relevance_score: 8
  source: llm_enhanced
  text: If you run evals, you can run evals with different K-values, you can do Recall@1,
    Recall@3, Recall@10, see how the scores differ, and maybe go off of that because
    it does change a lot for people.
  topic: technical
- impact_reason: 'Details a robust methodology for validating generative evaluation
    sets: checking if the relative performance ranking of underlying components (like
    embedding models) remains consistent across both ground truth and generated data.'
  relevance_score: 8
  source: llm_enhanced
  text: We compare the scores for generic queries, the scores for ground truth queries,
    and then we do that for each embedding model, and we see that we have consistent
    rankings for embedding models, regardless of whether you're looking at the ground
    truth queries or generic queries.
  topic: technical
- impact_reason: Focuses the purpose of evaluation on practical decision-making for
    developers—choosing the right infrastructure components—and highlights that inconsistent
    rankings invalidate the evaluation method.
  relevance_score: 8
  source: llm_enhanced
  text: 'Because ultimately, this is what matters to a developer building a RAG application:
    which embedding model should I use? So, if there is no switching positions...
    then that would not be good for choosing an embedding model.'
  topic: business/strategy
- impact_reason: Describes the current, flawed decision-making process in the industry
    based on easily accessible but potentially misleading benchmark scores.
  relevance_score: 7
  source: llm_enhanced
  text: The first thing that people do is they probably look into benchmarks like
    M-Tub, and they kind of see scores about that. And then they make a decision on
    which embedding model to use.
  topic: business
- impact_reason: Highlights the educational and cultural shift required in the developer
    community regarding evaluation practices.
  relevance_score: 7
  source: llm_enhanced
  text: I hope that from that, people get more familiar with the idea of doing evals
    and also understand the importance of it as well.
  topic: strategy
- impact_reason: 'Identifies a secondary benefit of using production query logs: assessing
    the coverage and relevance gaps within the existing document corpus.'
  relevance_score: 7
  source: llm_enhanced
  text: If you are able to work with real production data, then you can also use that
    to evaluate how well your document corpus reflects what your users are asking
    about.
  topic: business/strategy
- impact_reason: Provides a practical business/cost consideration for advanced RAG
    techniques like contextual rewriting, noting the computational expense.
  relevance_score: 7
  source: llm_enhanced
  text: I wouldn't say it's super common because it is pretty expensive to do. I mean,
    you're passing it into an LLM every time. So, it really depends on your use case.
  topic: business
- impact_reason: Provides a tangible data point for chunk size (around 400 tokens)
    while correctly advising that chunking strategy must be use-case dependent.
  relevance_score: 7
  source: llm_enhanced
  text: But I'd say there were typically around maybe 400 tokens, somewhere around
    that range. But yeah, I think your chunking strategy really depends on your use
    case as well.
  topic: technical
source: Unknown Source
summary: '## Generative Benchmarking with Kelly Hong - #728: Comprehensive Summary


  This podcast episode features Sam Charrington in conversation with Kelly Hong, a
  researcher at Chroma, focusing on the introduction and necessity of **Generative
  Benchmarking**—a novel approach to systematically evaluating Retrieval-Augmented
  Generation (RAG) systems and embedding models. The core narrative addresses the
  inadequacy of current public benchmarks and the common practice of "vibe checking"
  system performance.


  ### 1. Focus Area

  The primary focus is on **Evaluation Methodologies for AI/ML Systems**, specifically
  within the **Retrieval Space (RAG)**. Key technologies discussed include **embedding
  models**, **vector databases**, **synthetic data generation for evaluation**, and
  the use of **LLMs as judges** for automated assessment.


  ### 2. Key Technical Insights

  *   **Two-Step Generative Benchmarking Process:** The method centers on creating
  custom, representative evaluation sets by first performing **document/chunk filtering**
  (to ensure relevance to the use case) and then **context-steered query generation**
  (to mimic realistic, often vague, user queries).

  *   **Importance of Contextual Alignment:** Effective evaluation requires injecting
  specific application context (e.g., "This is a technical support bot") into both
  the filtering and query generation steps to ensure the synthetic test set reflects
  the true production environment.

  *   **LLM Judge Alignment is Crucial:** Blindly using an LLM as a judge for relevance
  or filtering yields poor results (initially 46% alignment). Frameworks like **EvalGen**
  are necessary to iterate on prompting and criteria to align the LLM judge''s decisions
  with human preferences (achieving over 70% alignment).


  ### 3. Business/Investment Angle

  *   **Public Benchmark Limitations:** Scores on generic benchmarks like M-Tub often
  fail to predict real-world performance; models that outperform on M-Tub may perform
  worse on domain-specific, messy production data.

  *   **Model Performance Divergence:** The conversation highlighted empirical findings
  where one embedding model (Jina AI) performed worse on real-world data than expected
  based on its M-Tub score, while another (Voyage 3 Large) performed best, underscoring
  the need for custom evaluation before deployment.

  *   **Cost vs. Benefit of Advanced Techniques:** Techniques like **contextual rewriting**
  (prepending context to chunks) can significantly boost retrieval performance but
  require careful consideration regarding the computational cost of running LLMs on
  every chunk.


  ### 4. Notable Companies/People

  *   **Kelly Hong (Chroma):** Researcher and lead on the Generative Benchmarking
  project.

  *   **Chroma:** The company developing vector database solutions and focusing on
  systematic AI system debugging and evaluation.

  *   **Weights & Biases (W&B):** Used as a case study partner; production query logs
  from their technical support bot informed the development and validation of the
  generative benchmarking approach.

  *   **Embedding Model Providers:** OpenAI (text-embedding-3-large), Jina AI, and
  Voyage were mentioned in the context of comparative performance testing.


  ### 5. Future Implications

  The industry is moving away from relying solely on static, public benchmarks toward
  **dynamic, synthetic evaluation sets** tailored to specific application data. The
  future of robust RAG deployment hinges on making evaluation accessible (not just
  for experts) and ensuring that the tools used for judging (LLM judges) are rigorously
  aligned with human expectations.


  ### 6. Target Audience

  This episode is highly valuable for **AI/ML Engineers, RAG Developers, MLOps Professionals,
  and Technical Product Managers** involved in building, deploying, and maintaining
  production-grade LLM and retrieval applications.'
tags:
- artificial-intelligence
- investment
- ai-infrastructure
- generative-ai
- openai
title: 'Generative Benchmarking with Kelly Hong - #728'
topics:
- keywords:
  - ai
  - machine learning
  - deep learning
  - neural networks
  - llm
  - large language model
  mentions: 108
  prominence: 1.0
  topic: artificial intelligence
- keywords:
  - investment
  - funding
  - valuation
  - ipo
  - acquisition
  mentions: 8
  prominence: 0.8
  topic: investment
- keywords:
  - gpu
  - tensor
  - training
  - inference
  - model deployment
  - vector database
  mentions: 3
  prominence: 0.3
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
<!-- Processing completed: 2025-10-05 22:35:13 UTC -->
