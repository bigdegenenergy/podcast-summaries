---
companies:
- category: unknown
  confidence: medium
  context: has made an impact on people's lives. My name is Matt Green, and I head
    up blockchain, digital assets, and te
  name: Matt Green
  position: 302
- category: unknown
  confidence: medium
  context: gital assets, and technology disputes at law firm Lauren Stevens. This
    week, I speak to Harry Donnelly, founder of
  name: Lauren Stevens
  position: 392
- category: unknown
  confidence: medium
  context: at law firm Lauren Stevens. This week, I speak to Harry Donnelly, founder
    of Circuit, a platform that enables the
  name: Harry Donnelly
  position: 430
- category: unknown
  confidence: medium
  context: FTX, like your FTX, or more specifically, like a Prime Trust. If you're
    familiar with Prime Trust, there are c
  name: Prime Trust
  position: 10591
- category: unknown
  confidence: medium
  context: rcuit, you can only move funds to point B for me. Point B being a wallet
    I set up. So, this means if you lo
  name: Point B
  position: 12700
- category: unknown
  confidence: medium
  context: nded by—and you put this in, I quite liked it—the National Institute of
    Standards and Technology, they define the key-
  name: National Institute
  position: 15903
- category: unknown
  confidence: medium
  context: s instance. Cool. I'll just clarify. So, it's the NIST CSF. Sorry, I was
    greedy for homework for this. And i
  name: NIST CSF
  position: 16246
- category: unknown
  confidence: medium
  context: ', "Okay, we talked about this disaster situation. Imagine I have a wallet
    provider, let''s say, my Fireblocks,'
  name: Imagine I
  position: 16917
- category: unknown
  confidence: medium
  context: d help like me to. Yeah, yeah, help me out. Okay. With BitBay, what happened
    with BitBay is basically they—ther
  name: With BitBay
  position: 20031
- category: unknown
  confidence: medium
  context: lion was lost, which is kind of crazy, and it was North Korea's Lazarus
    Group, which took the funds. What they
  name: North Korea
  position: 20260
- category: unknown
  confidence: medium
  context: which is kind of crazy, and it was North Korea's Lazarus Group, which took
    the funds. What they did is they were
  name: Lazarus Group
  position: 20274
- category: unknown
  confidence: medium
  context: signed instruction to sweep all the funds across. When I talk about a pre-signed
    instruction previously, w
  name: When I
  position: 22571
- category: Infrastructure/Security
  confidence: high
  context: A platform providing transaction-layer security and automatic asset extraction
    to recover crypto assets during key loss, hacks, or custody failures.
  name: Circuit
  source: llm_enhanced
- category: Infrastructure/Custody
  confidence: high
  context: Mentioned as a third-party wallet provider/custodian whose failure can
    trap customer funds, which Circuit's software is designed to protect against.
  name: Fireblocks
  source: llm_enhanced
- category: Exchange/Institution (Example)
  confidence: high
  context: Used as a prominent example of an exchange/custodian failure where customer
    funds were trapped and operations ceased.
  name: FTX
  source: llm_enhanced
- category: Institution/Custody (Example)
  confidence: high
  context: Cited as an example of a US custodian that failed entirely, trapping customer
    assets.
  name: Prime Trust
  source: llm_enhanced
- category: Layer 1 Project (Example)
  confidence: medium
  context: Referenced during an incident where a wallet provider froze, leading to
    funds being lost, implying the underlying ecosystem failure.
  name: Terra/Luna
  source: llm_enhanced
- category: exchange
  confidence: high
  context: A platform that was hacked in February of the current year, resulting in
    a $1.4 billion loss due to a front-end compromise leading to wallet control being
    signed over.
  name: BitBay
  source: llm_enhanced
- category: infrastructure
  confidence: high
  context: The front-end used by BitBay to showcase the transaction that was signed,
    leading to the hack.
  name: SafeWallet
  source: llm_enhanced
- category: organization
  confidence: high
  context: North Korean state-sponsored hacking group attributed with the BitBay hack.
  name: Lazarus Group
  source: llm_enhanced
- category: infrastructure
  confidence: high
  context: Mentioned as a hardware wallet provider whose devices the speaker's software
    has been tested or enabled for (e.g., dealing with seed phrases).
  name: Ledger
  source: llm_enhanced
date: 2025-10-14 18:13:09 +0000
duration: 30
has_transcript: false
layout: episode
llm_enhanced: true
original_url: https://audio.listennotes.com/e/p/5273a6b57cff4a43b9c520812645e9f2/
processing_date: 2025-10-16 04:44:27 +0000
quotes:
- length: 128
  relevance_score: 3
  text: Circuit is built to solve what we think is one of the biggest problems in
    crypto today, which is catastrophic operational losses
  topics: []
- length: 131
  relevance_score: 3
  text: You have to basically go after the fact to try and hunt things down, and you
    know how difficult it is and how it often doesn't work
  topics: []
- length: 76
  relevance_score: 3
  text: So, you have to have had a separate private key somewhere else to decrypt
    it
  topics: []
- length: 239
  relevance_score: 3
  text: This enables you to—our key-based recovery means you have to reconstitute
    the private key, which means you have to create the single point of failure, which
    means at that point, who's doing it is probably some form of engineer on your
    team
  topics: []
- length: 245
  relevance_score: 3
  text: That was the key-based recovery is in a disaster of the wallet provider failing,
    and you have to try and reconstitute the keys to get the funds out versus that
    was signing over control to someone else who could then use it to drain all the
    funds
  topics: []
- impact_reason: 'This is the core value proposition: automated, preventative response
    to major security failures (custodian failure, key loss, theft) without introducing
    a new central point of trust (Circuit).'
  relevance_score: 10
  source: llm_enhanced
  text: What we enable you to do is say, in the event of a total disaster—so, for
    example, your custodian, your wallet provider, fails, you lose your private key,
    or if someone steals your private key, or someone steals your API credentials
    and is trying to steal your funds—Circuit enables you to automatically respond
    to that, to take the funds and move them to a safe place, a safe vault, or an
    isolated destination, and does so without you having to give us private key material.
  topic: technology/security
- impact_reason: 'Defines the philosophical approach: augmentation, not replacement,
    of existing security standards (MPC, multisig).'
  relevance_score: 10
  source: llm_enhanced
  text: What's needed is a security model that separates recovery from key availability,
    not to replace key-based systems, but to reinforce them.
  topic: technology/strategy
- impact_reason: 'Technical definition of AAE: a failsafe operating at the transaction
    layer, independent of the key management layer.'
  relevance_score: 10
  source: llm_enhanced
  text: This white paper introduces automatic asset extraction, a transaction-layer
    failsafe that functions independently of the primary key infrastructure.
  topic: technology
- impact_reason: 'Detailed technical explanation of AAE: separating the ''sign'' step
    from the ''broadcast'' step to create usable, pre-authorized instructions.'
  relevance_score: 10
  source: llm_enhanced
  text: What we do is we separate it out. We sign something, so we say, 'Okay, we've
    given it a cryptographic stamp so that the blockchain will accept it and knows
    it's from us,' but we haven't yet broadcast it, which means we haven't given it
    to the blockchain to cause an action to happen...
  topic: technology
- impact_reason: Provides a clear architectural stack diagram (Wallet/Custody -> Keys
    -> Blockchain) to explain where Circuit intervenes—below the key layer but above
    the chain layer.
  relevance_score: 10
  source: llm_enhanced
  text: It's like every wallet provider, custodian, et cetera, is a layer on top of
    private keys, which is on top of blockchains. And so, if they stop working, the
    blockchain is still operating underneath; you just can't access the key to take
    an action and perform it.
  topic: technology/architecture
- impact_reason: 'Highlights a key institutional benefit: mitigating concentration
    risk by ensuring interoperability and failover between multiple custody/wallet
    providers.'
  relevance_score: 10
  source: llm_enhanced
  text: We are agnostic to that. So, ultimately, most of the institutions who work
    with them have multiple different wallet infrastructure setups... we effectively
    enable is we remove any aggregation and concentration risk between them. If one
    goes down, we get the funds out to another.
  topic: business
- impact_reason: Directly contrasts traditional recovery (which necessitates creating
    a single point of failure) with modern security practices like MPC.
  relevance_score: 10
  source: llm_enhanced
  text: One, it's a big security risk because it creates a single point of failure.
    The whole reason for using things like MPC is that you never create a single point
    of failure. This enables you to—our key-based recovery means you have to reconstitute
    the private key, which means you have to create the single point of failure...
  topic: technology
- impact_reason: Applies the technology directly to a major industry failure (FTX
    insolvency), suggesting it could have saved client funds from bankruptcy proceedings.
  relevance_score: 10
  source: llm_enhanced
  text: You've already got the assets safe. Exactly. So, in the example of—we've had
    clients who wanted to extract their funds from FTX even after the process of distribution—and
    I wonder whether your solution would have been excellent if it had been attached
    to FTX because though that money would have been pulled out and wouldn't have
    even been part of the proceedings.
  topic: investment
- impact_reason: A powerful hypothetical use case demonstrating the potential of proactive
    security solutions to bypass centralized exchange failures (like FTX bankruptcy)
    by immediately sweeping assets.
  relevance_score: 10
  source: llm_enhanced
  text: So, in the example of—we've had clients who wanted to extract their funds
    from FTX even after the process of distribution—and I wonder whether your solution
    would have been excellent if it had been attached to FTX because though that money
    would have been pulled out and wouldn't have even been part of the proceedings.
  topic: adoption/investment
- impact_reason: 'This is a crucial explanation of the inherent risk in centralized
    exchanges: the use of omnibus wallets, meaning customer balances are often just
    IOUs, not direct on-chain ownership.'
  relevance_score: 10
  source: llm_enhanced
  text: For exchanges, if you're an end-user, it's a little bit more tricky because
    what exchanges do behind the scenes, if people are familiar, is that instead of
    just saying, "These are your funds in your wallet," they have big wallets, omnibus
    wallets. They pull all the assets together, and they say, "Here's your balance,"
    and you see it on your screen, on your front end, but it's really coming over
    the bunch of other people. It's an IOU.
  topic: adoption/technology
- impact_reason: 'Clearly defines the unique value proposition: mitigating risks even
    *after* a primary key/credential breach has occurred, acting as the final line
    of defense.'
  relevance_score: 10
  source: llm_enhanced
  text: So, you've got an extra level of security, extra level of security. If someone's
    already moving funds out or stolen the private key or stolen the credential, they
    can then bypass all that security and sign whatever they want to move the funds
    out. And that's where AAE comes in.
  topic: technology
- impact_reason: 'Directly identifies the core, high-stakes problem Circuit addresses:
    massive, irrecoverable operational losses in the crypto space.'
  relevance_score: 9
  source: llm_enhanced
  text: Circuit is built to solve what we think is one of the biggest problems in
    crypto today, which is catastrophic operational losses.
  topic: business/strategy
- impact_reason: Highlights the scale of the loss problem and reinforces the fundamental
    nature of crypto assets (bearer assets) that makes recovery so difficult.
  relevance_score: 9
  source: llm_enhanced
  text: We still lose billions and billions of dollars every year, and because these
    are bearer assets, they're effectively irrecoverable.
  topic: adoption/risk
- impact_reason: A concise summary of the product's capability, focusing on operational
    continuity despite catastrophic key failure.
  relevance_score: 9
  source: llm_enhanced
  text: Circuit gives ops teams the power to extract assets from any wallet, even
    after key loss, hacks, or unexpected custody failures. No more downtime, dead
    ends, or dependency on keys alone.
  topic: technology/business
- impact_reason: Introduces and explains the proprietary concept ('automatic asset
    extraction') using a familiar 'if-this-then-that' structure, tailored for trustless
    environments.
  relevance_score: 9
  source: llm_enhanced
  text: We've built a technology we call automatic asset extraction, and it's pretty
    flexible. Think a bit like the ability to say, if this happens, then I want this
    to occur at a later point in time, and you can do it in crypto, which is a place
    where you don't want to have to trust anyone, but you also want to have lots of
    rigorous controls on top of it.
  topic: technology/innovation
- impact_reason: Connects the product's necessity to a major DeFi/market event (Terra/Luna),
    illustrating the danger of frozen access during market volatility.
  relevance_score: 9
  source: llm_enhanced
  text: Like the incident during Terra/Luna, someone was using a wallet provider,
    that wallet provider froze, and they had to watch all of their funds go all the
    way down to zero, and they couldn't do anything.
  topic: defi/risk
- impact_reason: Clearly states how AAE bridges the gap between detection and action
    when keys are unavailable.
  relevance_score: 9
  source: llm_enhanced
  text: AAE enables assets to move from danger to safety without requiring access
    to compromised or inaccessible keys, filling the critical response gap left open
    by current systems.
  topic: technology/security
- impact_reason: 'Lists the three primary ways key-based security fails: compromise,
    loss, or custodian failure, reinforcing the need for a secondary layer.'
  relevance_score: 9
  source: llm_enhanced
  text: If this fails, if someone gets access to your private key, you're done effectively.
    If you lose access to your private key, or you lose it entirely, or you lose the
    ability to access it because the custodian or the person who's holding it for
    you goes down, like your FTX, like your FTX, or more specifically, like a Prime
    Trust.
  topic: risk/security
- impact_reason: 'Explains the utility of the pre-signed transaction: it acts as an
    executable instruction available even when primary signing authority is lost.'
  relevance_score: 9
  source: llm_enhanced
  text: Because we've signed it, we can still use it at a later point in time, which
    means that if you lose access to your keys or if you want to take an action, you
    have this pre-created instruction that enables you to do so.
  topic: technology
- impact_reason: 'Defines the bypass mechanism: using pre-signed transactions to jump
    over the failed layer (custodian/key access) directly to the functioning layer
    (blockchain).'
  relevance_score: 9
  source: llm_enhanced
  text: So, all we've done is we've gone through this ahead of time, signed it. So,
    now we can effectively bypass it in the event of disaster to then take the action
    to move the funds out to a different wallet, which is still operating.
  topic: technology
- impact_reason: A detailed breakdown of the painful, multi-step process of traditional
    key recovery, emphasizing its complexity and time consumption.
  relevance_score: 9
  source: llm_enhanced
  text: Key-based recovery is how people generally approach recovery at the moment...
    you have to decrypt it. So, you have to have had a separate private key somewhere
    else to decrypt it. Then you need to reconstitute the private key... Then you
    need to go and derive all the different wallets... Then you need to go and say,
    'Okay, well, I'm not going to just leave it in raw private key form... I'm going
    to have to move it to another wallet.'
  topic: technology
- impact_reason: 'Articulates the business continuity failure of traditional recovery:
    it happens when the organization is already under maximum stress.'
  relevance_score: 9
  source: llm_enhanced
  text: As you can see, that is labor-intensive, timely—timely—but it's also just
    like it's happening at the worst possible time, which is when your business is
    down, and your customers are saying, 'Where's our money?'
  topic: business
- impact_reason: Contrasts the complex manual recovery with the proposed solution's
    simple, automated 'red button' execution via a secure web interface.
  relevance_score: 9
  source: llm_enhanced
  text: It's like, 'Ah, what do we do?' Well, rather than having to go through that
    key reconstitution process... instead, you just go to our web app, you log in,
    you do your 2FA, you coordinate the people online, sign your quorum, press the
    red button, and all the funds get swept across.
  topic: technology
- impact_reason: Describes the continuous, dynamic nature of their solution, which
    solves the state-change problem inherent in static pre-signing.
  relevance_score: 9
  source: llm_enhanced
  text: So, we've built infrastructure that's constantly monitoring, constantly creating
    new pre-signed transactions behind the scenes, and doing so in a safe way.
  topic: technology
- impact_reason: Crucially notes that the recovery instructions are stored *outside*
    the primary wallet provider, enhancing resilience against that provider failing.
  relevance_score: 9
  source: llm_enhanced
  text: We've got a little bit more. So, what we do is we've done that behind the
    scenes where it's constantly creating, storing, and managing these pre-signed
    transactions, and then encrypting them and storing them outside of your wallet
    provider.
  topic: strategy
- impact_reason: 'A clear summary of the superior recovery workflow: minimal steps,
    leveraging existing security (2FA/quorum) to trigger the pre-authorized escape.'
  relevance_score: 9
  source: llm_enhanced
  text: So, now imagine you lose your private key, you lose access to that wallet
    provider... instead, you just go to our web app, you log in, you do your 2FA,
    you coordinate the people online, sign your quorum, press the red button, and
    all the funds get swept across.
  topic: adoption
- impact_reason: This describes a significant improvement in emergency key management
    and fund recovery, moving from slow, physical key reconstitution to a fast, digital,
    multi-signature/quorum-based 'red button' sweep.
  relevance_score: 9
  source: llm_enhanced
  text: Well, rather than having to go through that key reconstitution process we
    talked about, where either you've kept the private keys in these different vaults
    in different locations and you have to bring multiple people together to reconstitute
    and perform the actions we talked about, instead, you just go to our web app,
    you log in, you do your 2FA, you coordinate the people online, sign your quorum,
    press the red button, and all the funds get swept across.
  topic: technology/strategy
- impact_reason: Highlights the speed and operational continuity enabled by their
    system during a security incident, minimizing downtime and asset exposure.
  relevance_score: 9
  source: llm_enhanced
  text: So, it just gives you within minutes the ability to just press the red button
    and move all the funds to your different wallet infrastructure, and then immediately
    resume operations again.
  topic: strategy/business
- impact_reason: Suggests a path for institutional-grade security integration *within*
    exchanges to protect their hot/cold storage infrastructure, even if retail users
    don't see direct benefit.
  relevance_score: 9
  source: llm_enhanced
  text: We can actually work with the exchanges behind the scenes to enable this because,
    ultimately, it's an IOU to you, but it's their money now. We can say, "If this
    wallet goes down, move it all across to here," or "Someone's trying to steal this
    fund from your wallet, move it across to here."
  topic: strategy/business
- impact_reason: 'Identifies the ultimate failure point for standard security: key
    compromise (blasting the keys), which their system is designed to mitigate.'
  relevance_score: 9
  source: llm_enhanced
  text: But in certain cases, it's just not going to help no matter what you do, which
    is if you blast the keys.
  topic: technology
- impact_reason: A strong summary statement positioning the product as comprehensive
    risk mitigation that prevents fund loss.
  relevance_score: 9
  source: llm_enhanced
  text: So, what we do is this last line of defense, which picks up where these wallets
    set off, and it complements and brings it all together and says, "We can protect
    against a lot more risks and ideally permit any funds disappearing."
  topic: strategy
- impact_reason: Emphasizes the non-custodial, trust-minimized nature of the solution,
    which is crucial for crypto adoption.
  relevance_score: 8
  source: llm_enhanced
  text: Our trust is never going to move it anywhere else.
  topic: strategy/security
- impact_reason: Uses the FTX collapse as a direct, relatable example of operational
    failure leading to customer panic and loss of trust.
  relevance_score: 8
  source: llm_enhanced
  text: If you're an exchange, your customers are saying, 'Hey, where's our funds?
    We can't withdraw. What are we going to do? Is this FTX again?'
  topic: adoption/risk
- impact_reason: Differentiates between manual (Recovery/Red Button) and automated
    (Response) action, addressing the speed required in modern hacks.
  relevance_score: 8
  source: llm_enhanced
  text: The second product is the response, which is, how can you do this automatically?
    But if you're not there in time to press the red button, what if you need to be
    able to automatically move it out without having to worry about anyone else doing
    it?
  topic: technology/security
- impact_reason: Excellent analogy clarifying the difference between alerting systems
    (fire alarm) and active mitigation systems (sprinklers).
  relevance_score: 8
  source: llm_enhanced
  text: Circuit is on this, and it's like sprinklers. Instead of just saying, 'Hey,
    there's a fire,' it's like, we take an action on the back of it. We stop the bad
    thing from happening.
  topic: strategy/technology
- impact_reason: Critiques the current industry standard (key security) as the single
    point of failure.
  relevance_score: 8
  source: llm_enhanced
  text: Ultimately, all of crypto security is right now mostly predicated on the fact
    that we keep your private key secure.
  topic: security
- impact_reason: Simplifies the concept of the pre-signed transaction into a clear,
    actionable instruction set.
  relevance_score: 8
  source: llm_enhanced
  text: So, you could say, 'Hey, I have the ability to move funds from wallet address
    A to wallet address B without having to sign again.'
  topic: technology
- impact_reason: 'Highlights the key benefit: executing pre-authorized transfers without
    requiring a fresh signature, crucial for automated disaster recovery.'
  relevance_score: 8
  source: llm_enhanced
  text: So, you could say, "Hey, I have the ability to move funds from wallet address
    A to wallet address B without having to sign again."
  topic: technology
- impact_reason: 'A concise description of the solution''s function: establishing
    a pre-approved escape route for assets.'
  relevance_score: 8
  source: llm_enhanced
  text: It just sets up the exit path and then triggers it to move the funds to safety.
  topic: strategy
- impact_reason: Uses a major, real-world hack ($1.4B loss) as a cautionary tale about
    signing malicious transactions via compromised interfaces.
  relevance_score: 8
  source: llm_enhanced
  text: With BitBay, what happened with BitBay is basically they—there was a front-end
    compromise... That transaction handed over control of the wallets with $1.4 billion
    to North Korea.
  topic: adoption
- impact_reason: 'Explains the technical hurdle: simple pre-signing fails because
    blockchain state (like balance) is dynamic, necessitating continuous updates.'
  relevance_score: 8
  source: llm_enhanced
  text: Every single time you take an action or move or change your balance, the pre-signed
    transaction is no longer going to be valid because the account balance is going
    to be different again.
  topic: technology
- impact_reason: Explains the technical hurdle for decentralized security solutions
    when dealing with centralized custodians utilizing omnibus structures—the lack
    of clear, segregated on-chain ownership.
  relevance_score: 8
  source: llm_enhanced
  text: Which then makes it very difficult for us because, ultimately, we can't figure
    out which is your business in this fast pool of other people's money, which means
    we can't attach to it.
  topic: technology/defi
- impact_reason: Clarifies that for exchanges, the solution must be adopted at the
    custodian level, potentially forcing a shift away from the risky omnibus model
    for clients who opt-in for segregated wallets.
  relevance_score: 8
  source: llm_enhanced
  text: It would work for the exchange basically doing this internally... In that
    example, you'd have to get FTX to sign up to your software. They would need to
    do it internally, unless they were to say, "We're not going to use this on-new
    bus model."
  topic: adoption/business
- impact_reason: 'Defines the current target market: large institutions demanding
    segregated, verifiable wallets, rather than retail users on centralized platforms.'
  relevance_score: 8
  source: llm_enhanced
  text: If you're not going to happen for a retail user, if you're a big hedge fund
    or a big person who they will say, "Here's your segregated wallet so you can always
    check it," then we could enable that.
  topic: adoption/investment
- impact_reason: Emphasizes the philosophy that their solution is additive security,
    designed to work alongside existing measures like MPC wallets, rather than attempting
    to replace established infrastructure.
  relevance_score: 8
  source: llm_enhanced
  text: It's not their place. I think I read it out earlier. Yeah, it's the complement.
    So, yeah, as mentioned, it's basically meant not to replace, but to exist in parallel
    and be added to it.
  topic: strategy
- impact_reason: Positions their solution as the necessary backup for when standard
    security protocols fail, which is critical for high-value operations.
  relevance_score: 8
  source: llm_enhanced
  text: Basically protecting all of your funds already. So, what we enable is basically,
    in the events where this doesn't work. For most of the cases, this actually works
    really, really well, and it's the reason that some of these companies are finally
    successful because, ultimately, everybody needs some form of security around their
    wallet.
  topic: strategy
- impact_reason: Reveals an early, perhaps experimental, application of their technology
    in recovering funds for retail users who have lost access to their seed phrases
    (a common crypto pain point).
  relevance_score: 8
  source: llm_enhanced
  text: One of the things that we like is we enable this for some Ledger devices.
    And so, we started basically giving out seed phrases on Reddit and saying, "Hey,
    like, you know, like can someone help us? We've lost access to our funds. Can
    someone help us with this?"
  topic: technology/adoption
- impact_reason: Addresses institutional resistance to change by promising integration
    and enhancement rather than disruptive overhaul.
  relevance_score: 7
  source: llm_enhanced
  text: We say, 'Okay, we'll meet you where you're at, and we can greater than or
    equal to make your security better. We don't want to diminish it in any way, but
    we can actually improve it.'
  topic: business/strategy
- impact_reason: Indicates flexibility in triggering the pre-signed action—it can
    be automated for speed or manually initiated.
  relevance_score: 7
  source: llm_enhanced
  text: So, you can say, "Okay, take action A first." And that can happen automatically,
    or happen under your system, or happen manually, should you wish?
  topic: technology
- impact_reason: Grounds the discussion in established cybersecurity standards (NIST
    CSF), lending credibility to the critique of traditional recovery methods.
  relevance_score: 7
  source: llm_enhanced
  text: 'The paper—your white paper—talks about the limits of key-based recovery,
    which you''ve spoken a bit about. As recommended by—and you put this in, I quite
    liked it—the National Institute of Standards and Technology, they define the key-based
    recovery system as: one, identify; two, protect; three, detect; four, respond;
    and five, recover.'
  topic: regulation
- impact_reason: Provides a concrete metric (15-second monitoring cycle) for how quickly
    the system can react to state changes or initiate recovery.
  relevance_score: 7
  source: llm_enhanced
  text: Every 15 seconds or so, we'll check with your wallet balances, and if we see
    a change to your wallet balance, we'll create a pre-signed instruction to sweep
    all the funds across.
  topic: technology
- impact_reason: A direct statement confirming the current B2B/Institutional focus
    of their advanced security product.
  relevance_score: 7
  source: llm_enhanced
  text: Yes, exactly. We don't worry about the retail users at the moment.
  topic: business
- impact_reason: Provides a concise summary of standard, high-end institutional crypto
    security practices (MPC, policies, role-based auth).
  relevance_score: 7
  source: llm_enhanced
  text: So, we talked about existing security like an MPC-based wallet, where they
    will have multiple layers of security. They'll have transaction policies. They'll
    have flight lists. They'll have quorums of people who need to come together, role-based
    authorization.
  topic: technology
- impact_reason: A philosophical reflection on the complexity and seemingly 'magical'
    nature of advanced cryptography and blockchain security for the uninitiated.
  relevance_score: 6
  source: llm_enhanced
  text: I keep saying magic, but it is really... You said it twice now. I like it.
    I think people... I don't know for the questions when you say... People don't
    realize how magical a lot of this stuff is when they get into it.
  topic: technology
- impact_reason: A slight contradiction or clarification that while their focus is
    institutional, they have *some* retail application, though details are confidential.
  relevance_score: 6
  source: llm_enhanced
  text: Some of the things that we talk about is we've enabled this for some retail
    wallets, so we don't talk about our customer cases.
  topic: adoption
source: Unknown Source
summary: '## Podcast Episode Summary: S2E11 Harry Donnelly, Circuit


  This episode of the "in-early" podcast features an interview with **Harry Donnelly,
  founder of Circuit**, focusing on his platform designed to mitigate catastrophic
  operational losses in the digital asset space through **Automatic Asset Extraction
  (AAE)**. The discussion centers on solving the critical security gap where the loss,
  compromise, or failure of private keys or custodians renders institutional crypto
  assets irrecoverable.


  ---


  ### 1. Focus Area

  The primary focus is **Crypto/Web3 Security and Operational Resilience**. The discussion
  centers on blockchain security mechanisms, specifically addressing failures in **key
  management (private keys, MPC, multi-sig)** and **custody infrastructure**, and
  introducing a novel, transaction-layer failsafe mechanism.


  ### 2. Key Technical Insights

  *   **Automatic Asset Extraction (AAE):** Circuit’s core innovation involves separating
  the signing and broadcasting of blockchain transactions. They pre-generate, authorize,
  and store **dormant, pre-signed transactions** that can be broadcast later, allowing
  assets to be moved to safety without needing current access to compromised or inaccessible
  primary keys.

  *   **Dynamic Pre-Signing:** The AAE infrastructure constantly monitors wallet balances
  (e.g., every 15 seconds) and automatically creates *new* pre-signed sweep transactions
  to account for any on-chain activity, ensuring the stored instructions remain valid
  for recovery.

  *   **Transaction-Layer Failsafe:** AAE operates independently of the primary key
  infrastructure (custodians, MPC setups), serving as a last line of defense that
  sits "underneath" existing security layers.


  ### 3. Market/Investment Angle

  *   **Mitigating Catastrophic Loss:** Circuit directly addresses the billions lost
  annually due to operational failures, offering institutions a way to prevent downtime
  and reputational damage (e.g., citing the Prime Trust failure where funds were trapped).

  *   **Agnostic Integration:** The platform is designed to integrate with existing
  infrastructure (like Fireblocks or other custodians) rather than requiring a complete
  overhaul, reducing adoption friction for institutions using multiple wallet providers.

  *   **Risk Aggregation Reduction:** By enabling funds to be moved between different
  wallet providers upon failure of one, Circuit removes aggregation and concentration
  risk across an institution''s custody setup.


  ### 4. Notable Companies/People

  *   **Harry Donnelly (Circuit Founder):** Creator of the AAE concept and Circuit
  platform.

  *   **Lauren Stevens (Host):** Lawyer specializing in blockchain, digital assets,
  and technology disputes.

  *   **Fireblocks:** Mentioned as an example of a wallet provider whose failure could
  halt all customer operations.

  *   **NIST CSF (National Institute of Standards and Technology Cybersecurity Framework):**
  Referenced as a traditional cybersecurity framework that Circuit applies to the
  crypto recovery process.

  *   **BitBay:** Used as a brief, contrasting example of a hack (front-end compromise
  leading to control signing) versus the key loss/custody failure scenario Circuit
  addresses.


  ### 5. Regulatory/Policy Discussion

  The discussion touched upon the **NIST CSF** framework (Identify, Protect, Detect,
  Respond, Recover) and how Circuit’s solution maps onto, and improves upon, the traditional
  "key-based recovery" model that NIST principles often imply in cybersecurity contexts.


  ### 6. Future Implications

  Circuit suggests a future where operational security in crypto moves beyond sole
  reliance on key security. The industry is trending toward **transaction-layer contingency
  planning** that allows for automated, rapid response to failures, ensuring business
  continuity even when primary access methods are compromised or unavailable.


  ### 7. Target Audience

  This conversation is highly valuable for **Crypto/Web3 Security Professionals, Institutional
  Operations Teams, Custodians, Digital Asset Hedge Funds, and Legal/Compliance professionals**
  dealing with digital asset risk management.


  ---


  ### Comprehensive Summary


  The podcast episode details the critical need for preventative security measures
  against catastrophic operational failures in the digital asset industry, as articulated
  by Harry Donnelly, founder of Circuit. Donnelly argues that while current security
  relies heavily on keeping private keys safe (via multi-sig or MPC), the failure
  of these systems—either through key loss or custodian collapse—leaves assets irrecoverable,
  costing the industry billions annually.


  Circuit’s solution is **Automatic Asset Extraction (AAE)**, a proprietary technology
  functioning as a transaction-layer failsafe. AAE works by separating the signing
  of a transaction from its broadcast. Circuit monitors client wallets and continuously
  generates and stores **pre-signed, dormant transactions** designed to sweep all
  assets to a designated safe vault. This process is dynamic, as new sweep instructions
  are created every few seconds to account for ongoing on-chain activity.


  Donnelly contrasts AAE with traditional **key-based recovery**, which, as outlined
  by the NIST framework, is a laborious, manual process involving decrypting recovery
  packages, reconstituting raw private keys, deriving all associated wallets, and
  manually transacting funds out. This traditional method introduces massive time
  delays (potentially hours) and creates a dangerous, temporary **single point of
  failure** (the raw private key) precisely when the business is under duress.


  Circuit’s platform offers two primary products: **Recovery** (a manual "big red
  button" to initiate the pre-signed sweep upon disaster) and **Response** (automatic
  execution of the sweep based on pre-set internal triggers or external signals, essential
  for responding to hacks that occur too quickly for human coordination). The system
  is agnostic, connecting various custodians to ensure funds can always exit a failing
  infrastructure to a functioning one, thereby eliminating aggregation risk. The core
  value proposition is shifting the response from a slow, high-risk reconstitution
  process to an immediate, pre-authorized asset migration.'
tags:
- artificial-intelligence
- startup
title: S2E11 Harry Donnelly, Circuit
topics:
- keywords:
  - ai
  - machine learning
  - deep learning
  - neural networks
  - llm
  - large language model
  mentions: 59
  prominence: 1.0
  topic: artificial intelligence
- keywords:
  - startup
  - entrepreneur
  - founder
  - venture
  mentions: 1
  prominence: 0.1
  topic: startup
---

<!-- Episode automatically generated from analysis data -->
<!-- Processing completed: 2025-10-16 04:44:27 UTC -->
