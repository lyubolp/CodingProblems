import System.IO  
import Control.Monad
import Data.Vector.Generic (headM)

main :: IO ()
main = do  
        handle <- openFile "03.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = words contents
        let columns = getColumns singlewords
        let count = map (\x -> countMostCommon x 0 0) columns
        let gamma_rate = convertToBinary count
        let epsilon_rate = convertToBinary (map (\x -> if x == 0 then 1 else 0) count)
        print (gamma_rate * epsilon_rate)
        hClose handle

getFirstBit :: [String] -> [String]
getFirstBit [] = []
getFirstBit items = [map head items]

removeFirstBit :: [String] -> [String]
removeFirstBit [] = []
removeFirstBit items = map tail items

getColumns :: [String] -> [String]
getColumns [] = []
getColumns ("":xs) = []
getColumns items = getFirstBit items ++ getColumns (removeFirstBit items)

countMostCommon :: String -> Int -> Int -> Int
countMostCommon [] zeros ones = if zeros > ones then 0 else 1
countMostCommon items zeros ones = 
    if head items == '1'
        then countMostCommon (tail items) zeros (ones + 1)
    else countMostCommon (tail items) (zeros + 1) ones

convertToBinary :: [Int] -> Int
convertToBinary [] = 0
convertToBinary nums = head nums * 2 ^ (length  nums - 1)  + convertToBinary (tail nums)