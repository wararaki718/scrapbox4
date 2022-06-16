module Lib
    ( someFunc
    ) where

import Sample


someFunc :: IO ()
someFunc = do
    let result = removeNonUppercase "This is a Pen."
    print result

    let result2 = addThree 1 2 3
    print result2

    let result3 = factorial 50
    print result3

    let result4 = circumference 4.0
    print result4

    let result5 = circumference' 4.0
    print result5

    let result6 = show 3
    print result6

    let result7 = show True
    print result7

    let result8 = "abc" `compare` "ghf"
    print result8

    let result9 = read "5" :: Int
    print result9

    let result10 = read "5" :: Float
    print result10

    let result11 = (read "5" :: Float) * 4
    print result11

    let result12 = read "[1,2,3,4]" :: [Int]
    print result12

    let result13 = read "(3, 'a')" :: (Int, Char)
    print result13

    let result14 = [read "True", True, False]
    print result14

    let result15 = ['a' .. 'e']
    print result15

    let result16 = [LT .. GT]
    print result16

    let result17 = [3 .. 5]
    print result17

    let result18 = succ 'B'
    print result18

    let result19 = minBound :: Int
    print result19

    let result20 = maxBound :: Char
    print result20

    let result21 = maxBound :: Bool
    print result21

    let result22 = minBound :: Bool
    print result22

    let result23 = maxBound :: (Bool, Int, Char)
    print result23

    let result24 = 20 :: Int
    print result24

    let result25 = 20 :: Integer
    print result25

    let result26 = 20 :: Float
    print result26

    let result27 = 20 :: Double
    print result27

    let result28 = fromIntegral (length [1, 2, 3, 4]) + 3.2
    print result28
