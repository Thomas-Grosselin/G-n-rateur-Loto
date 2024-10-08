import collections
import random

# Exemple de tirages passés
tirages = [
    
    [1, 4, 21, 24, 42, 3],
    [3, 6, 7, 22, 28, 7],
    [1, 17, 24, 30, 43, 7],
    [10, 21, 25, 38, 41, 8],
    [1, 6, 45, 47, 48, 6],
    [10, 25, 29, 34, 38, 3],
    [11, 18, 30, 35, 46, 2],
    [6, 11, 25, 28, 46, 2],
    [8, 16, 30, 40, 42, 2],
    [3 ,6, 13, 28, 33, 4],
    [5, 28, 34, 39, 47, 8],
    [18, 31, 35, 39, 43, 7],
    [4, 6, 7, 35, 47, 1],
    [9, 15, 39, 48, 49, 7],
    [2, 3, 27, 43, 48, 8],
    [10, 19, 28, 37, 38, 7],
    [19, 32, 41, 42, 47, 1],
    [18, 19, 20, 26, 42, 1],
    [20, 21, 23, 32, 46, 10],
    [6, 12, 29, 32, 36, 8],
    [14, 15, 34, 37, 45, 2],
    [9, 15, 16, 20, 21, 1],
    [12, 13, 18, 25, 26, 4],
    [6, 13, 24, 39, 43, 8],
    [3, 6, 7, 34, 36, 7],
    [1, 4, 21, 35, 39, 5],
    [2, 6, 12, 16, 19, 3],
    [5, 15, 17, 25, 42, 7],
    [3, 20, 30, 47, 49, 7],
    [14, 18, 27, 34, 44, 6],
    [25, 38, 39, 40, 41, 7],
    [8, 20, 39, 47, 48, 1],
    [10, 13, 16, 22, 24, 7],
    [6, 8, 17, 24, 48, 10],
    [2, 21, 24, 31, 36, 6],
    [7, 19, 29, 38, 45, 8],
    [1, 9, 18, 33, 39, 2],
    [2, 21, 22, 46, 49, 9],
    [2, 6, 7, 6, 43, 5],
    [5, 12, 26, 36, 46, 4],
    [9, 12, 15, 17, 26, 8],
    [8, 28, 40, 41, 42, 2],
    [2, 15, 23, 28, 45, 7],
    [1, 22, 26, 31, 37, 5],
    [20, 32, 34, 47, 49, 1],
    [3, 22, 24, 32, 46, 5],
    [20, 30, 36, 40, 48, 8],
    [10, 12, 25, 37, 49, 2],
    [4, 5, 10, 13, 29, 1],
    [16, 18, 36, 45, 48, 10],
    [7, 25, 28, 29, 35, 2],
    [8, 12, 43, 46, 49, 8],
    [8, 18, 25, 27, 37, 8],
    [13, 17, 20, 26, 27, 4],
    [2, 27, 38, 43, 46, 3],
    [7, 8, 20, 30, 45, 10],
    [14, 22, 25, 37, 45, 3],
    [9, 22, 33, 42, 45, 3],
    [8, 16, 23, 35, 42, 2],
    [2, 13, 19, 23, 36, 3],
    [3, 15, 28, 36, 46, 2],
    [5, 30, 36, 40, 43, 1],
    [15, 34, 37, 40, 44, 8],
    [6, 13, 23, 24, 34, 4],
    [3, 33, 34, 36, 42, 2],
    [4, 12, 15, 23, 42, 1],
    [2, 13, 15, 31, 34, 8],
    [8, 9, 5,26, 27, 4],
    [2, 14, 30, 33, 47, 5],
    [9,25, 31, 32, 34, 5],
    [5, 20, 29, 32, 37, 9],
    [19, 41, 42, 43, 45, 2],
    [8, 22, 29, 37, 39, 10],
    [7, 11, 15, 19, 23, 4],
    [12, 15, 21, 29, 48, 6],
    [12, 28, 32, 38, 45, 9],
    [6, 11, 46, 48, 49, 2],
    [19, 22, 40, 45, 49, 2],
    [1, 9, 14, 36, 45, 3],
    [4, 6, 13, 16, 41, 10],
    [7, 11, 12, 36, 38, 6],
    [13, 16, 26, 28, 41, 8],
    [1, 7, 9, 32, 47, 1],
    [5, 26, 28, 29, 39, 10],
    [2, 3, 9, 30, 31, 10],
    [3, 15, 16, 30, 41, 9],
    [1, 12, 15, 30, 44, 1],
    [4, 7, 18, 19, 22, 10],
    [12, 16, 25, 48, 49, 10],
    [15, 28, 34, 36, 40, 10],
    [1, 27, 29, 37, 43, 7],
    [8, 10, 38, 41, 44, 2],
    [11, 12, 19, 25, 28, 4],
    [6, 10, 21, 30, 31, 1],
    [8, 9, 19, 26, 46, 9],
    [1, 9, 11, 13, 19, 8],
    [4, 17, 18, 41, 45, 2],
    [15, 30, 34, 41, 46, 2],
    [12, 20, 21, 29, 48, 3],
    [2, 7, 16, 22, 30, 1],
    [13, 23, 39, 45, 46, 7],
    [17, 19, 22, 25, 35, 6],
    [1, 2, 14, 36, 49, 9],
    [10, 18, 31, 34, 40, 10],
    [13, 20, 25, 40, 46, 7],
    [1, 16, 27, 32, 46, 1],
    [1, 8, 13, 30, 34, 4],
    [22, 31, 32, 34,38, 2],
    [12, 22, 30, 33, 35, 10],
    [3, 10, 22, 26, 40, 4],
    [3, 14, 25, 28, 47, 10],
    [3, 13, 22, 46, 49, 1],
    [6, 7, 25, 37, 47, 9],
    [4, 13, 14, 20, 27, 1],
    [6, 10, 15, 16, 24, 8],
    [9, 16, 23, 30, 32, 6],
    [5, 9, 12, 26, 42, 2],
    [21, 26, 27, 31, 40, 1],
    [3, 6, 15, 17, 40, 1],
    [23, 25, 33, 41, 48, 1],
    [14, 17, 25, 30, 44 ,3],
    [4, 13, 21, 27, 46, 4],
    [6, 26, 28, 37, 40, 8],
    [16, 19, 29, 37, 48, 1],
    [5, 17, 30, 35, 40, 6],
    [15, 32, 40, 42, 43, 4],
    [11, 27, 30, 48, 49, 8],
    [13, 28, 31, 40, 44, 6],
    [3, 4, 7, 15, 42, 4],
    [4, 15, 30, 33, 47, 10],
    [2, 11, 13, 27, 36, 10],
    [1, 7, 10, 33, 47, 10],
    [20, 31, 39, 45, 46, 10],
    [9, 23, 28, 35, 37, 7],
    [14, 15, 21, 34, 45, 5],
    [8, 25, 29, 34, 46, 7],
    [3, 4, 17, 22, 36, 6],
    [4, 8, 11, 27, 32, 10],
    [19, 24, 27, 35, 41, 9],
    [3, 13, 27, 44, 49, 9],
    [1, 9, 20, 39, 44, 9],
    [3, 6, 14, 31, 45, 9],
    [1, 11, 15, 47, 48, 7],
    [2, 7, 10, 40, 42, 2],
    [9, 12, 18, 23, 32, 9],
    [1, 4, 22, 33, 47, 1],
    [1, 18, 29, 37, 49, 4],
    [11, 17, 18, 28, 49, 7],
    [1, 12, 17, 31, 45, 7],
    [31, 33, 36, 37, 42, 3],
    [5, 11, 19, 35, 39, 9],
    [6, 9, 20, 41, 47, 9],
    [7, 12, 32, 42, 45, 6],
    [18, 26, 27, 31, 34, 8],
    [3, 8, 10, 14, 44, 2],
    [6, 10, 19, 32, 48, 5],
    [7, 8, 15, 19, 22, 5],
    [2, 8, 23, 35, 42, 7],
    [7, 9, 15, 18, 24, 10],
    [12, 34, 36, 42, 49, 10],
    [14, 16, 21, 26, 48, 3],
    [2, 3, 21, 30, 40, 4],
    [12, 19, 20, 27, 35, 4],
    [29, 38, 39, 42, 49, 3],
    [28, 29, 38, 43, 44, 3],
    [9, 12, 14, 16, 33, 2],
    [12, 19, 21, 26, 28, 2],
    [11, 16, 28, 32, 49, 10],
    [3, 4, 23, 28, 41, 8],
    [3, 10, 13, 25, 46, 5],
    [2, 37, 39, 44, 46, 4],
    [9, 13, 28, 40, 43, 3],
    [12, 24, 28, 36, 38, 3],
    [9, 24, 25, 31, 34, 9],
    [11, 17, 20, 28, 36, 10],
    [22, 33, 37, 42, 43, 4],
    [3, 8, 18, 25, 37, 6],
    [2, 8, 11, 40, 47, 7],
    [7, 9, 12, 29, 48, 4],
    [6, 9, 25, 34, 43, 5],
    [9, 12, 15, 44, 45, 1],
    [4, 16, 39, 43, 47, 5],
    [2, 25, 30, 42, 47, 10],
    [13, 17, 20, 23, 45, 8],
    [5, 15, 33, 41, 44, 10],
    [3, 22, 36, 40, 48, 5],
    [3, 11, 14, 18, 24, 10],
    [1, 23, 25, 41, 49, 2],
    [12, 13, 26, 35, 48, 1],
    [5, 34, 41, 43, 46, 5],
    [3, 13, 18, 42, 43, 9],
    [15, 17, 19, 29, 32, 10],
    [10, 15, 18, 26, 30, 7],
    [10, 15, 24, 45, 49, 2],
    [3, 19, 35, 42, 48, 10],
    [16, 29, 31, 33, 39, 2],
    [15, 31, 39, 46, 49, 4],
    [12, 17, 35, 44, 48, 8],
    [1, 11, 14, 32, 34, 9],
    [1, 11, 23, 34, 41, 9],
    [3, 7, 11, 29, 34, 4],
    [12, 20, 24, 33, 38, 2],
    [7, 10, 19, 26, 38, 8],
    [7, 8, 31, 32, 48, 5],
    [5, 15, 17, 20, 37, 2],
    [19, 35, 42, 45, 47, 2],
    [6, 14, 18, 33, 34, 6],
    [7, 10, 16, 35, 46, 5],
    [5, 18, 24, 38, 41, 7],
    [12, 25, 35, 40, 42, 6],
    [14, 18, 21, 39, 45, 8],
    [2, 5, 6, 14, 37, 1],
    [1, 3, 19, 34, 43, 3],
    [3, 24, 31, 35, 37, 4],
    [16, 22, 35, 41, 43, 7],
    [1, 5, 12, 13, 24, 9],
    [5, 20, 24, 28, 44, 6],
    [8, 20, 27, 33, 35, 2],
    [9, 15, 43, 45, 47, 9],
    [16, 21, 24, 34, 44, 7],
    [5, 6, 13, 21, 32, 3],
    [13, 16, 26, 31, 42, 2],
    [9, 12, 35, 38, 48, 5],
    [8, 27, 30, 34, 35, 5],
    [5, 15, 30, 44, 45, 5],
    [18, 21, 26, 32, 44, 10],
    [6, 10, 28, 32, 35, 9],
    [4, 18, 24, 41, 45, 6],
    [7, 11, 35, 39, 48 ,8],
    [5, 10, 19, 28, 31, 4],
    [13, 14, 22, 36, 40, 9],
    [3, 8, 16, 17, 47, 9],
    [1, 20, 30, 38, 48, 3],
    [7, 8, 21, 34, 43, 6],
    [3, 5, 25, 38, 49, 10],
    [1, 39, 41, 45, 49, 5],
    [11, 16, 23, 35, 39, 8],
    [1, 3, 8, 29, 35, 8],
    [6, 23, 32, 48, 49, 4],
    [6, 12, 41, 46, 47, 6],
    [11, 12, 15, 21, 22, 7],
    [6, 31, 35, 36, 43, 4],
    [8, 23, 27, 42, 46, 3],
    [4, 6, 15, 20, 37, 10],
    [2, 25, 35, 46, 47, 10],
    [6, 13, 27, 29, 43, 2],
    [2, 10, 12, 15, 38, 5],
    [9, 17, 24, 36, 45, 7],
    [19, 26, 27, 32, 34, 9],
    [18, 28, 30, 44, 49, 5],
    [2, 9, 13, 24, 46, 6],
    [2 ,5, 7, 23, 28, 5],
    [15, 19, 36, 45, 46, 4],
    [15, 23, 33, 45, 47, 7],
    [1, 19, 24, 28, 40, 8],
    [1, 3, 8, 38, 48, 1],
    [14, 23, 28, 34, 44, 5],
    [4, 14, 25, 34, 44, 7],
    [1, 2, 15, 30, 41, 9],
    [8, 9, 24, 31, 40, 7],
    [6, 23, 32, 38, 40, 10],
    [4, 7, 26, 38, 45, 2],
    [4, 25, 34, 44, 45, 7],
    [26, 28, 33, 44, 48, 4],
    [2, 4, 23, 30, 45, 5],
    [28, 29, 33, 37, 43, 1],
    [2, 7, 12, 25, 35, 10],
    [16, 25, 35, 38, 46, 8],
    [16, 20, 38, 40, 49, 2],
    [16, 24, 27, 31, 46, 1],
    [7, 17, 39,40, 44, 3],
    [13, 19, 32, 40, 46, 7],
    [16, 17, 20, 34, 48, 7],
    [14, 23, 32, 35, 39, 7],
    [7, 20, 23, 31, 40, 1],
    [7, 8, 26, 35, 36, 2],
    [12, 14, 26, 29, 39, 10],
    [18, 29, 35, 39, 49, 1],
    [4, 6, 7, 25, 32, 10],
    [3, 9, 12, 22, 37, 10],
    [5, 7, 15, 33, 44, 1],
    [1, 3, 12, 17, 20, 3],
    [10, 26, 38, 40, 45, 1],
    [4, 7, 20, 21, 49, 10],
    [3, 8, 24, 25, 49, 5],
    [3, 20, 29, 30, 35, 9],
    [1, 5, 27, 35, 40, 4],
    [24, 32, 35, 38, 44, 6],
    [9, 10, 15, 39, 45, 7],
    [5, 10, 22, 28, 34, 4],
    [11, 22, 32, 34, 39, 3],
    [22, 27, 36, 39, 42, 10],
    [2, 9, 39, 44, 46, 9],
    [1, 17, 21, 38, 46, 2],
    [5, 14, 16, 17, 29, 3],
    [4, 22, 34, 42, 48, 3],
    [11, 17, 37, 38, 39, 2],
    [9, 11, 15, 28, 35, 2],
    [3, 22, 37, 40, 41, 2],
    [6, 23, 28, 37, 38, 1],
    [5, 10, 32, 40, 45, 5],
    [1, 4, 23, 30, 38, 6],
    [2, 14, 21, 24, 38, 6],
    [13, 31, 43, 46, 47, 10],
    [7, 13, 24, 26, 42, 2],
    [15, 25, 39, 41, 47, 9],
    [17, 21, 29, 31, 47, 4],
    [5, 18, 29, 37, 49, 8],
    [3, 4, 14, 33, 49, 3],
    [7, 30, 31, 46, 48, 3],
    [1, 5, 10, 47, 49, 1],
    [8, 9, 24, 34, 37, 2],
    [10, 16, 25, 43, 44, 4],
    [4, 12, 18, 20, 26, 8],
    [20, 22, 32, 34, 46, 9],
    [16, 24, 26, 43, 47, 9],
    [24, 31, 34, 36, 37, 1],
    [2, 31, 40, 47, 49, 9],
    [10, 17, 23, 27, 40, 2],
    [14, 23, 27, 47, 48, 3],
    [1, 12, 28, 31, 32, 9],
    [11, 13, 21, 37, 44, 6],
    [31, 43, 44, 45, 46, 10],
    [4, 7, 10, 11, 28, 8],
    [26, 27, 33, 38, 39, 5],
    [5, 18, 20, 22, 23, 5],
    [6, 9, 17, 23, 42, 5],
    [2, 4, 22, 33, 35, 7],
    [12, 13, 14, 22, 38, 2],
    [7, 20, 21, 26, 27, 7],
    [24, 27, 30, 37, 45, 10],
    [26, 30, 41, 47, 48, 6],
    [1, 7, 12, 21, 41, 4],
    [14, 22, 23, 36, 45, 7],
    [4, 14, 21, 32, 33, 1],
    [4, 24, 29, 32, 44, 4],
    [2, 7, 23, 45, 46, 10],
    [6, 7, 9, 15, 33, 2],
    [7, 15, 23, 37, 38, 3],
    [12, 17, 30, 37, 41, 2],
    [8, 13, 20, 46, 47, 7],
    [5, 6, 21, 27, 47, 9],
    [1, 8, 13, 31, 43, 10],
    [8, 23, 31, 36, 42, 7],
    [9, 11, 20, 42, 44, 4],
    [4, 13, 33, 45, 46, 7],
    [9, 10, 33, 39, 47, 5],
    [4, 21, 27, 30, 41, 6],
    [29, 35, 36, 44, 46, 8],
    [3, 17, 18, 22, 32, 10],
    [3, 13, 15, 29, 40, 10],
    [6, 12, 20, 38, 48, 7],
    [10, 22, 23, 33, 36, 6],
    [6, 11, 15, 24, 28, 10],
    [10, 12, 16 ,26 ,34, 7],
    [5, 16, 21, 26, 48, 10],
    [10, 12, 34, 37, 40, 5],
    [2, 18, 20, 29, 39, 10],
    [5, 10, 26, 35, 46, 9],
    [33, 38, 41, 44, 49, 7],
    [1, 12, 24, 39, 49, 3],
    [5, 9, 11, 32, 49, 6],
    [5, 16, 21, 33, 47, 5],
    [8, 21, 25, 32, 41, 4],
    [8, 15, 27, 29, 41, 4],
    [1, 14, 26, 36, 37 ,3],
    [3, 4, 22, 43, 46, 6],
    [9, 21, 27, 36, 43, 2],
    [22, 28, 29, 30, 39, 3],
    [6, 12, 14, 15, 33, 8],
    [2, 6, 10, 17, 32, 5],
    [24, 32, 39, 40, 49, 1],
    [21, 22, 24, 32, 41, 2],
    [13, 15, 20, 26, 29, 5],
    [22, 28, 37, 40, 45, 10],
    [21, 31, 44, 46, 48, 1],
    [15, 18, 31, 37, 46, 3],
    [11, 24, 31, 38, 48, 9],
    [11, 28, 37, 40, 49, 4],
    [10, 25, 31, 32, 36, 8],
    [8, 25, 29, 42, 46, 9],
    [14, 16, 33, 38, 45, 10],
    [4, 7, 15, 38, 40, 2],
    [3, 17, 26, 30, 39, 8],
    [8, 27, 41, 43, 44, 6],
    [4, 5, 15, 22, 27, 9],
    [10, 13, 19, 30, 47, 8],
    [1, 20, 23, 26, 44, 4],
    [14, 34, 35, 41, 43, 9],
    [17, 22, 25, 42, 43, 10],
    [6, 17, 30, 32, 45, 4],
    [22, 33, 34, 36, 38, 5],
    [6, 14, 30, 36, 39, 5],
    [18, 21, 33, 48, 49, 7],
    [6, 12, 14, 20, 32, 8],
    [6, 21, 25, 37, 48, 10],
    [11, 20, 24, 41, 46, 1],
    [12, 22, 23, 25, 47, 1],
    [2, 10, 31, 38, 46, 8],
    [11, 34, 37, 38, 47, 8],
    [18, 19, 23, 36, 38, 1],
    [16, 26, 34, 42, 45, 9],
    [1, 16, 26, 28, 30, 4],
    [7, 15, 16, 29, 36, 6],
    [5, 18, 23, 34, 44, 5],
    [3, 18, 26, 46, 49, 6],
    [26, 30, 31, 35, 44, 4],
    [12, 25, 27, 28, 46, 4],
    [14, 24, 34, 39, 47, 8],
    [8, 12, 16, 19, 41, 5],
    [9, 17, 18, 42, 44, 8],
    [4, 36, 37, 40, 43, 6],
    [7,8, 34, 41, 42, 8],
    [12, 13, 26, 31, 39, 6],
    [9, 12, 31, 40, 41, 2],
    [7, 11, 32, 44, 48, 3],
    [2,4, 18, 19, 22, 3],
    [7, 31, 38, 39, 42, 10],
    [1, 26, 27, 43, 47, 6],
    [11, 12, 30, 43, 46, 9],
    [15, 16, 27, 41, 44, 9],
    [3, 31, 37, 43, 48, 10],
    [6, 10, 35, 36, 48, 9],
    [16, 22, 26, 35, 42, 4],
    [9 ,27, 35, 36, 41 ,6],
    [5, 15, 23, 37, 46, 10],
    [19, 20, 21, 43, 49, 10],
    [1, 7, 9, 26, 28, 3],
    [15, 19, 22, 29, 34, 3],
    [8, 20, 34, 41, 44, 2],
    [5, 7, 15, 19, 44, 1],
    [6, 8, 20, 35, 46, 9],
    [6, 13, 28, 33, 39, 10],
    [12, 26, 31, 37, 40, 3],
    [16, 18, 20, 35, 49, 1],
    [5, 9, 13, 14, 40, 1],
    [10, 12, 15, 31, 45, 5],
    [2, 9, 21, 38, 39, 2],
    [4, 22, 27, 30, 48 ,7],
    [4, 21, 24, 30, 40, 4],
    [3, 5 ,15, 33, 49, 8],
    [7, 12, 15, 27, 34 ,4],
    [3, 13, 31, 36, 40, 9],
    [30, 35, 41, 45 ,49, 3],
    [17, 24, 27, 32, 49, 7],
    [3, 18, 32, 34 ,44, 9],
    [8, 11, 43, 46, 48 ,9],
    [3, 9, 19, 26, 29, 8],
    [11, 13, 21 ,22, 31, 6],
    [2, 8 ,19, 29, 46 ,2],
    [4, 7, 12, 24, 25, 2],
    [10, 13, 22, 27, 49, 4],
    [4, 28 ,35, 42, 49, 7],
    [5, 6, 13, 21, 43, 4],
    [28, 37, 38, 43, 45 ,3],
    [6, 7 ,24 ,36 ,47 ,10],
    [20, 21 ,22, 36, 44, 10],
    [7, 24 ,42, 44, 46, 2],
    [6, 7, 17 ,22 ,46, 3],
    [1 ,3, 8 ,28, 29, 6],
    [5, 21, 34, 37 ,42, 10],
    [5, 22, 24, 31, 40, 9],
    [6, 25, 27, 32 ,37, 9],
    [2, 3 ,4, 15, 28, 5],
    [8, 11, 17, 31, 47, 6],
    [18, 29, 31, 36, 38 ,10],
    [8, 30, 31, 37, 38, 1],
    [3, 38, 42, 43, 46, 1],
    [8, 18, 37, 44, 46 ,2],
    [3, 32, 36 ,43, 45, 2],
    [2, 13, 19 ,33, 48 ,2],
    [6, 8, 31, 44, 48 ,9],
    [4, 8, 5, 28, 48, 1],
    [13, 24, 37, 38, 45, 6],
    [1, 3, 6, 16, 40, 1],
    [18, 21, 25, 44, 47, 10],
    [3, 14, 27, 44, 46, 6],
    [3, 22, 23, 35, 46, 9],
    [12, 19, 21, 40, 47 ,7],
    [2, 5, 9, 10, 29, 1],
    [2, 16, 24, 33, 41, 8],
    [6, 7, 11, 28, 34, 8],
    [6, 16, 25, 37, 45, 9],
    [3, 25, 26, 33, 34, 6],
    [3, 13, 25, 32, 47, 9],
    [4, 9, 32, 36, 44, 3],
    [1, 5, 20, 22, 42, 6],
    [7, 11, 29, 44, 47, 9],
    [2, 7, 9, 19, 45, 10],
    [3, 17, 23, 28, 41, 3],
    [3, 17, 23, 42, 47, 4],
    [7, 24, 29, 31, 47, 3],
    [9, 11, 19, 22, 36, 1],
    [12, 13, 17, 27, 44, 10],
    [6, 24, 35, 40, 41, 6],
    [8, 36, 41, 46 ,48, 6],
    [8, 11, 37, 44, 48, 6],
    [5, 25, 27, 34, 38, 7],
    [4, 10, 12, 15, 49, 6],
    [2, 8, 32, 34, 41, 6],
    [12, 26, 36, 41, 42, 7],
    [6, 31, 39, 45, 49, 4],
    [17, 27, 36, 44, 49, 1],
    [17, 30, 34, 37, 38, 1],
    [20, 23, 25, 27, 47, 6],
    [7, 11, 14, 26, 43, 7],
    [4, 8, 9, 15, 35, 8],
    [9, 16, 19, 35, 43, 4],
    [2, 12, 15, 22, 32, 8],
    [1, 2, 17, 38, 45, 2],
    [2, 22, 24, 27, 35, 5],
    [13, 18, 28, 38, 41, 1],
    [8, 10, 11, 16, 18, 5],
    [9, 22, 28, 37, 38, 10],
    [6, 15, 24, 34, 39, 4],
    [4, 14, 18, 27, 42, 3],
    [3, 18, 30, 45, 46, 3],
    [15, 29, 33, 38, 41, 2],
    [4, 10, 19, 22, 47 ,8],
    [20, 26, 33, 34, 42, 9],
    [8, 19, 24, 38, 40, 10],
    [3, 11, 13, 22, 30, 8],
    [8, 19, 38, 41, 49, 7],
    [4, 8, 14, 21, 47, 9],
    [4, 11, 29, 42, 43, 10],
    [10, 18, 19, 41, 47, 2],
    [3, 15, 24, 26, 37, 7],
    [19, 21, 36, 39, 49, 5],
    [29, 31, 34, 35, 41, 8],
    [6, 12, 13, 17, 22, 7],
    [9, 13, 17, 28 ,31, 10],
    [13, 15, 29, 33, 44, 4],
    [5, 9, 10, 19, 29, 8],
    [9, 15, 42, 44, 47, 10],
    [17, 21, 26, 31, 37, 10],
    [1, 17, 18, 21, 45, 9],
    [5, 9, 17, 33, 37, 4],
    [6, 23, 25, 27 ,44, 6],
    [3, 7, 13, 31, 49, 5],
    [1, 13, 19, 24, 48, 5],
    [11, 21, 22, 32, 40, 9],
    [5, 10, 25, 43, 48, 10],
    [14, 20, 22, 36, 44, 2],
    [17, 30, 32, 41, 42, 5],
    [1, 8, 17, 33, 46, 5],
    [7, 11, 12, 27, 49, 1],
    [11, 21, 32, 41, 47, 9],
    [19, 30, 31, 39, 49, 8],
    [5, 7, 24, 27, 41, 10],
    [13, 20, 31, 36, 38, 1],
    [1, 22, 34, 41, 42, 5],
    [2, 3, 31, 35, 40, 7],
    [3, 5, 31, 38, 39, 9],
    [10, 31, 36, 37, 44, 5],
    [10, 23, 29, 30, 49, 5],
    [6, 16, 17, 21, 41, 9],
    [2, 13, 34, 47, 48, 6],
    [9, 14, 23, 31, 45, 6],
    [17, 24, 39, 47, 48, 7],
    [4, 27, 38, 45, 48, 4],
    [9, 14, 20, 34, 35, 1],
    [14, 23, 27, 40, 46, 1],
    [9, 18, 26, 28, 29, 3],
    [2, 9, 25, 35, 47, 10],
    [1, 10, 14, 26, 31, 4],
    [1, 6, 12, 15, 20, 1],
    [5, 17, 44, 46, 49, 4],
    [11, 14, 28, 41, 43, 8],
    [7, 16, 33, 42, 47, 7],
    [17, 24, 26, 40, 43, 9],
    [10, 15, 16, 17, 37, 9],
    [5, 18, 26, 38, 41, 10],
    [5, 30, 42, 45, 48, 9],
    [9, 10, 14, 16, 29, 1],
    [31, 33, 38, 42, 43, 3],
    [9, 13, 22, 28, 35, 5],
    [2, 19, 25, 30, 43, 9],
    [7, 8, 12, 22, 33, 5],
    [4, 8, 12, 25, 45, 2],
    [15, 21, 33, 35, 48, 1],
    [7, 25, 28, 35, 48, 1],
    [9, 20, 23, 24, 28, 4],
    [19, 26, 32, 39, 42, 6],
    [7, 11, 18, 21, 42, 3],
    [26, 31, 42, 47, 48, 8],
    [6, 17, 19, 30, 49, 2],
    [5, 6, 9, 19, 22, 5],
    [9, 18, 31, 33, 36, 2],
    [2, 24, 26, 32, 49, 5],
    [6, 22, 33, 35, 44, 2],
    [4, 8, 31, 39, 49, 9],
    [5, 11, 23, 25, 33, 5],
    [16, 19, 38, 41, 46, 9],
    [27, 32, 33, 42, 46, 7],
    [17, 19, 23, 28, 49, 7],
    [5, 13, 23, 32, 49, 2],
    [12, 16, 21, 24, 46, 2],
    [20, 24, 29, 45, 48, 3],
    [14, 31, 35, 37, 44, 7],
    [15, 19, 22, 24, 46, 3],
    [3, 14, 21, 23, 47, 3],
    [4, 7, 11, 16, 17, 10],
    [15, 21, 23, 38, 39, 4],
    [4, 13, 31, 40, 45, 3],
    [18, 19, 22, 28, 37, 2],
    [5, 7, 11, 32, 33, 5],
    [4, 11, 13, 34, 35, 1],
    [1, 6, 39, 40, 48, 6],
    [3, 5, 15, 41, 42, 7],
    [3, 17, 30, 44, 47, 3],
    [1, 2, 11, 28, 38, 6],
    [4, 6, 35, 42, 49, 9],
    [15, 17, 22, 32, 46, 8],
    [23, 30, 42, 43, 48, 7],
    [9, 17, 18, 25, 38, 9],
    [7, 19, 39, 46, 47, 5],
    [15, 19, 24, 25, 45, 3],
    [6, 10, 15, 18, 48, 4],
    [4, 18, 20, 28, 38, 1],
    [8, 22, 26, 28, 42, 2],
    [11, 22, 34, 42, 43, 4],
    [4, 6, 12, 35, 44, 3],
    [2, 3, 24, 35, 46, 8],
    [6, 28, 32, 35, 40, 7],
    [9, 26, 30, 37, 48, 8],
    [2, 11, 30, 35, 42, 6],
    [13, 23, 27, 36, 44, 6],
    [5, 13, 14, 44, 47, 8],
    [20, 21, 29, 46, 47, 7],
    [1, 2, 6, 27, 39, 4],
    [8, 17, 31, 34, 36, 7],
    [5, 9, 21, 36, 39, 5],
    [8, 14, 24, 33, 38, 5],
    [10, 13, 20, 26, 46, 1],
    [2, 22, 26, 47, 49, 2],
    [5, 6, 25, 28, 32, 4],
    [9, 11, 20, 36, 47, 2],
    [2, 8, 22, 26, 46, 1],
    [7, 14, 29, 43, 44, 5],
    [12, 13, 16, 26, 44, 6],
    [2, 24, 26, 32, 36, 7],
    [5, 14, 16, 42, 44, 9],
    [6, 12, 29, 31, 44, 6],
    [9, 26, 30, 36, 42, 4],
    [3, 22, 23, 28, 29, 2],
    [14, 20, 39, 45, 47, 8],
    [10, 14, 20, 30, 35, 9],
    [19, 26, 27, 41, 46, 4],
    [4, 17, 38, 43, 49, 8],
    [3, 5, 17, 33, 34, 10],
    [29, 35, 39, 47, 48, 7],
    [10, 14, 15, 36, 48, 3],
    [8, 9, 15, 33, 39, 10],
    [9, 12, 22, 30, 43, 4],
    [5, 7, 25, 29, 47, 1],
    [11, 14, 19, 29, 41, 9],
    [6, 10, 13, 24, 49, 3],
    [28, 30, 40, 41, 43, 7],
    [5, 7, 9, 37, 41, 6],
    [1, 27, 33, 45, 47, 8],
    [1, 3, 16, 31, 48, 6],
    [1, 17, 19, 23, 42, 9],
    [1, 8, 41, 43, 48, 7],
    [6, 9, 16, 19, 26, 9],
    [7, 18, 23, 29, 35, 4],
    [2, 35, 39, 40, 42, 9],
    [3, 28, 41, 42, 48, 6],
    [12, 17, 21, 23, 37, 7],
    [22, 23, 26, 32, 35, 5],
    [24, 32, 34, 40, 45, 1],
    [5, 21, 28, 48, 49, 2],
    [7, 8, 16, 37, 42, 8],
    [10, 28, 29, 46, 48, 9],
    [4, 16, 23, 40, 44, 3],
    [28, 31, 38, 41, 43, 10],
    [5, 14, 38, 45, 46, 1],
    [5, 26, 33, 41, 42, 7],
    [4, 5, 24, 35, 37, 2],
    [10, 17, 30, 33, 49, 4],
    [21, 26, 39, 40, 42, 5],
    [5, 10, 19, 24, 37, 6],
    [6, 20, 30, 32, 45, 4],
    [9, 15, 20, 27, 47, 7],
    [4, 5, 24, 26, 39, 4],
    [16, 21, 40, 41, 46, 2],
    [7, 19, 39, 41, 44, 1],
    [4, 5, 25, 45, 48, 7],
    [17, 30, 38, 43, 47, 5],
    [15, 25, 37, 38, 49, 8],
    [7, 12, 31, 45, 47, 10],
    [6, 11, 21, 29, 30, 4],
    [7, 20, 31, 33, 49, 4],
    [16, 21, 22, 25, 36, 9],
    [6, 14, 30, 31, 45, 8],
    [7, 10, 12, 27, 41, 1],
    [7, 11, 17, 30, 36, 5],
    [12, 25, 26, 28, 42, 10],
    [13, 26, 30, 31, 38, 1],
    [1, 2, 12, 13, 33, 9],
    [8, 19, 22, 35, 46, 2],
    [11, 14, 16, 25, 32, 9],
    [2, 13, 14, 23, 48, 3],
    [16, 17, 29, 37, 44, 8],
    [10, 19, 26, 30, 49, 3],
    [9, 22, 31, 34, 43, 5],
    [4, 7, 11, 24, 32, 10],
    [12, 32, 34, 38, 48, 6],
    [8, 18, 24, 48, 49, 8],
    [15, 24, 36, 40, 45, 9],
    [7, 20, 32, 36, 37, 2],
    [19, 22, 23, 27, 48, 2],
    [5, 6, 7, 17, 23, 9],
    [10, 26, 35, 38, 39, 6],
    [3, 4, 17, 38, 48, 9],
    [1, 25, 33, 40, 48, 8],
    [1, 15, 24, 25, 34, 8],
    [10, 29, 38, 40, 44, 8],
    [8, 26, 30, 35, 40, 2],
    [11, 14, 28, 39, 42, 9],
    [7, 16, 17, 25, 48, 3],
    [2, 15, 18, 29, 44, 4],
    [33, 35, 38, 41, 44, 8],
    [4, 9, 22, 27, 28, 4],
    [7, 22, 23, 30, 37, 3],
    [6, 12, 15, 31, 44, 7],
    [10, 12, 29, 30, 49, 9],
    [10, 13, 19, 22, 35, 1],
    [13, 14, 25, 27, 28, 5],
    [6, 18, 24, 26, 29, 3],
    [23, 27, 42, 43, 44, 10],
    [1, 9, 16, 39, 42, 7],
    

    
    # Ajoutez autant de tirages que nécessaire
]

# Initialiser un compteur pour les numéros
compteur = collections.Counter()

# Compter la fréquence de chaque numéro
for tirage in tirages:
    compteur.update(tirage)

    # Afficher les numéros les plus fréquents
numeros_frequents = compteur.most_common()
print("Numéros les plus fréquents :")
for numero, freq in numeros_frequents:
    print(f"Numéro {numero}: {freq} fois")

# Obtenir les numéros les plus fréquents et les moins fréquents
numeros_frequents = compteur.most_common()
numeros_moins_frequents = compteur.most_common()[::-1]

# Filtrer les numéros de 1 à 49
numeros_frequents_1_49 = [numero for numero, freq in numeros_frequents if 1 <= numero <= 49]
numeros_moins_frequents_1_49 = [numero for numero, freq in numeros_moins_frequents if 1 <= numero <= 49]

# Trouver les numéros dans la plage de 1 à 10
frequents_1_10 = [numero for numero, freq in numeros_frequents if 1 <= numero <= 10]
moins_frequents_1_10 = [numero for numero, freq in numeros_moins_frequents if 1 <= numero <= 10]

# Fonction pour générer une combinaison
def generer_combinaison(numeros_base, numeros_1_10):
    combinaison = random.sample(numeros_base[:10], 5)  # Sélectionner aléatoirement 5 numéros parmi les 10 premiers
    combinaison.sort()  # Trier les 4 premiers numéros en ordre croissant
    combinaison.append(random.choice(numeros_1_10))  # Ajouter un numéro dans la plage 1 à 10
    return combinaison

# Fonction pour générer une combinaison mélangée
def generer_combinaison_melangee(numeros_frequents, numeros_moins_frequents, numeros_1_10):
    combinaison = random.sample(numeros_frequents[:10], 3) + random.sample(numeros_moins_frequents[:10], 2)
    combinaison.sort()  # Trier les 4 premiers numéros en ordre croissant
    combinaison.append(random.choice(numeros_1_10))  # Ajouter un numéro dans la plage 1 à 10
    return combinaison

# Générer plusieurs combinaisons potentielles
propositions_frequentes = [generer_combinaison(numeros_frequents_1_49, frequents_1_10) for _ in range(5)]
propositions_moins_frequentes = [generer_combinaison(numeros_moins_frequents_1_49, moins_frequents_1_10) for _ in range(5)]
propositions_melangees = [generer_combinaison_melangee(numeros_frequents_1_49, numeros_moins_frequents_1_49, frequents_1_10 + moins_frequents_1_10) for _ in range(5)]

print("Propositions basées sur les numéros les plus fréquents :")
for proposition in propositions_frequentes:
    print(proposition)

print("\nPropositions basées sur les numéros les moins fréquents :")
for proposition in propositions_moins_frequentes:
    print(proposition)

print("\nPropositions basées sur un mélange de numéros fréquents et moins fréquents :")
for proposition in propositions_melangees:
    print(proposition)