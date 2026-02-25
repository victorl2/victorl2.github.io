---
layout: post
title: "What 30 Interviews Taught Me About the State of Senior Java Developers"
permalink: /30-interviews-senior-java/
date: 2025-11-01 10:00:00 -0300
categories: ["career", "software-engineering"]
tags: ["interviews", "java", "fundamentals", "hiring"]
---

Over the past few months, I conducted 30 technical screening interviews for a Senior Java Developer position. The candidates came from all over: Canada, the US, Mexico, Brazil, and several countries across Europe. The role was not exotic. It required solid Java fundamentals, reasonable concurrency knowledge, and the ability to reason about everyday backend problems. Standard expectations for someone with "senior" in their title.

I used the same set of 10 questions for every candidate. These were not algorithmic puzzles or whiteboard brain teasers. No one was asked to invert a binary tree or implement Dijkstra's algorithm. Every question was a foundational probe: a real scenario you would encounter in production backend work, designed to reveal whether the candidate actually understands the tools and patterns they claim to use daily. Spring dependency injection, thread safety, Kafka delivery guarantees, basic SQL. The kind of knowledge that should be second nature after a few years of building Java services.

Out of those 30 candidates, four passed.

That number kept nagging at me. Not because the bar was unusually high, but because the questions were genuinely straightforward. And yet, candidate after candidate stumbled on the basics. Worth noting: the hiring process had three stages. An initial HR screening, then my technical round, then a final interview with my boss. So these 30 candidates had already been filtered once before reaching me. The ones who passed my round still had to face my boss, who was considerably more strict with the depth of knowledge he expected. My round was supposed to be the easy one.

## What the questions looked like

Before starting with any questions, I made sure to set expectations clearly. I told every candidate that precise syntax, exact method names, and getting every detail right did not matter. If they could broadly indicate what they wanted to do with reasonable pseudo-code, that would be more than enough. We used [Rustpad](https://rustpad.io/) as a shared scratchpad so they could type out their thinking in real time, iterate freely, and treat it as a conversation rather than an exam. The goal was never to catch anyone on a technicality. It was to understand how they think about problems.

To give you a sense of the level, here are a few representative examples from my screening.

One question presented three implementations of the same interface and asked how you would inject a specific one:

```java
public interface NotificationService {
    void send(String userId, String message);
}

@Service
public class EmailNotificationService implements NotificationService { }

@Service
public class SmsNotificationService implements NotificationService { }

@Service
public class PushNotificationService implements NotificationService { }
```

This is core Spring. You can use `@Qualifier`, `@Primary`, or inject a `List<NotificationService>` and select by type. It is one of the first things you learn when working with dependency injection, and it comes up constantly in real codebases. Several candidates with years of Spring experience could not articulate any of these options clearly.

A different concurrency question described an IO bound operation that needed to run in parallel. Given a list of values and a heavy processing function:

```java

Result processValue(InputValue value); // IO-bound, slow operation

public List<Result> doWork(List<InputValue> values){
    //TODO: complete the function
}
```

The task: process all values concurrently and return the results in the same order as the input, without sorting afterward. We explicitly stated the function was IO bound, not CPU bound, which is why running everything at once makes sense here. The clean solution looks something like this:

```java
public List<Result> doWork(List<InputValue> values){
    List<CompletableFuture<Result>> futures = values.stream()
        .map(v -> CompletableFuture.supplyAsync(() -> processValue(v), executor))
        .toList();

    List<Result> results = futures.stream()
        .map(CompletableFuture::join)
        .toList();
    
    return results;
}
```

The key insight is twofold. First, you fire off all the futures before waiting on any of them, so the IO operations run concurrently. Second, because you collect the futures in a list that mirrors the input order, calling `join()` sequentially on that list naturally preserves the ordering with no sorting required. The candidate needed to demonstrate awareness of [CompletableFuture](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/CompletableFuture.html), thread pools via an `ExecutorService`, and the fundamental idea that futures represent handles to work that is already in progress. Candidates who listed "multithreading" as a skill on their resume often could not sketch even a basic approach using these standard tools.

Another concurrency question dealt with a common scenario: your application has a cache refresh that takes 30 seconds, and multiple threads might trigger it simultaneously. How do you ensure only one thread refreshes while others either wait or skip? The answer space includes `ReentrantLock`, `Semaphore`, double checked locking, or even a simple `AtomicBoolean` flag depending on the desired behavior. The point was not to recite the perfect solution but to demonstrate awareness of [Java's concurrency primitives](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html) and reason about thread coordination. Most candidates defaulted to vague answers about "using synchronized" without being able to explain the tradeoffs or explore alternatives.

A Kafka question described a consumer that reads an event, inserts a row in Postgres, then crashes before committing the offset. On restart, what happens? The insert has a unique constraint on `event_id`. Is that enough? This probes understanding of at least once delivery, [idempotent consumers](https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/), and what happens when you combine message brokers with database writes. Candidates who had "Kafka" on their resume often could not explain the redelivery behavior or reason through why a unique constraint alone might not be sufficient in more complex processing pipelines.

The SQL question presented a simple orders table and asked: find customers who placed orders in January but not in February. A straightforward `NOT EXISTS` subquery. No joins across five tables, no window functions, no recursive CTEs. Basic relational reasoning. This tripped up more candidates than I expected.

## The pattern

What struck me was not that candidates got individual questions wrong. Everyone has blind spots. The pattern was that the gaps were consistently in foundational areas. Not framework trivia, not obscure API details, but the core mechanics of the platform these developers claimed years of experience in.

To put it concretely: on the cache refresh question, several candidates could not even articulate that a mutex or an atomic variable would be involved in synchronizing access across threads. Not the Java specific classes, not the exact API. The concept itself. These were candidates with more than five years of professional experience on their resumes. Some of them were not primarily Java developers, and that was fine. I was not expecting anyone to recite the `java.util.concurrent` package from memory. But the idea that concurrent access to a shared resource requires some form of synchronization primitive is not a Java concept. It is a computer science concept. It is the kind of thing you learn once and carry with you regardless of the language or framework. When someone with half a decade of experience cannot reach for that idea even in pseudo-code, something fundamental was missed along the way.

Many candidates could talk fluently about microservice patterns, Kubernetes deployments, and cloud architectures. They could describe systems they had worked on at a high level. But when the conversation shifted to how things actually work underneath, the confidence evaporated. It was as if the abstractions had become the entire mental model, with nothing solid beneath them.

A fair question is why I chose these specific questions in the first place. The answer is simple: they were modeled after the questions my own boss used when he hired me years ago. They reflect what is actually required in the existing codebase we work on every day. The system is Java heavy and uses all the concepts covered in the screening: concurrency, message processing, dependency injection, relational queries. These were not theoretical exercises chosen to make candidates feel small. They were a direct reflection of the work the person would be doing on day one.

This compounds over time. If you spend years building Spring Boot services without understanding how thread safety works, what Kafka actually guarantees about message delivery, or how basic SQL subqueries function, you end up with a fragile kind of seniority. You can be productive within a narrow band of familiar patterns, but the moment something unexpected happens, a concurrency bug in production, a message processing anomaly, a query that returns wrong results, you lack the vocabulary to even describe the problem, let alone fix it.

## What this means if you are preparing for interviews

If you are a developer targeting senior level roles, the single most impactful thing you can do is go back to fundamentals. Not LeetCode grinding, not memorizing design pattern names, but genuinely understanding the platform you work on.

For Java specifically, that means being comfortable with the [concurrency utilities](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html), understanding Spring's dependency injection beyond just slapping `@Autowired` on everything, knowing how your message broker handles failures and redelivery, and being able to write SQL that goes beyond simple SELECT statements. Read [Effective Java](https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/) by Joshua Bloch if you haven't. Understand [Kafka's delivery semantics](https://kafka.apache.org/documentation/#semantics) if you list it on your resume.

The broader principle applies regardless of your stack. Frameworks come and go. The fundamentals of how your runtime works, how concurrency behaves, how your data layer operates, those stay relevant for your entire career.

## What this means if you run interviews

The biggest lesson here is that practical, role-specific questions reveal what algorithmic interviews cannot. A candidate can pass a LeetCode medium and still have no idea how to coordinate threads, handle message redelivery, or wire up dependency injection in the framework your team actually uses. Those are not theoretical gaps. They are gaps that will show up on the first week of real work.

If you are hiring a Senior Java Developer to work on a concurrent, Kafka-driven system, your interview should reflect that. If you are hiring a Senior Rust Developer, you would expect them to know their way around [Tokio](https://tokio.rs/) and async runtimes. If it is a Senior Go position, they should be able to reason about goroutines and channels without hesitation. The point is not to quiz people on trivia. It is to verify that the person you are about to embed in your team can actually operate in the environment they are being hired for. Tailoring your questions to your actual stack and codebase is a far better signal than any generic coding challenge.

## The uncomfortable truth

A 13% pass rate on foundational questions for a senior role is not normal. Something is off in how developers are building and maintaining their skills. Whether it is overreliance on frameworks that hide complexity, a culture that rewards shipping speed over understanding, or simply a job market where the "senior" title inflated faster than the expectations behind it, the result is the same: a significant number of experienced developers cannot explain the basics of the tools they use every day.

This is not a call to gatekeep or to make interviews harder for the sake of it. It is an observation that the gap between what "senior" implies and what many candidates actually know has widened.

At the end of the day, this is about computer science fundamentals more than anything else. The busy reality of day to day work, the layers of abstractions, the pressure to ship using whatever patterns already exist in the codebase, all of it quietly dissuades you from true learning. You solve today's ticket with today's tools and move on. Months pass, then years, and the foundational knowledge you assumed you had never actually solidified.

My recommendation is to make a real, deliberate effort on two fronts. First, ground yourself in fundamental CS knowledge: how operating systems manage processes and memory, how concurrency actually works at the hardware and OS level, how networks deliver data, how databases execute queries. This is the layer beneath every framework and every language, and understanding it changes how you reason about every system you touch. Second, deepen your mastery in your language of choice. Not just knowing enough to get by, but understanding the runtime, the memory model, the standard library, and the idioms that separate competent code from fragile code. For Java specifically, I recommend [The Ultimate Java Mastery Series](https://codewithmosh.com/p/the-ultimate-java-mastery-series) by Mosh Hamedani (not sponsored, just genuinely exhaustive and complete material). It covers the language thoroughly and is structured well enough to fill gaps you might not even know you have.

Neither of these is something that happens passively. It requires a genuine love for the craft, a willingness to learn things on your own time not because a manager asked you to or because a deadline demands it, but because you actually care about being good at what you do. That is the difference between a developer who can only operate within familiar patterns and one who can reason through anything the job throws at them.
