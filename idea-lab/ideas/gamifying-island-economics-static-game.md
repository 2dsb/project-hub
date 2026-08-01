---
id: "idea-20260411-a3f7c2"
summary: "The game distills island economics into a two-person simulation driven by Action Points that regenerate and convert to Labor, which combined with Capital like a fishing net yields Savings. Savings deplete via Consumption and can be riskily invested to create new Capital. Agents can gift, borrow, lend, or invest via Contracts, and accidents destroy Capital and Savings. Founding a partnership pools resources into a corporation with shared employees. A global economy variable tracks total daily Savings, linking productivity to Capital stock."
title: "Gamifying Island Economics (Static Game)"
tags: ["island-economics", "gamification", "action-points", "capital", "savings", "lending", "investment", "partnership", "game-design", "economic-simulation", "game-mechanics"]
importance: 1
connections: []
---
Let's design a game that tells the story of everything in island economics.

This game has only two elements: two people, A and B, and a timeline.

If you open A's user interface, you'll find:

```

user:A
Action Points: 10
Labor: Fishing (5)
Savings: 20
Capital: one fishing net
Consumption: 5
```

As time passes, action points continuously increase.

```
Action Points: 10 → 20
```

Action points can be converted into labor.

```
Action Points: 20 → 10
Labor: Fishing (5 → 15)
```

Capital applied to labor can convert labor into savings at a certain ratio.

```
Labor: Fishing (15 → 5)
Capital: fishing net
Savings: 20 → 30

Labor: Fishing (15 → 5)
Capital: none
Savings: 20 → 22
```

Savings and action points, with a certain amount of risk, can be converted into capital.

```
Savings: 20 → 0
Action Points: 10 → 0
Capital: none → one fishing net
Success probability: 20%
```

Over time, savings decrease due to consumption.

```
One day passes
Consumption: 5
Savings: 20 → (20 - 5 = 15)
```

Action: giving savings to someone (A gives to B)

```
user:A
Savings: 20 → 15

user:B
Savings: 5 → 10
```

Action: giving capital to someone (A gives to B)

```
user:A
Capital: one fishing net → none

user:B
Capital: none → one fishing net
```

Contract (logical binding of two actions) (Action 1, Condition, Action 2)

Borrowing/Lending (can be divided into business loans, consumer loans, and emergency loans)

```
A and B agree:

Time point 1:
A gives B 10 units of savings

Time point 2:
B gives A 15 units of savings
```

Investment:

```
A and B agree:

Time point 1,
A gives B 10 units of savings

If B creates capital before time point 2: a fishing net,
at time point 2,
B gives A 20 units of savings
```

Event: accident, causing reduction of capital and savings

```
Accident: natural disaster
Capital: one fishing net → none
Savings: 15 → 0
```

Action: founding a partnership

```
A and B invest savings and capital to found partnership C

user:A,B
Savings: -5
Capital: -one fishing net

(new) corporation:C
Savings: +10
Capital: 2 fishing nets
Employees: A, B
```

As the entire game evolves over time, there is a global variable: the economy

```
Within 1 day
user:A,B
Savings: +10 each

Daily economy: 10 + 10 = 20
```

Therefore, the economy is related to total capital.
