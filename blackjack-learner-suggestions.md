# Blackjack Learner Suggestions

Based on `black_jack (1).py`. You already fixed the `main() -> True/False + break` bug. Nice work!

This roadmap is ordered easiest -> hardest.

## 1. Fix Your Scoring Bug — Biggest Win

Location: `player_point_count()` lines 40-80 and `computer_point_count()` lines 85-132.

Current pattern:

```python
if "8 of Spades" in player_hand or "8 of Clubs" in player_hand ...
  player_points += 8
```

`in` only asks "is at least one there?" Example failures:

- `["8 of Spades", "8 of Clubs"]` -> gives 8, should be 16
- `["Jack of Spades", "Queen of Hearts"]` -> gives 10, should be 20

Lesson: **loop over the list instead of checking each rank.**

```python
for card in player_hand:
  # get rank from card, add value
```

This deletes ~90 lines of repeated `if`s. This is DRY — Don't Repeat Yourself.

Ace challenge: Ace should be `11, but 1 if you'd bust`. Count Aces as 11, then subtract 10 while total `> 21`.

## 2. The Hidden Infinite Loop

Location: lines 94-96:

```python
while computer_points > 10:
  if "Ace..." in computer_hand:
    computer_points += 1
```

If computer has an Ace, `computer_points` starts at 11, so `> 10` is True, then you add 1 -> 12, still True... forever.

Lesson: `while` needs a way to become False. `if` is almost always what you want for scoring.

## 3. Stop Using `global`

You have `player_hand` defined at top-level *and* inside `play()`, but `player_points` as `global`. That shadowing is confusing.

Learner upgrade: pass data in, return data out:

```python
def hand_value(hand):
  points = 0
  # ... calculate ...
  return points
```

No `global` needed. Functions become testable:
`hand_value(["Ace of Spades", "9 of Hearts"])` should be 20.

## 4. Handle Bad Input

Location: line 144:

```python
hit_stand = input("Press 'H'...")
if hit_stand == "H": ...
if hit_stand == "S": ...
```

What if user types `h`, ` s`, or `x`? Both `if`s fail, you return `None`. Then `if keep_going == False:` is `None == False` -> False, so you loop again with no message.

Fix:

```python
hit_stand = input(...).strip().upper()
# + else: print("Please type H or S")
```

Lesson: never trust user input.

## 5. Give the Dealer a Brain

Right now computer gets 2 cards and never hits. Real dealer hits until 17.

Next feature after player stands/busts:

```python
while computer_value < 17:
  computer_hand.append(cards.pop())
```

This is why your `a/a1/a2/a3/b1/b2/b3` winner code at lines 164-211 almost always favors the player.

Also remove debug prints `a`, `a1`, `a2`, `a3`, `b1`, `b2`, `b3` when done.

## 6. Clean Up the Deck

- Line 6: `" 2 of Spades"` has a leading space — will never match `"2 of Spades"` checks.
- `random.shuffle(cards)` runs once, `cards.pop(0)` drains it, you never reshuffle. After ~13 rounds you hit `Game Over`.
- `pop(0)` is slow, `pop()` from the end is standard after shuffle.

Learner project: make `def create_deck():` that builds + shuffles + returns a fresh list. Call it each new game.

## Suggested Order

1. Rewrite `player_point_count(hand)` with a `for` loop — fixes scoring and teaches parsing + dicts.
2. Fix input with `.upper()` + `else`.
3. Add dealer hits to 17.
