import numpy as np

from sample_poetry_docker_with_build.module import plus


def test_module_plus():
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    c = np.array([2, 4, 6])

    assert (plus(a, b) == c).all()
