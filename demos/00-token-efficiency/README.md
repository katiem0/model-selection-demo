# Demo 00 — Token Efficiency Essentials

**Time:** ~5–8 minutes (best used during the opening slides, reference during live demos)  
**Purpose:** Build awareness of token cost, understand the math, and learn five concrete practices to reduce spend without sacrificing quality.

---

## Why This Matters (2 min)

### Slide 1: The Cost Reality

> 💰 **LLM costs are real.**
> 
> - Your Copilot plan scales with usage: more sessions, longer prompts, longer responses = higher bill.
> - Poor prompting = wasted spend. A bad prompt might take 3 turns to get right; a good prompt nails it in 1.
> - Better prompting → faster iteration → better code → **lower cost**.

### Slide 2: The Token Equation

> 📊 **Tokens are the unit of billing.**
>
> ```
> Total Cost = (Prompt Tokens + Response Tokens) × Model Unit Price
> ```
>
> - **Prompt tokens:** everything you send the model (code, context, instructions).
> - **Response tokens:** everything the model sends back (code, explanation, clarifications).
> - Both count equally toward the bill (though pricing varies by model tier).
> 
> **Insight:** If your prompt is 2× bigger but your response is half as long, you might spend more or less depending on the model.

### Slide 3: Cost Drivers

> 🎯 **Two levers to pull:**
>
> 1. **Bigger prompt = Higher cost** → include only essential context
> 2. **Longer response = Higher cost** → guide the model to stop when done

---

## Five Token-Efficiency Practices

### 1. **Be Specific (not generic)**
   - ❌ Bad: "Refactor my authentication module to be better."
   - ✅ Good: "Refactor auth.py to use bcrypt instead of plaintext hashing. Keep the API the same."
   - 💡 Specific prompts get right-sized responses; generic ones ramble.

### 2. **Limit Output Scope**
   - ❌ Bad: "Write a complete user management system."
   - ✅ Good: "Write a `User` class with `__init__`, `hash_password()`, and `verify_password()` methods. No ORM, standard library only."
   - 💡 Bounded scope = bounded response size.

### 3. **Reduce Context (Reuse sessions where appropriate)**
   - ❌ Bad: Paste your entire codebase into every chat.
   - ✅ Good: Reference files with `#file:path/to/file.py` in VS Code; start fresh chats between unrelated tasks.
   - 💡 Stale context bloats; new chats stay focused.

### 4. **Provide Clear Spec (not open-ended asks)**
   - ❌ Bad: "Make this function faster."
   - ✅ Good: "Optimize the `calculate()` function; it should return results in <100ms. Current bottleneck is the loop over `items`. Here's the spec: [insert requirements]."
   - 💡 Clear specs prevent back-and-forth; vague asks trigger clarification rounds.

### 5. **Match Model to Task (right tool, right cost)**
   - ❌ Bad: Use Claude Opus for every task (overkill on simple edits).
   - ✅ Good: Haiku for refactor, Sonnet for implementation, Opus for architecture.
   - 💡 Lightweight models cost 10× less for execution-heavy work; use them.

---

## Hands-On: Bad Prompt vs. Good Prompt

Use this to show live token impact during the workshop. Open two chats side-by-side.

### Example 1: Refactor Task

#### ❌ BAD PROMPT
```
I have this Python code that needs to be cleaned up. Can you make it better?

def process_data(x):
  result = []
  for i in range(len(x)):
    if x[i] > 0:
      result.append(x[i] * 2)
    else:
      result.append(x[i])
  return result
```

**What happens:**
- Model responds with not just refactoring, but explanation, alternative approaches, performance notes, etc.
- Response tokens: ~400–600 (depending on verbosity)
- You might ask follow-ups: "But why?" → more tokens.

#### ✅ GOOD PROMPT
```
Refactor this function to use a list comprehension. Keep the logic identical; no performance changes. Here's the code:

def process_data(x):
  result = []
  for i in range(len(x)):
    if x[i] > 0:
      result.append(x[i] * 2)
    else:
      result.append(x[i])
  return result

Return only the refactored function, no explanation.
```

**What happens:**
- Model knows exactly what you want: list comp, keep logic, no explanation.
- Response tokens: ~80–120 (just the code)
- You get the answer in one shot.

**Token savings:** ~70–80% fewer response tokens.

---

### Example 2: Implementation Task

#### ❌ BAD PROMPT
```
I need a function that calculates something. Can you write it?
```

**What happens:**
- Model asks for clarification: "What should it calculate? Input? Output? Edge cases?"
- You clarify. Model asks again. Back-and-forth.
- Total tokens across 3–4 turns: ~2000+
- You get what you wanted, but at high cost.

#### ✅ GOOD PROMPT
```
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
```

**What happens:**
- Model has everything: input, output, edge case, test.
- One response: working code.
- Total tokens: ~500–700 (one turn, done).

**Token savings:** ~65–70% fewer tokens across the entire task.

---

### Example 3: Debugging Task

#### ❌ BAD PROMPT
```
My code doesn't work. Can you debug it?
```

**What happens:**
- Model needs to see the code.
- You paste it. Model sees the failing test.
- Model asks: "What's the error message?"
- More back-and-forth. 3–5 turns.
- Total tokens: ~3000+

#### ✅ GOOD PROMPT
```
This test is failing. Find the root cause and fix it.

#file:inventory.py
#file:reporting.py
#file:test_inventory.py

Failing test: test_each_warehouse_is_independent

Error: adding an item to warehouse A somehow affects warehouse B.

Return only the diagnosis (one sentence) and the fix.
```

**What happens:**
- Model has context files and clear failure symptom.
- Model traces across files to root cause.
- One response: diagnosis + fix.
- Total tokens: ~1200–1500 (one turn with context, but tight).

**Token savings:** ~60% fewer tokens vs. back-and-forth.

---

## How to Show Token Counts Live

### In VS Code Copilot Chat:
1. Open a chat and send a prompt.
2. **Hover over the assistant response** (or look at the response metadata).
3. You'll see token usage displayed: *"Used N input tokens, M output tokens"*.

### During the workshop:
- Send the **bad prompt** first. Note the token count.
- Send the **good prompt** next (or show a screenshot of the previous result).
- Compare side-by-side: "Bad prompt: 400 output tokens. Good prompt: 100 output tokens. **Same result, 4× cheaper.**"

---

## Takeaway

> **Three rules for every prompt:**
>
> 1. **Be specific.** Generic asks get generic, long responses.
> 2. **Limit scope.** Bounded work = bounded response.
> 3. **Provide context.** Tests, specs, errors, and file references prevent clarification rounds.
>
> These three practices reduce token spend by **50–80%** without sacrificing quality. **Pair them with the right model tier, and you cut costs even further.**

---

## Integration with Other Demos

- **Before Demo 01–03:** Show this to frame why model selection matters—it's not just speed, it's cost.
- **During any hands-on demo:** Pause and say, "Notice the prompt? It's specific, bounded, and has examples. That's why we got it in one shot."
- **At the end:** Remind participants to apply these five practices to their daily workflow.

---

## Reference: Token Estimation

For rough mental math during the workshop:

| Content | Rough Tokens |
| --- | --- |
| One English word | ~1–2 |
| One line of Python | ~4–8 |
| A 40-line module | ~150–200 |
| A medium error stack trace | ~300–400 |
| This entire README | ~2500–3000 |

Use [Anthropic's token counter](https://github.com/anthropics/anthropic-sdk-python) or similar tools to verify.

---

## Notes for Instructors

- **Keep this punchy.** Token efficiency is the "why," not the centerpiece. 5–8 minutes max.
- **Show real token counts live.** Screenshots or live demos of VS Code Copilot Chat token display are worth 1000 words.
- **Reinforce with every demo.** As you run Demos 01–05, point out tight prompts and note the one-shot success.
- **End with a challenge:** "In your next Copilot session today, count how many clarification rounds you could eliminate with a tighter prompt."
