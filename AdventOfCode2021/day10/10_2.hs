import System.IO
import Data.List ( sort )

main :: IO ()
main = do
        handle <- openFile "10.txt" ReadMode
        contents <- hGetContents handle
        let all_lines = lines contents
            incomplete_lines = filter (\line -> checkBrackets line [] /= []) all_lines
            brackets_left = map (`checkBrackets` []) incomplete_lines
            brackets_to_add = map reverseStack brackets_left
            brackets_scores = sort (map scoreMissingBrackets brackets_to_add)
        print (getMean brackets_scores)
        hClose handle

average :: [Int] -> Int
average items = div (sum items) (length items)

getMean :: [Int] -> Int
getMean positions =
    if mod (length positions) 2 == 1
        then take (mean + 1) positions !! max 0 mean
    else average (drop (mean - 1) (take (mean + 1) positions))
        where mean = div (length positions) 2

checkSinglePairBrackets :: Char -> Char -> Bool
checkSinglePairBrackets '(' ')' = True
checkSinglePairBrackets '[' ']' = True
checkSinglePairBrackets '{' '}' = True
checkSinglePairBrackets '<' '>' = True
checkSinglePairBrackets _ _ = False

scoreMissingBracket :: Char -> Int
scoreMissingBracket ')' = 1
scoreMissingBracket ']' = 2
scoreMissingBracket '}' = 3
scoreMissingBracket '>' = 4
scoreMissingBracket _ = 0

scoreMissingBrackets :: [Char] -> Int
scoreMissingBrackets = foldl (\acc item -> (acc * 5) + scoreMissingBracket item) 0

reverseBracket :: Char -> Char
reverseBracket '(' = ')'
reverseBracket '[' = ']'
reverseBracket '{' = '}'
reverseBracket '<' = '>'
reverseBracket _ = ' '


reverseStack :: [Char] -> [Char]
reverseStack stack = reverse (map reverseBracket stack)

checkBrackets :: String -> [Char] -> [Char]
checkBrackets "" stack = stack
checkBrackets (x:xs) stack
    | x == '(' = checkBrackets xs (stack ++ [x])
    | x == '[' = checkBrackets xs (stack ++ [x])
    | x == '{' = checkBrackets xs (stack ++ [x])
    | x == '<' = checkBrackets xs (stack ++ [x])
    | otherwise =
        if checkSinglePairBrackets (last stack) x
            then checkBrackets xs (take (length stack - 1) stack)
        else []