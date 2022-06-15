module Lib
    ( someFunc
    ) where

import Baby

someFunc :: IO ()
someFunc = do
    let result = 2 + 15
    print result

    let result2 = 49 * 100
    print result2

    let result3 = 1892 - 1472
    print result3

    let result4 = 100 - (9*9)
    print result4

    let result5 = True && False
    print result5

    let result6 = False || True
    print result6

    let result7 = not result5
    print result7

    let result8 = 5 == 5
    print result8

    let result9 = 5 /= 5
    print(result9)

    let result10 = min 9 10
    print result10

    let result11 = max 10 100
    print result11

    let result12 = succ 9 * 10
    print result12

    let result13 = succ 8 * 10
    print result13

    let result14 = div 92 10
    print result14

    let result15 = 92 / 10
    print result15

    let result16 = doubleMe 9
    print result16

    let result17 = doubleMe 1.5
    print result17

    let result18 = doubleUs 4 9
    print(result18)

    let result19 = doubleUs 2.3 34.2
    print result19

    let result20 = doubleUs 28 88 + doubleMe 123
    print result20

    let result21 = doubleSmallNumber 50
    print result21

    let result22 = doubleSmallNumber 101
    print result22

    let result23 = doubleSmallNumber' 50
    print result23

    let result24 = doubleSmallNumber' 101
    print result24

    let lostNumbers = [4, 8, 15, 16, 23, 42]
    print lostNumbers

    let result26 = [1, 2, 3] ++ [8, 9, 10]
    print result26

    let result27 = "hello" ++ "world"
    print result27

    let result28 = 'A':" small cat"
    print result28

    let result29 = 5 : [1, 2, 3]
    print result29

    let result30 = "hello" !! 2
    print result30

    let result31 = [1, 2, 3, 4, 5] !! 1
    print result31

    let b = [[1, 2, 3, 4], [5, 3, 3, 3], [1, 2, 2, 3, 4], [1, 2, 3]]
    print b

    let c = b ++ [[1, 1, 1, 1]]
    print c

    let d = [6, 6, 6] : b
    print d

    let e = b !! 2
    print e

    let result32 = [3, 2, 1] > [2, 1, 0]
    print result32

    let result33 = [3, 2, 1] > [2, 10, 11]
    print result33
    
    let result34 = [3, 4, 2] > [2, 4]
    print result34

    let result35 = [3, 4] > [2, 1, 0]
    print result35

    let a = [5, 4, 3, 2, 1]
    let result36 = head a
    print result36

    let result37 = tail a
    print result37

    let result38 = last a
    print result38

    let result39 = init a
    print result39

    let result40 = length a
    print result40

    let result41 = null a
    print result41

    let result42 = null []
    print result42

    let result43 = reverse a
    print result43

    let result44 = take 3 a
    print result44

    let result45 = take 0 a
    print result45

    let result46 = drop 3 a
    print result46

    let result47 = maximum a
    print result47

    let result48 = minimum a
    print result48

    let result49 = sum a
    print result49

    let result50 = product a
    print result50

    let result51 = 3 `elem` a
    print result51

    let result52 = [1..5]
    print result52
    
    let result53 = ['a'..'z']
    print result53

    let result54 = [2, 4..10]
    print result54

    let result55 = take 24 [13, 26..]
    print result55

    let result56 = take 10 (cycle [1, 2, 3])
    print result56

    let result57 = take 10 (repeat 5)
    print result57

    let result58 = replicate 3 10
    print result58

    let result59 = [x*2 | x <- [1..10]]
    print result59

    let result60 = [x*2 | x <- [1..10], x*2 >= 12]
    print result60

    let result61 = [x | x <- [50..100], x `mod` 7 == 3]
    print result61

    let result62 = boomBangs [7..13]
    print result62

    let result63 = [x | x <- [10..20], x /= 13, x /= 15, x /= 19]
    print result63

    let result64 = [x+y | x <- [1, 2, 3], y <- [10, 100, 1000]]
    print result64

    let result65 = (1, 3)
    print result65

    let result66 = (1, 2, 3)
    print result66

    let result67 = (1, 'a', "hello")
    print result67

    let f = (8, 11)
    let result68 = fst f
    print result68

    let result69 = snd f
    print result69

    let result70 = zip [1..5] ['a'..'e']
    print result70

    let result71 = zip [1..10] ['a'..'z']
    print result71

    let result72 = zip [1..] ['a'..'g']
    print result72

    let rightTriangles = [(a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2, a+b+c == 24]
    let result73 = rightTriangles
    print rightTriangles
