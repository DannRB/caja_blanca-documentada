import pytest
from process import process


@pytest.mark.statement
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"]),
])
def test_statement_coverage(values, expected):
    assert process(values) == expected


@pytest.mark.branch
@pytest.mark.parametrize("values, expected", [
    ([2], ["positivo", "par"]),
    ([-3], []),
    ([], []),
])
def test_branch_coverage(values, expected):
    assert process(values) == expected
