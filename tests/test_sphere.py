import pytest
from geometry.sphere import volume_sphere


def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid sphere radius.
    """
    radius = 2.0
    expected = 33.51
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-2)


def test_volume_sphere_negative_radius():
    """
    Test that negative radius raises ValueError.
    """
    with pytest.raises(ValueError):
        volume_sphere(-1.0)


def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 2.5
    expected = (4/3) * 3.14159 * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
