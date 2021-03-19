import pytest
from random import randint
from timeit import repeat


example_people_data = [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def format_data_for_display(people=[]):
    res_list = []
    if not people:
        return []
    for dct in people:
        try:
            formal_title = f"{dct['given_name']} {dct['family_name']}: {dct['title']}"
        except (KeyError, TypeError):
            return []
        res_list.append(formal_title)
    return res_list

# @pytest.mark.tryfirst
# def test_format_data_for_display(example_people_data):
#
#     assert format_data_for_display(example_people_data) == [
#         "Alfonsa Ruiz: Senior Software Engineer",
#         "Sayid Khan: Project Manager",
#     ]
#
#
# def test_wrong_inputs():
#     assert not format_data_for_display(['tjena'])
#
#
# def test_empty_input():
#     assert not format_data_for_display()


run_sorting_algorithm('format_data_for_display', example_people_data)