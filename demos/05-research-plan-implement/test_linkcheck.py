"""Smoke test for the markdown link checker.

This is the only test that exists at the start of the demo. The Plan phase
adds more cases; the Implement phase makes them all pass.
"""
import pytest


def test_linkcheck_module_importable():
    import linkcheck  # noqa: F401


@pytest.mark.skip(reason="Implemented during Phase 3 of the demo.")
def test_finds_at_least_one_broken_local_link():
    from pathlib import Path

    from linkcheck import check_file

    sample = Path(__file__).parent / "sample.md"
    results = check_file(sample)
    broken = [r for r in results if r.is_broken]
    assert broken, "expected to find broken local links in sample.md"
