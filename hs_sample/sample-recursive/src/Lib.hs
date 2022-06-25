module Lib
    ( someFunc
    ) where

import Sample

someFunc :: IO ()
someFunc = do
    let result = maximum' [1, 4, 10, 3, 9, 23, 6, 13, 19]
    print result

    let result2 = replicate' 2 5
    print result2

    let result3 = take' 3 [5, 4, 3, 2, 1]
    print result3

    let result4 = reverse' [1, 2, 3]
    print result4

    let result5 = take' 3 (repeat' 5)
    print result5

    let result6 = zip' [1, 2, 3] [4, 5, 6]
    print result6

    let result7 = elem' 3 [1, 2, 3 ,4]
    print result7

    print "DONE"
