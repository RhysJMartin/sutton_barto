import matplotlib.pyplot as plt


class GamblersProblem:

    def __init__(self, probability_heads, target):
        self.target = target
        self.probability_heads = probability_heads
        self.states_plus = range(0, self.target + 1)
        self.states = range(1, self.target)
        self.state_value = self.initialise_state_value()
        self.tol = 0.000001

    def initialise_state_value(self):
        state_value = {state: 0 for state in self.states_plus}
        state_value[self.target] = 1
        return state_value

    @staticmethod
    def actions(state):
        return range(1, state + 1)

    def state_transition_probability(self, next_state, state, action):
        probability = 0
        if (next_state == state + action) | ((next_state == self.target) & ((state + action) > self.target)):
            probability = self.probability_heads
        elif next_state == (state - action):
            probability = 1 - self.probability_heads
        return probability

    def action_value_update(self, state, action):
        action_value = 0
        for next_state in self.states_plus:
            action_value += self.state_transition_probability(next_state, state, action) * self.state_value[next_state]
        return action_value

    def calculate_policy(self):
        policy = {}
        for state in self.states:
            best_action = -1
            state_value = -1
            for action in self.actions(state):
                action_value = self.action_value_update(state, action)
                if action_value > state_value + self.tol:
                    state_value = action_value
                    best_action = action
            policy[state] = best_action
        return policy

    @staticmethod
    def plot_dict(state_value, label, plot_type='line', xlabel=None, ylabel=None):
        sorted_state_value_tuples = sorted(state_value.items())
        x, y = zip(*sorted_state_value_tuples)
        if plot_type == 'line':
            plt.plot(x, y, label=label)
        elif plot_type == 'bar':
            plt.bar(x, y, label=label)
        if xlabel is not None:
            plt.xlabel(xlabel)
        if ylabel is not None:
            plt.ylabel(ylabel)
        plt.legend()
        plt.draw()

    def train(self):
        i = 1
        while True:
            print('Starting iteration {}'.format(i))
            delta = 0
            for state in self.states:
                prev_state_value = self.state_value[state]
                max_action_value = 0
                for action in self.actions(state):
                    action_value = self.action_value_update(state, action)
                    max_action_value = max(max_action_value, action_value)
                self.state_value[state] = max_action_value
                delta = max(delta, abs(self.state_value[state] - prev_state_value))
            if i in (1, 2, 3, 10):
                self.plot_dict(self.state_value, 'Iter {}'.format(i), xlabel='State', ylabel='Value')
            if delta < self.tol:
                print('Found state value mapping: {}'.format(self.state_value))
                print('Found optimal policy: {}'.format(self.calculate_policy()))
                break
            i += 1


if __name__ == '__main__':
    gamblers_problem = GamblersProblem(0.4, 100)
    # Train
    gamblers_problem.train()
    # Plot the optimal policy
    plt.figure(2)
    gamblers_problem.plot_dict(gamblers_problem.calculate_policy(), 'Optimal Action',  plot_type='bar', xlabel='State', ylabel='Action')
    # display plots
    plt.show()
