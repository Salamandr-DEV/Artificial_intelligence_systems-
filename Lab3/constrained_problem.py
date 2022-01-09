from simpleai.search import CspProblem, backtrack, \
        min_conflicts, MOST_CONSTRAINED_VARIABLE, \
        HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

def constraint_unique(variables, values):
    return len(values) == len(set(values))

def constraint_bigger(variables, values):
    return values[0] > values[1]

def constraint_odd_even(variables, values):
    if values[0] % 2 == 0:
        return values[1] % 2 == 1
    else:
        return values[1] % 2 == 0

if __name__=='__main__':
    variables = ('John', 'Anna', 'Tom', 'Patricia')

    domains = {
        'John': [1, 2, 3],
        'Anna': [1, 3],
        'Tom': [2, 4],
        'Patricia': [2, 3, 4],
    }

    constraints = [
        (('John', 'Anna', 'Tom'), constraint_unique),
        (('Tom', 'Anna'), constraint_bigger),
        (('John', 'Patricia'), constraint_odd_even),
    ]

    problem = CspProblem(variables, domains, constraints)

    print('\nSolutions:\n\nNormal:', backtrack(problem))
    print('\nMost constrained variable:', backtrack(problem,
            variable_heuristic=MOST_CONSTRAINED_VARIABLE))
    print('\nHighest degree variable:', backtrack(problem,
            variable_heuristic=HIGHEST_DEGREE_VARIABLE))
    print('\nLeast constraining value:', backtrack(problem,
            value_heuristic=LEAST_CONSTRAINING_VALUE))
    print('\nMost constrained variable and least constraining value:',
            backtrack(problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE,
            value_heuristic=LEAST_CONSTRAINING_VALUE))
    print('\nHighest degree and least constraining value:',
            backtrack(problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE,
            value_heuristic=LEAST_CONSTRAINING_VALUE))
    print('\nMinimum conflicts:', min_conflicts(problem))