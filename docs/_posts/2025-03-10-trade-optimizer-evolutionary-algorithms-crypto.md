---
layout: post
title: "TradeOptimizer: Using Evolutionary Algorithms to Trade Crypto"
permalink: /trade-optimizer/
date: 2025-03-10 10:00:00 -0300
categories: ["projects", "algorithms"]
tags: ["rust", "brkga", "algorithmic-trading", "crypto", "metaheuristics"]
---

When I started working on my graduation thesis at [UFF](https://www.uff.br/) (Universidade Federal Fluminense), I wanted to pick something that combined two things I was genuinely curious about: algorithmic trading and metaheuristic optimization. The crypto market seemed like the perfect playground -- it runs 24/7, has publicly available historical data, and the futures market lets you go both long and short. So I built [TradeOptimizer](https://github.com/victorl2/trade-optimizer), a system that uses an evolutionary algorithm called BRKGA to find optimal parameters for a trading model operating on cryptocurrency futures.

A paper that was a big inspiration for this work was Caranha and Iba's ["Optimization of the trading rule in foreign exchange using genetic algorithm"](http://www.iba.t.u-tokyo.ac.jp/papers/2009/caranha1GECCO2009.pdf), which applied genetic algorithms to optimize trading rules in forex markets. I wanted to take a similar idea and apply it to the crypto futures market using a different evolutionary approach.

The full paper is available (in Portuguese): [TradeOptimizer: Operando no mercado de criptoativos com BRKGA (PDF)](https://app.uff.br/riuff/bitstream/handle/1/25787/VICTOR%20FERREIRA%20TEIXEIRA%20TradeOptimizer__Operando_no_mercado_de_criptoativos_com_BRKGA.pdf?sequence=1&isAllowed=y).

## The idea

The core question was simple: can we describe a trading strategy as a set of numerical parameters and then use an optimization algorithm to find the best combination of those parameters? Instead of manually tweaking indicator thresholds and hoping for the best, I wanted the algorithm to explore that space systematically.

The trading model uses well-known technical indicators -- [RSI](https://www.investopedia.com/terms/r/rsi.asp), [MACD](https://www.investopedia.com/terms/m/macd.asp), [EMA](https://www.investopedia.com/terms/e/ema.asp), SMA, and [ATR](https://www.investopedia.com/terms/a/atr.asp) -- to decide when to open long or short positions. Each indicator has configurable parameters (periods, thresholds, bounds), and the combination of all these parameters forms what BRKGA calls a "chromosome" -- a vector of 36 floating-point values between 0 and 1 that fully describes a trading strategy.

## What is BRKGA

[BRKGA](https://en.wikipedia.org/wiki/Biased_random-key_genetic_algorithm) stands for Biased Random-Key Genetic Algorithm. It's an evolutionary metaheuristic, which means it works by evolving a population of candidate solutions over many generations, loosely inspired by natural selection.

Here's how it works in practice: you start with a large population of random individuals (in my case, 10,000 random trading strategies). Each one gets evaluated by running a backtest against historical price data, and the result -- the total profit or loss -- becomes its fitness score. Then the algorithm selects the top performers (the "elite"), generates some completely random newcomers ("mutants"), and creates the rest of the next generation by combining genes from elite and non-elite parents, with a bias toward picking genes from the elite parent. Repeat this for many generations, and the population gradually converges toward better solutions.

The beauty of BRKGA is that the chromosomes are always just vectors of random keys between 0 and 1. A decoder function maps these values into actual strategy parameters -- indicator periods, RSI bounds, leverage, take-profit multiples, and so on. This clean separation between the algorithm and the problem domain makes it very flexible. You can swap in a completely different trading model without touching the optimization code.

## Overfitting: the real enemy

If there's one thing I learned from this project, it's that overfitting is the most dangerous trap in algorithmic trading. It's absurdly easy to find a strategy that performs incredibly well on historical data and then completely falls apart on new data. The algorithm is powerful enough to find patterns in noise if you let it.

To fight this, I split the historical data into alternating training and validation segments. The dataset gets divided into 12 chunks, and the algorithm only sees the even-numbered chunks during optimization. The odd-numbered chunks are held back for validation. This interleaving approach is important -- if you just split the data in half chronologically, you might end up training on a bull market and validating on a bear market (or vice versa), which tells you nothing useful about generalization.

Even with this setup, overfitting remained a constant concern. A strategy that looked promising on training data would often show mediocre results on validation. The market is genuinely hard to predict, and any system that claims otherwise probably hasn't been tested properly.

## My first real Rust project

TradeOptimizer was my first serious project in [Rust](https://www.rust-lang.org/), and I chose it deliberately. The optimizer needs to evaluate thousands of trading strategies per generation, each running a full backtest across months of minute-by-minute candle data. Performance matters a lot here, and Rust delivered.

The backtesting engine processes candlestick data, computes all the technical indicators, simulates trade execution with slippage and fees, and tracks profit/loss -- all of it running across multiple threads using [Rayon](https://github.com/rayon-rs/rayon) for parallel fitness evaluation. Going from a single-threaded version to parallel evaluation with Rayon was surprisingly easy -- practically just swapping `.iter()` for `.par_iter()` in the fitness evaluation loop.

That said, fighting the borrow checker as a Rust beginner was a real experience. I spent more time than I'd like to admit restructuring code to satisfy lifetime requirements, especially around the backtest engine that gets shared across threads. But it forced me to think carefully about data ownership, and the resulting code is genuinely safe from data races without any runtime overhead.

Reflecting on it now, Rust was way more challenging than C++ would have been for this kind of project. The learning curve was steeper than I initially thought. In C++ I could have gotten the same performance with less friction -- raw pointers, manual memory management, and all the foot-guns included, sure, but for a solo graduation project where correctness guarantees weren't the priority, it would have been the more pragmatic choice. Still, I'm glad I went with Rust. The struggle taught me a lot about systems programming concepts that I wouldn't have internalized otherwise.

## Looking back

This project taught me a few things worth sharing. First, metaheuristics like BRKGA are remarkably effective at exploring large parameter spaces -- way better than grid search or manual tuning. Second, the hard part of algorithmic trading isn't finding a strategy that works on past data; it's building one that generalizes. And third, Rust is an excellent choice for compute-heavy work like backtesting, even if the learning curve is steeper than what you'd get with Python.

The [code is open source](https://github.com/victorl2/trade-optimizer) if you want to take a look or experiment with it yourself.
