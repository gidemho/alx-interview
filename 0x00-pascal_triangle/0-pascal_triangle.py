def pascal_triangle(n):
    """
    Generates Pascal's Triangle of height n.

    Args:
        n (int): The number of rows in the triangle.
    
    Returns:
        list: A 2D list representing the triangle. Each inner list contains 
              the elements of the corresponding row in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        current_row = [1]  # Start each row with 1
        for j in range(1, i):
            current_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        current_row.append(1)  # End each row with 1
        triangle.append(current_row)
    
    return triangle
