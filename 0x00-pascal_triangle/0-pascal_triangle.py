#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates a Pascal triangle of height n

    Args:
        n (int): The height of the triangle
    Returns:
        triangle: A 2D array representation of the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        left_side = [1]
        for j in range(1, i):
            left_side.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        left_side.append(1)
        triangle.append(left_side)
    return triangle


n = int(input("n? "))
print(pascal_triangle(n))
