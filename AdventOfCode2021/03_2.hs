import System.IO  
import Control.Monad
import Data.Char
import Data.Vector.Generic (headM)

main :: IO ()
main = do  
        handle <- openFile "03.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = words contents
        let mostCommon = convertToBinary (filterOut singlewords 0 countMostCommon)
        let leastCommon = convertToBinary (filterOut singlewords 0 countLeastCommon)
        print mostCommon
        print leastCommon
        print (mostCommon * leastCommon)
        hClose handle

filterOut :: [String] -> Int -> (String -> Int -> Int -> Char) -> String
filterOut [] _ _ = ""
filterOut [x] _ _ = x
filterOut entries bit f = filterOut (filter (\entry -> getNthBit entry bit == mostCommonElement) entries) (bit + 1) f
    where mostCommonElement = f (getNthBits entries bit) 0 0

getNthBit :: String -> Int -> Char
getNthBit entry 0 = head entry
getNthBit entry n = getNthBit (tail entry) (n - 1)

getNthBits :: [String] -> Int -> [Char]
getNthBits entries 0 = map head entries
getNthBits entries n = getNthBits (map tail entries) (n- 1)

countMostCommon :: String -> Int -> Int -> Char
countMostCommon [] zeros ones = if zeros > ones then '0' else '1'
countMostCommon items zeros ones = 
    if head items == '1'
        then countMostCommon (tail items) zeros (ones + 1)
    else countMostCommon (tail items) (zeros + 1) ones

countLeastCommon :: String -> Int -> Int -> Char 
countLeastCommon [] zeros ones = if zeros <= ones then '0' else '1'
countLeastCommon items zeros ones = 
    if head items == '1'
        then countLeastCommon (tail items) zeros (ones + 1)
    else countLeastCommon (tail items) (zeros + 1) ones


convertToBinary :: String -> Int
convertToBinary "" = 0
convertToBinary num = (Data.Char.ord (head num) - Data.Char.ord '0') * 2 ^ (length num - 1)  + convertToBinary (tail num)