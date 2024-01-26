import sympy as sp

# Define the symbol for x and a dummy symbol for epsilon
x, epsilon = sp.symbols('x epsilon')

# Define a function to analyze the improper integral
def analyze_improper_integral(f, a, b):
    # Define the integral from a+epsilon to b
    integral_expr = sp.integrate(f, (x, a + epsilon, b))
    # Compute the limit of the integral as epsilon approaches 0
    limit_expr = sp.limit(integral_expr, epsilon, 0, dir='+')
    
    # Determine if the integral is convergent or divergent
    is_convergent = limit_expr.is_finite

    # Create the LaTeX for the integral computation
    latex_integral = sp.latex(integral_expr)
    latex_limit = sp.latex(limit_expr)

    return {
        'is_convergent': is_convergent,
        'integral': latex_integral,
        'limit': latex_limit,
        'integral_expr': integral_expr  # Include the sympy expression for further processing
    }

# Define the function for the integral
f = 1 / (x - 4)

# Define the limits of integration
a, b = 4, 8

# Check for discontinuities and define epsilon accordingly
discontinuities = sp.singularities(f, x)
epsilon_conditions = [sp.Lt(epsilon, b - point) for point in discontinuities if a < point < b]

# If there's a discontinuity in (a, b), adjust a to be a+epsilon
if epsilon_conditions:
    a += epsilon

# Analyze the integral
analysis_results = analyze_improper_integral(f, a, b)

# Generate LaTeX for the example solution
continuous_range = f"({a}, {b}]" if epsilon_conditions else f"[{a}, {b}]"
bounded_statement = "bounded" if analysis_results['is_convergent'] else "not bounded"
discontinuity_approach = "from the right" if epsilon_conditions else ""

latex_solution = f"""\
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\begin{{document}}

The function $f(x) = {sp.latex(f)}$ is defined for $x > 2$ and continuous on {continuous_range}. However, $f$ is {bounded_statement} on {continuous_range} since the function approaches infinity as $x$ approaches 2 {discontinuity_approach}. Thus, the integral $\\int_{{2}}^{{4}} {sp.latex(f)} \\, dx$ is improper.

To determine if the improper integral is convergent or divergent, we evaluate the integral with an epsilon approach from the point of discontinuity:

\\[
\\int_{{2+\\epsilon}}^{{4}} {sp.latex(f)} \\, dx = {analysis_results['integral']}
\\]

We then take the limit of this integral as $\\epsilon$ approaches 0 from the right:

\\[
\\lim_{{\\epsilon \\to 0^+}} \\int_{{2+\\epsilon}}^{{4}} {sp.latex(f)} \\, dx = {analysis_results['limit']}
\\]

Since the limit is {"" if analysis_results['is_convergent'] else "not "}finite, the integral is {"" if analysis_results['is_convergent'] else "divergent"}.

\\end{{document}}
"""

print(latex_solution)

