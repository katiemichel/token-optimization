"""
Simple token counter for demonstration purposes.

This uses a basic approximation (word count + code factor) for rough estimation.
For precise counts, use your model's tokenizer or the Copilot Chat token metadata.

Usage:
    python token_counter.py < some_code.py
    # or
    python -c "from token_counter import estimate_tokens; print(estimate_tokens('your text here'))"
"""

import re
import sys


def estimate_tokens(text: str) -> int:
    """
    Rough token estimate for English + Python code.
    
    This is a heuristic, not a true tokenizer. Actual token counts will vary by model.
    
    Rules:
    - English: ~1–1.3 tokens per word
    - Python: ~0.3–0.5 tokens per character (denser than English)
    - Whitespace & punctuation: counted separately
    """
    if not text:
        return 0
    
    # Count words (roughly 1 token each in English)
    words = len(text.split())
    
    # Count lines (Python code is denser; roughly 4 tokens per line avg)
    lines = len(text.splitlines())
    
    # Heuristic: English-heavy text uses word count; code-heavy uses line count
    # Detect code by looking for common Python patterns
    is_code = bool(re.search(r'(def |class |import |return |if |for |while |\.|\[|\{)', text))
    
    if is_code:
        # Code: use line-based estimate (4 tokens per line is conservative)
        return max(words, lines * 4)
    else:
        # English: use word-based estimate (1.2 tokens per word on average)
        return int(words * 1.2)


def compare_prompts(bad_prompt: str, good_prompt: str) -> None:
    """Show token savings side-by-side."""
    bad_tokens = estimate_tokens(bad_prompt)
    good_tokens = estimate_tokens(good_prompt)
    savings = ((bad_tokens - good_tokens) / bad_tokens) * 100 if bad_tokens > 0 else 0
    
    print(f"❌ Bad prompt:  ~{bad_tokens} tokens")
    print(f"✅ Good prompt: ~{good_tokens} tokens")
    print(f"💰 Savings:    {savings:.0f}%")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        # Show example comparison
        bad = "I have code that needs to be better. Can you help?"
        good = (
            "Refactor this function to use list comprehension. "
            "Keep logic identical.\n\ndef process_data(x):\n  result = []\n"
            "  for i in range(len(x)):\n    if x[i] > 0:\n"
            "      result.append(x[i] * 2)\n    else:\n"
            "      result.append(x[i])\n  return result"
        )

        print("📊 Token Comparison Example\n")
        compare_prompts(bad, good)
    else:
        # Read from stdin and estimate
        text = sys.stdin.read()
        tokens = estimate_tokens(text)
        print(f"Estimated tokens: {tokens}")
