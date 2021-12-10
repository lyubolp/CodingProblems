import System.IO

main :: IO ()
main = do
        handle <- openFile "10.txt" ReadMode
        contents <- hGetContents handle
        let all_lines = lines contents
            corrupted_lines_scores = map (`checkBrackets` []) all_lines
        print all_lines
        print corrupted_lines_scores
        print (sum corrupted_lines_scores)
        hClose handle

checkSinglePairBrackets :: Char -> Char -> Bool
checkSinglePairBrackets '(' ')' = True
checkSinglePairBrackets '[' ']' = True
checkSinglePairBrackets '{' '}' = True
checkSinglePairBrackets '<' '>' = True
checkSinglePairBrackets _ _ = False

scoreIllegalBracket :: Char -> Int
scoreIllegalBracket ')' = 3
scoreIllegalBracket ']' = 57
scoreIllegalBracket '}' = 1197
scoreIllegalBracket '>' = 25137
scoreIllegalBracket _ = 0

checkBrackets :: String -> [Char] -> Int
checkBrackets "" stack = 0
checkBrackets (x:xs) stack
    | x == '(' = checkBrackets xs (stack ++ [x])
    | x == '[' = checkBrackets xs (stack ++ [x])
    | x == '{' = checkBrackets xs (stack ++ [x])
    | x == '<' = checkBrackets xs (stack ++ [x])
    | otherwise = 
        if checkSinglePairBrackets (last stack) x 
            then checkBrackets xs (take (length stack - 1) stack)
        else scoreIllegalBracket x