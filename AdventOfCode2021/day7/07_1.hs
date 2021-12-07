import System.IO
import Data.List.Split ( splitOn )
import Data.List ( sort )

main :: IO ()
main = do
        handle <- openFile "07.txt" ReadMode
        contents <- hGetContents handle
        let positions = sort (map (\age -> read age :: Int) (splitOn "," contents))
            mean = getMean positions
        print positions
        print mean
        print (getNeededFuel positions mean)
        hClose handle

average :: [Int] -> Int
average items = div (sum items) (length items)

getMean :: [Int] -> Int
getMean positions =
    if mod (length positions) 2 == 1
        then take (mean + 1) positions !! max 0 mean
    else average (drop (mean - 1) (take (mean + 1) positions))
        where mean = div (length positions) 2

getNeededFuel :: [Int] -> Int -> Int
getNeededFuel positons target = foldr (\item acc -> acc + abs (item - target)) 0 positons