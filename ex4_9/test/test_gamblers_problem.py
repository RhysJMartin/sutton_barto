from unittest import TestCase
from suttonbarto.ex4_9.gamblers_problem import GamblersProblem


class TestGamblersProblem(TestCase):

    def setUp(self):
        probability_heads = 0.4
        self.gamblers_problem = GamblersProblem(probability_heads, 100)

    def test_heads(self):
        state = 50
        action = 2
        next_state = 52
        expected_transition_probability = 0.4
        transition_probability = self.gamblers_problem.state_transition_probability(next_state, state, action)
        self.assertAlmostEqual(expected_transition_probability, transition_probability)

    def test_heads_terminal(self):
        state = 90
        action = 50
        next_state = 100
        expected_transition_probability = 0.40
        transition_probability = self.gamblers_problem.state_transition_probability(next_state, state, action)
        self.assertAlmostEqual(expected_transition_probability, transition_probability)

    def test_tails(self):
        state = 50
        action = 2
        next_state = 48
        expected_transition_probability = 0.6
        transition_probability = self.gamblers_problem.state_transition_probability(next_state, state, action)
        self.assertAlmostEqual(expected_transition_probability, transition_probability)

    def test_invalid_transition(self):
        state = 50
        action = 2
        next_state = 50
        expected_transition_probability = 0
        transition_probability = self.gamblers_problem.state_transition_probability(next_state, state, action)
        self.assertAlmostEqual(expected_transition_probability, transition_probability)

    # def test_plot(self):
    #     state_values = {1:10,2:20,3:30}
    #     GamblersProblem.plot_state_value(state_values)




