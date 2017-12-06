"""Test path count algorithms."""


def test_dynamic():
    """Test dynamic method."""
    from count_paths import count_path_dynamic
    count = count_path_dynamic(3, 3)
    assert count == 6


def test_recursive():
    """Test recursive method."""
    from count_paths import count_path_recursive
    count = count_path_recursive(3, 3)
    assert count == 6
