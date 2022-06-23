module Lib
    ( someFunc
    ) where

import Sample

someFunc :: IO ()
someFunc = do
    let result = lucky 5
    print result
    
    let result1 = lucky 7
    print result1

    let result2 = sayMe 1
    print result2

    let result3 = sayMe 8
    print result3

    let result4 = factorial 5
    print result4

    let result5 = addVectors (1, 2) (3, 4)
    print result5

    let result6 = addList [(1, 3), (3, 4), (5, 9)]
    print result6

    let result7 = head' [4, 5, 6]
    print result7

    let result8 = firstLetter "hello"
    print result8

    let result9 = firstLetter ""
    print result9
