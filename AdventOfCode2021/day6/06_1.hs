import System.IO  
import Data.List.Split

main :: IO ()
main = do  
        handle <- openFile "06.txt" ReadMode
        contents <- hGetContents handle
        let ages = map (\age -> read age :: Int) (splitOn "," contents)
            ages_after = days ages 80
        print (length ages_after)
        hClose handle

isThereZero :: [Int] -> Int -> Int
isThereZero [] currentZeros = currentZeros
isThereZero ages currentZeros = 
    if head ages == 0
        then isThereZero (tail ages) (currentZeros + 1)
    else isThereZero (tail ages) currentZeros

replaceZero :: [Int] -> [Int]
replaceZero = map (\age -> if age == 0 then 7 else age)

decreaseByOne :: [Int] -> [Int]
decreaseByOne = map (\age -> age - 1)

day :: [Int] -> [Int]
day ages = 
    if isThereZero ages 0 > 0
        then day (replaceZero ages ++ replicate (isThereZero ages 0) 9)
    else decreaseByOne ages

days :: [Int] -> Int -> [Int]
days ages 0 = ages
days ages currentDay = days (day ages) (currentDay - 1)