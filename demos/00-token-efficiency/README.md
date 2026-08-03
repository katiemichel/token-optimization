# Demo 00 - Token Efficiency Essentials

**Time:** ~5-8 minutes
**Recommended model:** GPT-5 mini
**Contrast model (optional):** GPT-5.5 or Claude Opus 4.7, to show how the same task can become more verbose than necessary

## The setup

This demo is a short framing exercise, not a coding task. It shows how prompt quality affects response length, clarification rounds, and total token usage.

- [`example_prompts.py`](example_prompts.py) contains the bad/good prompts for the live comparison.
- [`token_counter.py`](token_counter.py) provides a rough token estimate for quick demonstrations.

## Run it

```bash
python demos/00-token-efficiency/token_counter.py --demo
python demos/00-token-efficiency/example_prompts.py
```

## The exact prompt to paste

Use the prompts below during the workshop. Open two Copilot Chat sessions side by side, paste the bad prompt on the left and the good prompt on the right, then compare the response length and token metadata.

### Example 1: Refactor task

Bad prompt:

> I have this Python code that needs to be cleaned up. Can you make it better?
>
> def process_data(x):
> 	result = []
> 	for i in range(len(x)):
> 		if x[i] > 0:
> 			result.append(x[i] * 2)
> 		else:
> 			result.append(x[i])
> 	return result

Good prompt:

> Refactor this function to use a list comprehension. Keep the logic identical; no performance changes.
>
> def process_data(x):
> 	result = []
> 	for i in range(len(x)):
> 		if x[i] > 0:
> 			result.append(x[i] * 2)
> 		else:
> 			result.append(x[i])
> 	return result
>
> Return no explanation.

### Example 2: Implementation task

Bad prompt:

> I need a function that calculates discount, can you write it?

Good prompt:

> Write a function `calculate_discount(price, customer_type)` that:
> - Takes a float `price` and string `customer_type` ('standard', 'vip', 'bulk')
> - Returns the discounted price: standard=10%, vip=20%, bulk=15%
> - Raise ValueError if customer_type not in that list
> - Use only standard library
>
> Here's the test it should pass:
>
> def test_calculate_discount():
> 		assert calculate_discount(100, 'standard') == 90
> 		assert calculate_discount(100, 'vip') == 80
> 		assert calculate_discount(100, 'bulk') == 85
> 		with pytest.raises(ValueError):
> 				calculate_discount(100, 'unknown')
>
> Implement only the function, no test code.

### Example 3: Debugging task

Bad prompt:

> My code doesn't work. Can you debug it?
>
> Here's the code:
>
> def add_item(warehouse, item):
> 		all_items.append(item)
>
> def get_warehouse_items(warehouse):
> 		return all_items
>
> # Test
> add_item('warehouse_a', 'item1')
> assert get_warehouse_items('warehouse_a') == ['item1']
> assert get_warehouse_items('warehouse_b') == []  # FAILS! warehouse_b has the item too!

Good prompt:

> This code is failing the test below. The bug is that items added to warehouse_a
> appear in warehouse_b. Find the root cause and fix it.
>
> Here's the code:
>
> def add_item(warehouse, item):
> 		all_items.append(item)
>
> def get_warehouse_items(warehouse):
> 		return all_items
>
> # Test
> add_item('warehouse_a', 'item1')
> assert get_warehouse_items('warehouse_a') == ['item1']
> assert get_warehouse_items('warehouse_b') == []  # FAILS
>
> The issue is that all warehouses share the same list. Fix the data structure
> to keep each warehouse's items separate. Return only the corrected code.

If you want a single instruction to give the assistant during the demo, use this:

> Compare the bad and good prompts in #file:demos/00-token-efficiency/example_prompts.py.
>
> Explain why the good prompt is cheaper and more reliable, and call out the three prompt rules it demonstrates.

## What to notice

- The good prompt response is shorter and correct. The bad prompt response hedges, explains, or asks a clarifying question.
- Bounded scope keeps both the prompt and the response small.
- Including the test as the spec eliminates a clarification round entirely.
- The same task, with a tighter prompt, costs less and requires fewer follow-up turns.

## Reset before the next demo

> Click New chat in Copilot Chat. Demo 01 should start clean.
