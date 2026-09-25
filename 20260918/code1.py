import sympy as sp

def calculate_derivative():
    # 1. Define your variables
    x, y, z = sp.symbols('x y z')
    
    # 2. Define the function you want to differentiate
    # Example 1: Single variable trigonometric/exponential function
    # expr = sp.sin(x) * sp.exp(x**2)
    
    # Example 2: Multivariable function for partial derivatives
    expr = x**3 * y**2 + sp.sin(y) * z
    
    # 3. Choose the differentiation type
    # Option A: Ordinary Derivative with respect to x
    diff_order = 1  # 1 for first derivative, 2 for second, etc.
    result_ordinary = sp.diff(expr, x, diff_order)
    
    # Option B: Partial Derivative (e.g., first with respect to x, then y)
    result_partial = sp.diff(expr, x, y)
    
    print("--- Differential Calculus Results ---")
    print(f"Original Expression: {expr}")
    print(f"Derivative w.r.t x (Order {diff_order}): {result_ordinary}")
    print(f"Partial Derivative (d^2 / dx dy): {result_partial}")

if __name__ == "__main__":
    calculate_derivative()