"""Chapter 2 - Sets

This file introduces sets, which are unordered collections of unique items.
"""

print("--- Sets ---")

languages = {"Python", "Java", "Python", "C++"}
print("Set with duplicates removed:", languages)

languages.add("JavaScript")
print("After adding an item:", languages)

print("Contains Python?", "Python" in languages)

other_languages = {"Python", "Go", "Rust"}
print("Union:", languages | other_languages)
print("Intersection:", languages & other_languages)
