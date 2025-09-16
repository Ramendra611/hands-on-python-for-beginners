# **Assignment: OOP Concepts with IPL, Cricketers, Batsmen, and Bowlers**

## **Part A: Basics of Inheritance and super()**

1. Create a base class `Cricketer` with attributes like `name` and `team`. Add a method `play()` that prints a generic message.  
2. Create a subclass `Batsman` that inherits from `Cricketer` and adds a `batting_average` attribute.  

   * Use `super().__init__()` to initialize the parent attributes.  
3. Create a subclass `Bowler` that inherits from `Cricketer` and adds a `bowling_average` attribute.  

   * Again, use `super().__init__()` properly.  

**Learning Points**

* How to use `super()` to call a parent class constructor.  
* Why `super()` is better than calling the parent explicitly.  

---

## **Part B: super() with Methods (not just `__init__`)**

4. Add a method `introduce()` in `Cricketer` that introduces the player.  
5. Override `introduce()` in `Batsman` and `Bowler` to add their role-specific stats (batting/bowling averages).  
6. Use `super().introduce()` in the child classes to reuse the parent logic and extend it.  

**Learning Points**

* How `super()` can be used for methods other than `__init__`.  
* How code reuse works in inheritance hierarchies.  

---

## **Part C: Flexible Initialization with `*args` and `**kwargs`**

7. Modify the constructors of `Batsman` and `Bowler` to accept `*args` and `**kwargs` and pass them to `super()`.  
8. Demonstrate that adding new attributes to `Cricketer` won’t break `Batsman` and `Bowler` classes.  

**Learning Points**

* How and why to use `*args` and `**kwargs` with `super()`.  
* Avoiding repetitive argument lists (DRY principle).  

---

## **Part D: Polymorphism**

9. Create a list of mixed `Cricketer`, `Batsman`, and `Bowler` objects.  
10. Iterate through the list and call the `play()` method on each.  

**Learning Points**

* Demonstrates **polymorphism**: same method name (`play`), different behavior depending on the class.  

---

## **Part E: Encapsulation**

11. In `Cricketer`, make the `salary` attribute private (e.g., `self.__salary`).  
12. Add `get_salary()` and `set_salary()` methods with validation (salary must be positive).  
13. Show that direct access to `__salary` raises an error.  

**Learning Points**

* Encapsulation: restricting direct access to attributes.  
* Using getters and setters for controlled access.  

---



---
# Extensions: Advanced OOP with the IPL Model

## **Part F: Composition (IPL Teams)**

14. Create a class `IplTeam` with attributes: `name`, `players` (a list).  
15. Add methods to `IplTeam` to:  

* `add_player()` → add a cricketer to the team.  
* `list_players()` → show all players in the team.  

16. Extend the team logic to also maintain lists of batsmen and bowlers separately.  
17. Demonstrate adding players to teams and displaying them.  

**Learning Points**

* Composition: Teams are not subclasses of cricketers but contain cricketers.  
* Organizing related objects into aggregates.  
## **Part G: Multiple Inheritance and MRO**
18. Create a mixin class `ContractedPlayer`
        - with an attribute `contract_amount`
        - method `show_contract()` that prints `contract_amount`
20. Make a new class `AllRounder` that inherits from both `Batsman` and `Bowler`.  
21. Use `super()` in `AllRounder` to call parent methods and print out the Method Resolution Order using `AllRounder.__mro__`.

**Learning Points**  
- How multiple inheritance works in Python.
- How Mixins add specific functionality without being a “main parent” class.
- Understanding the Method Resolution Order (MRO) and cooperative `super()` calls.  

---

## **Part H: Abstract Base Classes (Interfaces)**
21. Convert `Cricketer` into an abstract base class using `abc.ABC`.  
22. Define an abstract method `role_description()` that subclasses (`Batsman`, `Bowler`) must implement.  
23. Show that you cannot instantiate `Cricketer` directly.

**Learning Points**  
- How abstract base classes enforce contracts.  
- Forcing subclasses to implement required methods.  

---

## **Part I: @property vs Explicit Getters/Setters**
24. Refactor the `salary` attribute in `Cricketer` to use `@property` and `@salary.setter` with validation.  
25. Compare it with earlier `get_salary()` and `set_salary()` methods by showing both approaches.

**Learning Points**  
- Idiomatic encapsulation in Python with `@property`.  
- Cleaner access vs. explicit getters/setters.  

---

## **Part J: Type Hints and Duck Typing (Protocols)**
26. Add type hints to public APIs.  
27. Create a `Protocol` named `PlayerProtocol` with `introduce()` and `play()`.  
28. Write a function that accepts any object matching `PlayerProtocol`, and pass both `Cricketer` subclasses and a non-Cricketer object that still satisfies the protocol.

**Learning Points**  
- Type hints for readability/tooling.  
- Duck typing and structural subtyping with `Protocol`.  

---

## **Part K: isinstance / issubclass Checkpoints**
29. Create a function `filter_batsmen(players)` that returns only instances of `Batsman`.  
30. Use `issubclass()` to check relationships among `Batsman`, `Bowler`, `AllRounder`, and `Cricketer`.

**Learning Points**  
- `isinstance()` for object membership.  
- `issubclass()` for class relationships.  

---

## **Bonus: Dependency Injection**
31. Create a `StatsProvider` that supplies batting/bowling averages.  
32. Modify `Batsman` and `Bowler` to accept a `stats_provider` rather than hardcoding stats.  
33. Demonstrate replacing the real provider with a `MockStatsProvider` for tests.

**Learning Points**  
- Decoupling via injection.  
- Easier testing with swappable implementations.  



