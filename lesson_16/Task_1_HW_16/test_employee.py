from lesson_16.Task_1_HW_16.class_teamlead import TeamLead
from assertpy import assert_that


class TestEmployee:
    aqa_team_lead: TeamLead = TeamLead("Mark", 5000,
                                       "Test Department", 7, "Python")

    expected_marks_attrs: dict[str, object] = {
        "name": "Mark",
        "salary": 5000,
        "programming_language": "Python",
        "department": "Test Department",
        "team_size": 7
    }

    def test_employee_attrs(self):

        (assert_that(self.aqa_team_lead.__dict__,
                     "Desired User's attrs are not equal to desired user attributes.")
         .is_equal_to(self.expected_marks_attrs))
