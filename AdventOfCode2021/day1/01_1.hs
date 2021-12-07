import System.IO  
import Control.Monad

main :: IO ()
main = do  
        let list = []
        handle <- openFile "01_1.txt" ReadMode
        contents <- hGetContents handle
        let singlewords = words contents
            list = f singlewords
        print list
        hClose handle
        print (length (filter (== True) (incrementMap list)))
        
f :: [String] -> [Int]
f = map read

incrementMap :: [Int] -> [Bool]
incrementMap [] = [False]
incrementMap [x] = [False]
incrementMap list = [head list < head (tail list)] ++ incrementMap (tail list)
