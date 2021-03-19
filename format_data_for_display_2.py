import pytest


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


@pytest.mark.parametrize("func_input, expected_out", [
    ([
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
    ],
     [
         "Alfonsa Ruiz: Senior Software Engineer",
         "Sayid Khan: Project Manager",
     ]
    ),
    ("tjena", []),
    ('', []),
    ([], []),
    ([
        {
            "given_name": "Alfonsa",
            "title": "Senior Software Engineer",
            "family_name": "Ruiz",
        }
    ],
        ["Alfonsa Ruiz: Senior Software Engineer"]),
    ([
            {
                "given_naem": "Alfonsa",
                "title": "Senior Software Engineer",
                "family_name": "Ruiz",
            }
        ],
        []),

])
def test_format_data_for_display(func_input, expected_out):

    assert format_data_for_display(func_input) == expected_out
