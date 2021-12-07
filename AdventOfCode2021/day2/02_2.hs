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
        let result = calculatePosition list 0 0 0
        print (head result * head (tail result))

        
f :: [String] -> [[String]]
f = map words

calculateDirection:: [String] -> Int -> Int -> Int -> [Int]
calculateDirection (direction:value) depth horizontal aim
    | direction == "up" = [depth, horizontal, aim - read (head value)]
    | direction == "down" = [depth, horizontal, aim + read (head value)]
    | direction == "forward" = [depth + (aim * read (head value)), horizontal + read (head value), aim]

calculatePosition :: [[String]] -> Int -> Int -> Int -> [Int]

calculatePosition [] depth horizontal aim = [depth, horizontal]
calculatePosition (direction:directions) depth horizontal aim = calculatePosition directions (head result) (head (tail result)) (head (tail (tail result)))
        where result = calculateDirection direction depth horizontal aim

    


    