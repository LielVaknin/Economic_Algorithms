import doctest
from typing import List


class Agent:
    """This class represents an agent"""

    def __init__(self, values):
        self.values = values

    def value(self, option: int) -> float:
        """
        :param option: The index of an option
        :return: The value of the option to the agent
        """
        return self.values[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    """
    Question 1.a:
    Receives a list of agents and two options and returns whether option 1 is a Pareto improvement of option 2
    :param agents: A list of agents
    :param option1: One option
    :param option2: Second option
    :return: Returns True if option 1 is a Pareto improvement of option 2, else - return False

    >>> isParetoImprovement(agents=agents, option1=1, option2=2)
    False
    >>> isParetoImprovement(agents=agents, option1=3, option2=2)
    True
    """
    if option1 == option2:
        return False
    is_pareto_improvement = True
    for agent in agents:
        if agent.value(option1) < agent.value(option2):
            is_pareto_improvement = False
    return is_pareto_improvement


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    """
    Question 1.b:
    Receives a list of agents, an option number and a list of all options
    and returns whether the given option is Pareto optimal
    :param agents: A list of agents
    :param option: A given option
    :param allOptions: A list of all options
    :return: Returns True if a given option is Pareto optimal, else - return False

    >>> isParetoOptimal(agents=agents, option=1, allOptions=all_options)
    True
    >>> isParetoOptimal(agents=agents, option=2, allOptions=all_options)
    False
    >>> isParetoOptimal(agents=agents, option=3, allOptions=all_options)
    True
    >>> isParetoOptimal(agents=agents, option=4, allOptions=all_options)
    True
    >>> isParetoOptimal(agents=agents, option=5, allOptions=all_options)
    True
    """
    is_pareto_optimal = True
    for op in allOptions:
        if isParetoImprovement(agents, op, option):
            is_pareto_optimal = False
    return is_pareto_optimal


if __name__ == '__main__':
    ami_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    tami_values = {1: 3, 2: 1, 3: 2, 4: 5, 5: 4}
    rami_values = {1: 3, 2: 5, 3: 5, 4: 1, 5: 1}
    ami = Agent(ami_values)
    tami = Agent(tami_values)
    rami = Agent(rami_values)
    agents = [ami, tami, rami]
    all_options = [1, 2, 3, 4, 5]
    doctest.testmod()
