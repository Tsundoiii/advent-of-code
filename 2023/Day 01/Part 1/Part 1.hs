import Data.Char
import System.IO

headLast :: [Char] -> [Char]
headLast s = [head s, last s]

firstLast :: [[Char]] -> [[Char]]
firstLast = map headLast

main = do
  input <- readFile "input.txt"
  let digitFilter = filter isDigit
  let digits = map digitFilter

  print $ sum $ (map read $ firstLast $ digits $ lines input :: [Integer])