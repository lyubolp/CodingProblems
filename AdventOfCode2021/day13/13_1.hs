import System.IO
import Data.List.Split ( splitOn )
import Data.List (nub)

main :: IO ()
main = do
        handle <- openFile "13.txt" ReadMode
        contents <- hGetContents handle
        let all_lines = lines contents
            empty_line_location = findEmptyLine all_lines
            coordinates = handleCoordinates (take empty_line_location all_lines)
            folds = map handleFold (drop (empty_line_location + 1) all_lines)
            firstFold = head folds
            afterFirstFold = nub (map (uncurry foldCoordinate firstFold) coordinates)

        print (length afterFirstFold)
        hClose handle

handleFold :: String -> (String, Int)
handleFold input = (head parsed,  read (head (tail parsed)))
    where parsed = splitOn "=" (splitOn " " input !! 2)

handleCoordinates :: [String] -> [[Int]]
handleCoordinates = map (map read . splitOn ",")

foldCoordinate :: String -> Int -> [Int] -> [Int]
foldCoordinate "x" by coordinate = 
    if x >= by then [2*by - x, y]
    else [x, y]
    where x = head coordinate
          y = head (tail coordinate)

foldCoordinate "y" by coordinate = 
    if y >= by
        then [x, 2*by - y]
    else [x, y]
    where x = head coordinate
          y = head (tail coordinate)
foldCoordinate _ _ coordinate = coordinate


findEmptyLine :: [String] -> Int
findEmptyLine lines =
    if head lines == ""
        then 0
    else 1 + findEmptyLine (tail lines)