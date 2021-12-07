import System.IO  
import Control.Monad

main :: IO ()
main = do  
        let list = []
        handle <- openFile "02_1.txt" ReadMode
        contents <- hGetContents handle
        let splitByLines = lines contents
            list = f splitByLines
        print list
        hClose handle
        let result = calculatePosition list 0 0
        print (head result * head (tail result))

        
f :: [String] -> [[String]]
f = map words

calculateDirection:: [String] -> Int -> Int -> [Int]
calculateDirection (direction:value) depth horizontal
    | direction == "up" = [depth - read (head value), horizontal]
    | direction == "down" = [depth + read (head value), horizontal]
    | direction == "forward" = [depth, horizontal + read (head value)]

calculatePosition :: [[String]] -> Int -> Int -> [Int]

calculatePosition [] depth horizontal = [depth, horizontal]
calculatePosition (direction:directions) depth horizontal = calculatePosition directions (head result) (head (tail result))
        where result = calculateDirection direction depth horizontal

    


    