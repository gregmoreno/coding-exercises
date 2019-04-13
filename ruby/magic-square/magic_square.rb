#!/bin/ruby

# https://www.hackerrank.com/challenges/magic-square-forming/problem
# We define a magic square to be an  matrix of distinct positive
# integers from  to  where the sum of any row, column, or diagonal of
# length  is always equal to the same number: the magic constant.
# You will be given a  matrix  of integers in the inclusive range.
# We can convert any digit  to any other digit  in the range  at
# cost of. Given , convert it into a magic square at minimal cost.
# Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in
# the inclusive range .

# Assumes a 3x3 input for now.
# More info about magic squares https://en.wikipedia.org/wiki/Magic_square

# Algorithm
#
# 1. Form all magic squares
# 2. For every magic square, calculate difference with input matrix
# 3  Min amount wins

def create_magic_squares(size)
  [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
  ]
end

def calculate_cost(size, matrix1, matrix2)
  cost = 0

  0.upto(size - 1) do |i|
    0.upto(size - 1) do |j|
      cost += (matrix1[i][j] - matrix2[i][j]).abs
    end
  end

  cost
end

def form_magic_square(matrix, size)
  squares = create_magic_squares(size)

  cost = 100 # some high enough number to compare with
  squares.each do |square|
    cost = [cost, calculate_cost(size, square, matrix)].min
  end

  cost
end


size = 3
matrix = Array.new(size)

size.times do |i|
  matrix[i] = gets.rstrip.split.map(&:to_i)
end

# result shows the cost of the transformation
result = form_magic_square(matrix, size)
puts result

