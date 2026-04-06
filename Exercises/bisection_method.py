import pytest

def square_root_bisection(target, tolerance=0.01, maximum_iterations=10):
    if target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif target == 0 or target == 1:
        print(f'The square root of {target} is {target}')
        return target
    else:
        current_iterations = 0
        if target < 1:
            high = 1
        else:
            high = target
        low = 0
        while current_iterations < maximum_iterations:
            mid = (high + low) / 2
            if high - low <= tolerance:
                print(f'The square root of {target} is approximately {mid}')
                return mid

            if target <= mid ** 2:
                high = mid
            else:
                low = mid
            current_iterations += 1
        print(f'Failed to converge within {maximum_iterations} iterations')
        return None

def test_fraction_high_iterations():
    assert pytest.approx(0.5) == square_root_bisection(0.25, 1e-7, 50)

def test_fraction_low_iterations():
    assert pytest.approx(0.03162279) == square_root_bisection(0.001, 1e-7, 50)

def test_large_num_low_iterations():
    assert square_root_bisection(225, 1e-7, 10) is None

def test_large_num_high_iterations():
    assert pytest.approx(15) == square_root_bisection(225, 1e-7, 100)

def test_large_num_high_iterations_low_tolerance():
    assert pytest.approx(15) == square_root_bisection(225, 1e-5, 100)