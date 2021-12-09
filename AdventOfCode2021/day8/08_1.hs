import System.IO
import Data.List.Split ( splitOn )
import Data.List ( sort )
import Data.Text ( strip )

main :: IO ()
main = do
        handle <- openFile "08.txt" ReadMode
        contents <- hGetContents handle
        let input = map (tail . splitOn "|") (lines contents)
            digits = concatMap (words . head) input
            uniqueDigits = filterDigits digits
        print (length uniqueDigits)
        hClose handle

isDigitUnique :: String -> Bool
isDigitUnique digit 
    | length digit == 2 = True
    | length digit == 4 = True
    | length digit == 3 = True
    | length digit == 7 = True
    | otherwise = False

filterDigits :: [String] -> [String]
filterDigits = filter isDigitUnique
