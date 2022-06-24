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

    let result10 = bmiTell 10
    print result10

    let result11 = bmiTell 20
    print result11

    let result12 = bmiTell' 85 1.90
    print result12

    let result13 = bmiTell2 85 1.90
    print result13

    let result14 = bmiTell2' 85 1.20
    print result14

    let result15 = calcBmis [(40, 1.20), (100, 1.50)]
    print result15

    let result16 = cylinder 5 2
    print result16

    let result17 = calcBmis' [(40, 1.20), (100, 1.50)]
    print result17

    let result18 = head'' [100, 20, 130, 90]
    print result18
