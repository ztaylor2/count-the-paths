"""Test path count algorithms."""


def test_dynamic_two_d_array():
    """Test the two d array of the dynamic solution."""
    from count_paths import count_path_dynamic
    count_three_by_three = count_path_dynamic(3, 3)
    assert count_three_by_three == 6
