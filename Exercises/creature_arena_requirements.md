# Exercise 6: Creature Arena

Build a text-based creature battle simulator using classes and objects. Two creatures face off in a turn-based duel, each with unique stats and abilities.

---

## Part 1 — The `Creature` Class

Define a `Creature` class that represents a battle creature.

1. **Initialization** — Each creature has a `name` (string), `hit_points` (int), `strength` (int), and `defense` (int). Store these as instance attributes. Validate that `name` is a non-empty string and that all stats are positive integers; raise appropriate exceptions for invalid input.

2. **Class attribute** — Track how many creatures have been created across all instances.

3. **String representation** — Printing a creature should produce a readable summary, e.g. `Fang (HP: 20 | STR: 6 | DEF: 3)`. Displaying a creature in a list or collection should show something shorter, e.g. `Creature('Fang')`.

4. **Length** — Calling `len()` on a creature should return the sum of all three stats (hit_points + strength + defense), representing its overall "power level."

5. **Equality** — Two creatures are considered equal if they have the same name and the same stats.

---

## Part 2 — Abilities via Dynamic Attributes

Creatures can learn abilities at runtime. An ability is just a string describing what it does (e.g. `"Deals 5 bonus damage"`).

6. **`learn_ability(ability_name, description)`** — Attach the ability as an attribute on the creature. The attribute name should be the ability name. If the creature already knows this ability, raise a custom exception. Also reject ability names that clash with the creature's core attributes (e.g. `"strength"`, `"name"`).

7. **`use_ability(ability_name)`** — Check if the creature has the ability; if yes, return its description. If not, return a message saying the creature hasn't learned that ability.

8. **`forget_ability(ability_name)`** — Remove the ability from the creature. If the ability doesn't exist, handle it gracefully.

9. **`list_abilities()`** — Return a list of all ability names the creature currently has. You'll need a way to distinguish ability attributes from the creature's core stats.

---

## Part 3 — The `Arena` Class

Define an `Arena` class where creatures fight.

10. **Initialization** — The arena holds a roster (a list of creatures). It should start empty.

11. **`register(creature)`** — Add a creature to the roster. Don't allow duplicate creatures (use your equality logic). Raise an exception if the creature is already registered.

12. **`roster_summary()`** — Return a single formatted string showing all registered creatures with their stats, one per line. If the roster is empty, return a message saying so.

13. **`battle(creature_a, creature_b)`** — Simulate a turn-based fight between two registered creatures. On each turn:
    - The attacker deals damage equal to its `strength` minus the defender's `defense` (minimum 1 damage).
    - Subtract the damage from the defender's `hit_points`.
    - Alternate turns until one creature's `hit_points` drop to 0 or below.
    - Return the winner.
    - The battle must not permanently alter the creatures' stats. Work on temporary HP values so that creatures can fight again afterwards.
    - Both creatures must be in the roster; if either isn't, raise an exception.
    - Wrap the battle logic so that unexpected errors during combat are caught and reported without crashing the program.

---

## Part 4 — Custom Exception

14. **Define a custom exception class** for arena-related errors (e.g. duplicate registration, battling an unregistered creature, learning a duplicate ability). Use it wherever the requirements above call for raising exceptions.

---

## Part 5 — Putting It Together

15. **`main()`** — Write a `main` function (guarded by `if __name__ == "__main__"`) that:
    - Creates at least three creatures with different stats.
    - Teaches at least one creature an ability, then uses and forgets it.
    - Registers the creatures in the arena and prints the roster summary.
    - Runs at least two battles and prints the results.
    - Deliberately triggers at least one of your custom exceptions inside a `try`/`except` block and handles it with an informative message.

---

## What This Exercise Targets

| Topic | Where in exercise |
|---|---|
| Classes, `__init__`, instance attributes | `Creature` and `Arena` classes |
| Class attributes | Creature creation counter |
| `__str__`, `__repr__` | String representation (#3) |
| `__len__` | Power level (#4) |
| `__eq__` | Creature equality (#5) |
| `setattr` / `getattr` / `hasattr` / `delattr` | Ability system (#6–9) |
| `try`/`except`/`raise`, custom exceptions | Battle logic, duplicate checks (#11, #13, #14) |
| Falsy checks (weakness) | Empty roster check in `roster_summary` |
| Comprehension + `join()` (weakness) | Roster summary formatting |
