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

> I need a function that calculates something. Can you write it?

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

```text
Compare the bad and good prompts in #file:demos/00-token-efficiency/example_prompts.py.

Explain why the good prompt is cheaper and more reliable, and call out the three prompt rules it demonstrates.
```

## What to point out

- Specific prompts get smaller, more useful answers.
- Bounded scope keeps both the prompt and the response short.
- Clear specs and examples prevent clarification rounds.
- The same task can cost much less without sacrificing quality.

## The contrast moment (optional, ~2 min)

1. Reset the chat.
2. Switch to GPT-5.5 or Claude Opus 4.7.
3. Set thinking effort to low for the explanation prompt.
4. Paste the same comparison prompt.
5. Point out whether the response becomes more explanatory than the demo needs.
6. Reinforce the lesson: on simple prompt-crafting work, more reasoning can be overhead.

## Reset before the next demo

> Click New chat in Copilot Chat. Demo 01 should start clean.

## Instructor notes

- Keep this fast. The point is to show the pattern, not to dwell on token math.
- Use the live token metadata in VS Code if it is visible.
- Tie the result back to the next demos: better prompts make the rest of the workshop cheaper and faster.
