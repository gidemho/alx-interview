#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates a Pascal triangle of height n.

    Args:
        n (int): The height of the triangle.
    Returns:
        list: A 2D array representation of the triangle.
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


