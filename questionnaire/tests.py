from django.test import TestCase

from dependency_checker import check_actual_answers_against_expression
from .models import Question


class QuestionSetTests(TestCase):
    def test_dependencies_for_multiple_choice_question(self):
        check_question = Question()
        self.assertTrue(check_actual_answers_against_expression('3B', ['3B', '3E'], check_question))
        self.assertTrue(check_actual_answers_against_expression('3E', ['3B', '3E'], check_question))

    def test_dependencies_for_multiple_choice_question_false(self):
        check_question = Question()
        self.assertFalse(check_actual_answers_against_expression('3C', ['3B', '3E'], check_question))
        self.assertFalse(check_actual_answers_against_expression('3F', ['3B', '3E'], check_question))

    def test_dependencies_for_multiple_choice_question_negation(self):
        check_question = Question()
        self.assertTrue(check_actual_answers_against_expression('!3C', ['3B', '3E'], check_question))
        self.assertTrue(check_actual_answers_against_expression('!3A', ['3B', '3E'], check_question))

    def test_dependencies_for_multiple_choice_question_negation_false(self):
        check_question = Question()
        self.assertFalse(check_actual_answers_against_expression('!3C', ['3C', '3E'], check_question))
        self.assertFalse(check_actual_answers_against_expression('!3E', ['3C', '3E'], check_question))

    def test_dependencies_for_single_choice_question(self):
        check_question = Question()
        self.assertTrue(check_actual_answers_against_expression('3B', '3B', check_question))
        self.assertFalse(check_actual_answers_against_expression('3C', '3B', check_question))
        self.assertTrue(check_actual_answers_against_expression('!3C', '3B', check_question))
        self.assertFalse(check_actual_answers_against_expression('!3C', '', check_question))

    def test_dependencies_for_numeric_checks(self):
        check_question = Question()
        self.assertTrue(check_actual_answers_against_expression('>5.6', '6', check_question))
        self.assertFalse(check_actual_answers_against_expression('>5.6', '3.6', check_question))
        self.assertFalse(check_actual_answers_against_expression('>5.6', '5.6', check_question))

        self.assertTrue(check_actual_answers_against_expression('>=5.6', '6', check_question))
        self.assertFalse(check_actual_answers_against_expression('>=5.6', '3.6', check_question))
        self.assertTrue(check_actual_answers_against_expression('>=5.6', '5.6', check_question))

        self.assertTrue(check_actual_answers_against_expression('<5.6', '4.6', check_question))
        self.assertFalse(check_actual_answers_against_expression('<5.6', '8.6', check_question))
        self.assertFalse(check_actual_answers_against_expression('<5.6', '5.6', check_question))

        self.assertTrue(check_actual_answers_against_expression('<=5.6', '3.6', check_question))
        self.assertFalse(check_actual_answers_against_expression('<=5.6', '9.6', check_question))
        self.assertTrue(check_actual_answers_against_expression('<=5.6', '5.6', check_question))
