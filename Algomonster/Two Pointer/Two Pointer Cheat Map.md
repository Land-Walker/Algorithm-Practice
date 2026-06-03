# Cheat Map (how to solve Qs easily)
## Invariant
One general idea that appears on all TP problems is:
> each correct solution maintains an invariant

### What is Invariant?
Invariant = a statement taht must stay true as loop runs
- This must be true again when the loop is ready for the next iteration as values, pointers, states are changing through iterations

The simpler and more useful mental model to consider during problem solving is:
> what must be true again once this iteration finishes?

### Why this matters?
- Dont have to memorize pointer modtion, instead just ask:
    > what must still be true after these pointers move?
  - less allured by messy changes inside of algorithms

### Common Invariant Shapes
When you face a new loop, ask which shape it resembles. That usually makes the invariant easier to state.

#### 1. Finished Region is Correct
Invariant = the finished region already contains the correct result so far

Update: extend that region by one safe step

Why it stays true: the new element is exactly the next one that belongs in the finished region

#### 2. Remaining Candidates Still Contain the Answer
Invariant = if the answer exists, it is still inside the current candidate range

Update: discard part of the range that cannot contain the answer

Why it stays true: the information you have right now justifies ruling that region out

#### 3. Active State is Valid
Invariant = the current live state satisfies the rule you need before using it

Update: change the state, then repair it if that rule breaks

Why it stays true: you only use the state after the repair step finishes

#### 4. Variables keep a Meaningful Relationship
Invariant = the variables still have the relationship that your reasoning depends on

Update: move them in a coordinated way

Why it stays true: each move preserves the same gap, speed ratio, or ordering