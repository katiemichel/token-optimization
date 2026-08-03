"""
Hands-on example prompts: BAD vs. GOOD

Copy-paste these into separate Copilot Chat sessions to compare token usage live.
Open two chats side-by-side to show the difference.

Note the token count in each response metadata (hover over the response in VS Code).
"""

# ==============================================================================
# EXAMPLE 1: REFACTOR TASK
# ==============================================================================

REFACTOR_BAD = """
I have this Python code that needs to be cleaned up. Can you make it better?

def process_data(x):
  result = []
  for i in range(len(x)):
    if x[i] > 0:
      result.append(x[i] * 2)
    else:
      result.append(x[i])
  return result
"""

REFACTOR_GOOD = """
Refactor this function to use a list comprehension. Keep the logic identical;
no performance changes.

def process_data(x):
  result = []
  for i in range(len(x)):
    if x[i] > 0:
      result.append(x[i] * 2)
    else:
      result.append(x[i])
  return result

Return only the refactored function, no explanation.
"""

# ==============================================================================
# EXAMPLE 2: IMPLEMENTATION TASK
# ==============================================================================

IMPLEMENTATION_BAD = """
I need a function that calculates something. Can you write it?
"""

IMPLEMENTATION_GOOD = """
Write a function `calculate_discount(price, customer_type)` that:
- Takes a float `price` and string `customer_type` ('standard', 'vip', 'bulk')
- Returns the discounted price: standard=10%, vip=20%, bulk=15%
- Raise ValueError if customer_type not in that list
- Use only standard library

Here's the test it should pass:

def test_calculate_discount():
    assert calculate_discount(100, 'standard') == 90
    assert calculate_discount(100, 'vip') == 80
    assert calculate_discount(100, 'bulk') == 85
    with pytest.raises(ValueError):
        calculate_discount(100, 'unknown')

Implement only the function, no test code.
"""

# ==============================================================================
# EXAMPLE 3: DEBUGGING TASK
# ==============================================================================

DEBUGGING_BAD = """
My code doesn't work. Can you debug it?

Here's the code:

def add_item(warehouse, item):
    all_items.append(item)

def get_warehouse_items(warehouse):
    return all_items

# Test
add_item('warehouse_a', 'item1')
assert get_warehouse_items('warehouse_a') == ['item1']
assert get_warehouse_items('warehouse_b') == []  # FAILS! warehouse_b has the item too!
"""

DEBUGGING_GOOD = """
This code is failing the test below. The bug is that items added to warehouse_a 
appear in warehouse_b. Find the root cause and fix it.

Here's the code:

def add_item(warehouse, item):
    all_items.append(item)

def get_warehouse_items(warehouse):
    return all_items

# Test
add_item('warehouse_a', 'item1')
assert get_warehouse_items('warehouse_a') == ['item1']
assert get_warehouse_items('warehouse_b') == []  # FAILS

The issue is that all warehouses share the same list. Fix the data structure 
to keep each warehouse's items separate. Return only the corrected code.
"""

# ==============================================================================
# INSTRUCTOR NOTES
# ==============================================================================

INSTRUCTOR_NOTES = """
HOW TO USE THESE IN A LIVE WORKSHOP:

1. Open VS Code with two Copilot Chat panes side-by-side (or just two browser windows).

2. EXAMPLE 1 (Refactor):
   - Left pane: Send REFACTOR_BAD
   - Right pane: Send REFACTOR_GOOD
   - Point out token counts. Good should be 70–80% fewer response tokens.
   - Emphasize: "Specific input → bounded, quick response."

3. EXAMPLE 2 (Implementation):
   - Left pane: Send IMPLEMENTATION_BAD
   - Right pane: Send IMPLEMENTATION_GOOD
   - Model will ask for clarification on BAD; GOOD gets it in one turn.
   - Ask class: "How many turns would BAD take to nail down?"
   - Answer: Usually 3–4 turns to clarify input, output, edge cases, etc.

4. EXAMPLE 3 (Debugging):
   - Left pane: Send DEBUGGING_BAD (model asks for error message, stack trace, etc.)
   - Right pane: Send DEBUGGING_GOOD (model diagnoses and fixes in one shot)
   - Highlight how diagnosis + fix in one response = fewer tokens overall.

KEY TALKING POINTS:

- "The bad prompt isn't just less efficient—it gets you a longer response because 
   the model has to fill in the blanks. The good prompt is shorter AND gets a 
   shorter response."

- "These aren't edge cases. This is what happens every day in real work. Vague 
   asks beget long responses and back-and-forth. Specific asks get surgical 
   replies—and cost less."

- "The best part? The good prompt is EASIER to write once you know the pattern:
   (1) What do you want? (2) What are the constraints? (3) What should I NOT do?
   (4) Here's an example or test."

- "Pair specificity with the right model tier, and you're cutting costs by 60–80% 
   without sacrificing quality."
"""

if __name__ == "__main__":
    print(INSTRUCTOR_NOTES)
    print("\n\n=== COPY-PASTE EXAMPLES BELOW ===\n")
    print("REFACTOR_BAD:")
    print(REFACTOR_BAD)
    print("\n---\n")
    print("REFACTOR_GOOD:")
    print(REFACTOR_GOOD)
    print("\n\n")
    print("IMPLEMENTATION_BAD:")
    print(IMPLEMENTATION_BAD)
    print("\n---\n")
    print("IMPLEMENTATION_GOOD:")
    print(IMPLEMENTATION_GOOD)
    print("\n\n")
    print("DEBUGGING_BAD:")
    print(DEBUGGING_BAD)
    print("\n---\n")
    print("DEBUGGING_GOOD:")
    print(DEBUGGING_GOOD)
