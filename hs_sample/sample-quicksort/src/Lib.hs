module Lib
    ( someFunc
    ) where

import Sort

someFunc :: IO ()
someFunc = do
    let result = quicksort [4, 5, 3, 1, 2, 8, 7, 9, 6]
    print result
