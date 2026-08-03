# Sample document

Welcome to the sample. This file is the input for the link checker demo.

## Local links that should work

- [Sibling file](./linkcheck.py)
- [The demo README](./README.md)
- [Up one level to the source doc](../../docs/improve-agent-quality-and-token-optimization.md)

## Local links that are broken

- [Missing file in the same folder](./does-not-exist.md)
- [Broken relative path](./fixtures/missing.txt)
- [Typo in the path](./linkceck.py)

## External links (out of scope for v1)

- [GitHub Copilot docs](https://docs.github.com/copilot)
- [The accompanying blog post](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/)

## Anchor links (out of scope for v1)

- [Jump to the top of this file](#sample-document)
- [Section that does not exist on this page](#nope)

## Reference-style links

This [reference link][working-ref] resolves to a sibling file.
This [reference link][broken-ref] does not.

[working-ref]: ./linkcheck.py
[broken-ref]: ./not-here.md

## Image links

![Local image that is missing](./images/logo.png)
![Remote image](https://example.com/logo.png)
