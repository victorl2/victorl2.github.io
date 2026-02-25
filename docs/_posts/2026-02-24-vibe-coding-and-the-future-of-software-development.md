---
layout: post
title: "Vibe Coding and the Need to Adapt"
permalink: /vibe-coding/
date: 2026-02-24 14:00:00 -0300
categories: ["career", "software-engineering"]
tags: ["vibe-coding", "ai", "developer-productivity", "career"]
---

The term "vibe coding" has been floating around developer circles for a while now. Coined by [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) in early 2025, it describes the practice of writing software almost entirely through natural language prompts to AI tools, where you "fully give in to the vibes" and let the LLM generate the code. You describe what you want, the AI produces it, you run it, and if something breaks, you paste the error back and ask it to fix it. The code itself becomes secondary to the intent.

It sounds radical if you frame it as a departure from "real programming." That framing misses the point entirely.

## What vibe coding actually is

Vibe coding is not a methodology or a framework. It is a way of working. You sit down with a tool like [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Cursor](https://www.cursor.com/), or [GitHub Copilot](https://github.com/features/copilot), and instead of writing every line yourself, you describe behavior at a higher level and let the model translate that into implementation. Sometimes you review the output carefully. Sometimes you don't. You just check if it works.

That last part is what makes people uncomfortable. The idea that a professional developer would ship code they didn't fully read or understand feels wrong. And in many contexts, it is wrong. You wouldn't vibe code a payment processing system or a security-critical authentication flow. But let me tell you a secret, not all production code is mission critical, and vibe coding works surprisingly well most of the time.

The important distinction is that vibe coding is not about abandoning understanding. It is about choosing where to invest your attention. A senior developer vibe coding a CRUD endpoint is making a conscious tradeoff. They know what the code should look like, they can spot when it is wrong, and they are saving time on the parts that are mechanical.

## The industry is already there

This is not a fringe experiment. The biggest companies in tech have embraced AI-assisted development at scale. [Satya Nadella revealed](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html) that 20% to 30% of Microsoft's code is now written by AI. [Google's Sundar Pichai](https://www.entrepreneur.com/business-news/ai-is-taking-over-coding-at-microsoft-google-and-meta/490896) put their number at over 30%. Mark Zuckerberg has predicted that within the next year, half of Meta's development will be done by AI.

[Uber](https://www.uber.com/blog/the-transformative-power-of-generative-ai/) has taken a particularly systematic approach. They built [uReview](https://www.uber.com/blog/ureview/), an AI-powered code review system that catches bugs, security vulnerabilities, and coding standard violations. Their Autocover tool generates test cases automatically and has saved an estimated [21,000 developer hours](https://medium.com/@_jaydeepkarale/how-uber-built-an-ai-agent-that-saved-21000-developer-hours-382c40776f3b) by increasing test coverage across their platform. They even ran a company-wide hackathon with over 700 engineers focused entirely on generative AI applications for developer productivity.

[Stripe](https://stripe.com/blog/how-we-built-stripe-minions) has gone even further with their internal "minions" system: over 1,300 pull requests merged per week that are entirely AI-produced with zero human-written code, only human review. This is not some low-stakes SaaS product. Stripe processed $1.9 trillion in total payment volume in 2025, roughly 1.6% of global GDP. Their codebase is mission-critical financial infrastructure, and they are still confident enough in AI-assisted development to ship it at this scale.

<div style="display: flex; justify-content: center;">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Over 1,300 Stripe pull requests merged each week are completely minion-produced, human-reviewed, but contain no human-written code (up from 1,000 last week).<br><br>How we built minions: <a href="https://t.co/GazfpFU6L4">https://t.co/GazfpFU6L4</a>. <a href="https://t.co/MJRBkxtfIw">pic.twitter.com/MJRBkxtfIw</a></p>&mdash; Stripe (@stripe) <a href="https://twitter.com/stripe/status/2024574740417970462?ref_src=twsrc%5Etfw">February 19, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

These are not startups experimenting with a trend. These are companies operating massive codebases with thousands of engineers, and they have decided that AI-assisted development is how software gets built now.

## Developers adapt. That's what we do.

Here is something I have noticed throughout my career: the tools and constraints around software development change constantly, and developers just... adapt.

Some companies require you to work exclusively from remote virtual environments. Others lock down your machine so tightly that installing a browser extension requires a ticket. I have worked in places where the entire development workflow ran inside a Citrix session, and places where you SSH into a cloud dev box because nothing runs locally. Different teams use different version control workflows, different CI systems, different deployment strategies. Some shops are all-in on pair programming. Others rely on asynchronous code review across time zones.

None of these constraints felt natural at first. Each one required adjustment, sometimes significant adjustment. But developers adapted because that is what the job demands. You learn the tools, you learn the constraints, you find ways to be productive within them.

Having worked at multiple Fortune 500 companies, I have seen firsthand how much of a developer's time is spent just navigating internal complexity. Big companies have in-house frameworks, proprietary deployment pipelines, internal libraries, and dozens of tools that only exist within that organization. Even with robust documentation, finding what you need when you are trying to understand yet another internal system out of the hundred you interact with is genuinely hard. Every new team, every new project brings a ramp-up period where you are reading wikis, Slack threads, and outdated READMEs trying to piece together how things work.

This is where AI-assisted development delivers some of its clearest value. A well-integrated AI with context over company-wide tools, codebases, and internal documentation can dramatically shorten that ramp-up. Instead of spending a day hunting down how the internal auth service works or which config flags a deployment tool expects, you ask the AI and get an answer grounded in the actual codebase. It is not replacing the developer's judgment. It is removing the friction that slows down experienced engineers in unfamiliar territory.

Vibe coding is the same kind of shift. It is a new way of interacting with the machine to produce software. The underlying skill, understanding what software should do, how systems fit together, how to debug when things go wrong, remains the same. The interface is changing.

## What actually changes

The developer role is not disappearing, but it is shifting in emphasis. When AI handles more of the translation from intent to code, the value moves upstream. Understanding the problem clearly, defining the right behavior, knowing what questions to ask, recognizing when the output is subtly wrong. These become the differentiators.

Debugging is a good example. When you vibe code something and it breaks, you still need to understand the error. You still need to reason about what the system is doing and why. The AI can help, but it can also confidently lead you in the wrong direction. The developer who understands the fundamentals will catch that. The one who doesn't will spend hours going in circles.

Architecture and system design become more valuable as well. AI is remarkably good at generating local solutions, a function here, a component there. It is much less reliable at making coherent decisions across an entire system. Knowing how to structure a codebase, manage dependencies, and make tradeoffs that hold up over time is still a fundamentally human skill.

## The Learning problem

There is one aspect of this shift that concerns me. For most senior developers, AI-assisted development is a positive multiplier. You already have the mental models, the debugging instincts, the understanding of why things break. You can evaluate what the AI gives you and course correct when it is wrong. But for junior engineers, it is a double edged sword.

You do not develop deep software development skills at the same pace when AI is writing most of your code. There is something irreplaceable about going from zero to one by yourself. Reading the docs, hitting a wall, stepping through the debugger, finally understanding why that null pointer keeps showing up. That struggle is where the real learning happens. When the AI just hands you the answer, you might ship faster, but you skip the part where the knowledge actually sticks.

This is not a solved problem. The industry is still figuring out how to onboard and grow junior developers in a world where the tools do so much of the heavy lifting. How do you build intuition about systems when you never had to wrestle with them from scratch? How do you learn to debug effectively when your first instinct is to paste the error into a prompt? These are open questions, and the answers will shape what the next generation of senior engineers looks like.

And this is not just a junior problem. Here is a question worth sitting with: will the skills of senior developers who rely exclusively on AI to write code eventually degrade? Yes. A resounding yes. Skill is not a permanent acquisition, it is a muscle. What you do not use, you lose. If every line of code you write for the next two years is AI generated while you just review and prompt, your ability to reason through complex systems from scratch will atrophy. It is not a matter of if, it is when. This is why running your own side projects the artisanal way, writing code by hand, solving problems without a copilot, matters more than ever. Not because AI tools are bad, but because you need to keep the underlying capability sharp. When the moment comes that demands true mission critical code, the kind where a subtle bug means real consequences, you need to be able to deliver. If you have spent years outsourcing that muscle to a machine, you will not have it when it counts.

## The pragmatic take

Vibe coding is not the future of all software development. It is one more tool in an expanding toolkit. Like every tool before it, it works well in some contexts and poorly in others. The developers who thrive will be the ones who understand when to use it and when not to, the same judgment call we make with every other technology.

Is software engineering over? No. But the pace companies demand has changed. Iteration cycles are shorter, expectations are higher, and there is simply not enough time to stop and fight with red tape every time you need to ship. The developers and teams that integrate AI effectively into their workflow are not cutting corners, they are removing the friction that used to slow everything down, so they can focus on the work that actually matters.

Take code review for example, it has never been the most glamorous part of the job, but it is more important than ever. When a growing percentage of code is AI generated, the reviewer is the last line of defense, catching subtle bugs, questioning architectural decisions, ensuring the output actually aligns with the intent. If anything, the bar for thoughtful code review has gone up, not down.

And this is no longer a matter of personal preference. Companies are starting to measure and expect AI usage as part of how developers work. [Shopify's CEO Tobi Lütke](https://www.businesstoday.in/technology/news/story/ai-use-is-no-longer-optional-at-shopify-declares-ceo-tobi-lutke-in-internal-memo-471211-2025-04-08) declared in an internal memo that "reflexive AI usage is now a baseline expectation," with AI competency becoming part of performance reviews and hiring decisions. [Coinbase's CEO Brian Armstrong](https://techcrunch.com/2025/08/22/coinbase-ceo-explains-why-he-fired-engineers-who-didnt-try-ai-immediately/) went further and fired engineers who refused to adopt AI tools after giving them a week to onboard. Companies are even tying [AI adoption metrics to executive compensation](https://www.equilar.com/blogs/620-ai-as-a-performance-metric.html). This is quickly becoming the reality of corporate software development "ways of work," not something up for discussion.

A side note on the layoffs: the massive waves of tech layoffs happening right now are not caused by AI replacing developers. These cuts stem from over-hiring during the pandemic boom, rising interest rates, and pressure from investors to improve margins. But AI makes for a convenient narrative. Saying "we are investing in AI efficiency" sounds a lot better in a press release than "we hired too many people and need to correct course." Keep that distinction clear. Conflating the two feeds unnecessary panic about the profession disappearing when the reality is far more mundane.

That said, we should not throw the baby out with the bathwater.

![Don't throw the baby out with the bathwater](/assets/imgs/throw-away-bath-water.jpg)

The fundamentals, understanding systems, writing clean interfaces, reasoning about failure modes, knowing how to debug, are what make AI-assisted development actually work. Without them, you are just generating code you cannot evaluate. The tooling is only as good as the person directing it.

The real question is not whether vibe coding is "legitimate" programming. It is whether you are willing to adapt, the way you always have. New tools, new constraints, new ways of working. The constant is not the tool. It is the developer's ability to learn, adjust, and keep building.
