log2 :: Int -> Int
log2 1 = 0
log2 x = log2(x `div` 2) + 1


combineList :: Int -> Int -> [[Int]]
combineList x 0 = [[0..(x-1)]]
combineList x y = (take y [[(y)..(x-1)]])++(take y(combineList x (y-1))


