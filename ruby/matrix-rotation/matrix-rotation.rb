# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
# You are given a 2D matrix of dimension M x N and a positive integer R.
# You have to rotate the matrix r times and print the resultant matrix.
# Rotation should be in anti-clockwise direction.
#
# The approach is to treat the matrix as layers like peeling an onion. You start
# with the edges and work your way inside until the last layer. Note that M and
# N can be different values.
#
# My first naive implementation rotates each layer R times and took around 266 seconds
# to complete a 142x70 matrix 6045 times. This implemenation failed most of the tests
# in HackerRank :(.
#
# My first optimization factors in the fact that rotating a matrix P times can bring the
# matrix back to its original form. Say you have a 2x2, rotating it 4 times is the same
# as the original matrix. Rotating a 2x2 matrix 101 times is the same as rotating it
# just 1 time.
#
# To calculate, P = 2 * (M + N - 2)
#
# Another optimization is to re-calculate the required rotations as you iterate inside each layer.
# For example, given a 4x5 and R=20, the first layer requires only just 6 rotations. The next layer
# becomes a 2x3 matrix, and does not need to be rotated.
#
# This optimization reduced the execution time to 6.9 seconds which is a huge improvement but
# still not enough to satisfy the HackerRank gods :)
#
# The next optimization is about placing the value in the right location after the rotation.
# The original naive implementation just loops through the values in the edges of the layer
# and copies them 1 position (i.e. 1 rotation) at a time. So for a given R=6, the implementation
# loops through the values 6 times which is unnecessary. Following our example, you do not
# need to loop 6 times - you only need to copy the 6th value from the current location.
#
# After this optimization, execution time was down to 0.08 seconds!


# Assumes rotate left.
#
# Approach:
#   1. Build an array of values from edges in the following order: top, right, bottom, left
#   2. Rotate the values by shifting the array equal to passed `rotations` parameter.
#   3. Project the rotated values to the matrix in the same order
def rotate(matrix, start_row, start_col, end_row, end_col, rotations)
  edge = []

  # top
  edge.concat start_col.upto(end_col - 1).collect { |c| matrix[start_row][c] }
  # right
  edge.concat start_row.upto(end_row - 1).collect { |r| matrix[r][end_col] }
  # bottom
  edge.concat end_col.downto(start_col + 1).collect { |c| matrix[end_row][c] }
  # left
  edge.concat end_row.downto(start_row + 1).collect { |r| matrix[r][start_col] }

  rotated = edge[rotations..-1] + edge[0, rotations]

  # top
  i = 0
  start_col.upto(end_col - 1) do |c|
    matrix[start_row][c] = rotated[i]
    i += 1
  end

  # right
  start_row.upto(end_row - 1) do |r|
    matrix[r][end_col] = rotated[i]
    i += 1
  end

  # bottom
  end_col.downto(start_col + 1) do |c|
    matrix[end_row][c] = rotated[i]
    i += 1
  end

  # left
  end_row.downto(start_row + 1) do |r|
    matrix[r][start_col] = rotated[i]
    i += 1
  end

  matrix
end

def matrix_rotation(matrix, m, n, r)
  # number of layers inside the matrix
  layers = [(m / 2), (n / 2)].min

  start_row = 0
  start_col = 0
  end_row = m - 1
  end_col = n - 1

  layers.times do
    # There exists a P rotations that will just result in the original matrix.
    # Then, calculate the actual required rotations
    p = 2 * (end_row - start_row + end_col - start_col)
    rotations = r % p

    rotate(matrix, start_row, start_col, end_row, end_col, rotations)

    # Next layer, i.e. move inside the matrix
    start_row += 1
    start_col += 1
    end_row -= 1
    end_col -= 1
  end

  matrix
end


m, n, r = gets.rstrip.split.map(&:to_i)

matrix = Array.new(m)
m.times do |i|
  matrix[i] = gets.rstrip.split.map(&:to_i)
end

result = matrix_rotation(matrix, m, n, r)
result.each do |row|
  puts row.join(' ')
end

