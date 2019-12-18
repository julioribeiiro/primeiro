mult4 :: Int -> Int
mult4 x = x^2

allEqual :: Int -> Int -> Int -> Bool
allEqual n m p = (n == p) && (m == p)

max2 :: Int -> Int -> Int
max2 n m | n>=m = n
         | otherwise = m

max3 :: Int -> Int -> Int -> Int
max3 a b c | a>b && a>c = a
           | b>a && b>c = b
           | otherwise = c

fac :: Double -> Double
fac 0 = 1
fac n = n * fac(n - 1)

power :: Int -> Int -> Int
power _ 0 = 1
power x y = x * power x (y-1)

doubleList :: [Int] -> [Int]
doubleList as | as == [] = []      
              | otherwise = (head as)*2 : doubleList (tail as)

dobroLista :: [Int] -> [Int]
dobroLista [] = []
dobroLista (a:as) = a*2 : dobroLista as

maxList :: [Int] -> Int
maxList [a] = a
maxList [] = 0
maxList (a:as) | a > head as = maxList (a:tail as)
               | otherwise = maxList(as)

maxList' :: [Int] -> [Int]
maxList' [a] = [a]
maxList' [] = []
maxList' (a:as) | a > head as = maxList'(a:tail as)
                | otherwise = maxList'(as)

maxLista :: [Int] -> [Int]
maxLista [] = []
maxLista [a] = [a]
maxLista (a:as) | a > head (maxLista as) = [a]
                | otherwise = maxLista(as)


addPair' :: (Int, Int) -> Int
addPair' (x, y) = x+y

addPair :: [(Int, Int)] -> [Int]
addPair [] = []
addPair (a:as) = addPair'(a) : addPair(as)


digits :: String -> String
digits [] = []
digits (a:as) | a `elem` "0123456789" = a : digits(as)
              | otherwise = digits(as)


zip2 :: [Int] -> [Int] -> [(Int, Int)]
zip2 [] [] = []
zip2 (a:as) (b:bs) = (a,b) : (zip2 as bs)



primeiro :: [(a,b)] -> [a]
primeiro [] = []
primeiro (x:xs) = (\(t,f) -> t) x : primeiro xs


hipo :: Float -> Float -> Float
hipo a b = sqrt (a^2 + b^2)


ordenaTripla :: (Int, Int, Int) -> (Int, Int, Int)
ordenaTripla (a, b, c) | a > b && a > c && b > c = (a, b, c)
                       | a > b && a > c && b < c = (a, c, b)
                       | b > a && b > c && a > c = (b, a, c)
                       | b > a && b > c && a < c = (b, c, a)
                       | c > a && c > b && a > b = (c, a, b)
                       | c > a && c > b && a < b = (c, b, a)


pegaPares :: [Int] -> [Int]
pegaPares [] = []
pegaPares (a:as) | a `mod` 2 == 0 = a : pegaPares as 
                 | otherwise = pegaPares as


pegaImpares :: [Int] -> Int -> [Int]
pegaImpares [] _ = []
pegaImpares (a:as) x | a `mod` 2 /= 0 = a*x : pegaImpares as x
                     | otherwise = pegaImpares as x


splitAndMult :: [Int] -> Int -> ([Int], [Int])
splitAndMult a x = (pegaPares a, pegaImpares a x)




--1 CONCATENAR TODAS AS LISTAS DA FUNCAO
--2 CRIAR SUBLISTA COM TODOS OS NUMEROS QUE ESTAO NA LISTA COMPLETA
--3 CRIAR FUNCAO QUE CONTA QUANTAS VEZES CADA NUMERO ESTA NA LISTA COMPLETA

juntaListas :: [[Int]] -> [Int]
juntaListas [] = []
juntaListas (a:as) = a ++ juntaListas as


numExiste :: [Int] -> Int -> Bool
numExiste [] _ = False
numExiste y x | x == head y = True
              | otherwise = numExiste (tail y) x



--CRIA UMA LISTA SEM NUMEROS DUPLICADOS
tiraDuplicados :: [Int] -> [Int]
tiraDuplicados [] = []
tiraDuplicados (a:as) | numExiste as a == False = a : tiraDuplicados as
                      | otherwise = tiraDuplicados as



numerosRepetidos :: Int -> [Int] -> Int
numerosRepetidos _ [] = 0
numerosRepetidos x (a:as) | a == x = 1 + numerosRepetidos x as
                          | otherwise = numerosRepetidos x as


--PRIMEIRO JUNTA TODAS AS LISTAS EM UMA UNICA
--PARA CADA ELEMENTO NAO REPETIDO USASSE A FUNCAO NUMEROS REPETIDOS
--RETORNA O NUMERO E A QUANTIDADE DE VEZES QUE ELE FOI ENCONTRADO


recebeLista :: [Int] -> [Int] -> [(Int, Int)]
recebeLista _ [] = []
recebeLista x (y:ys) = (y, numerosRepetidos y x) : recebeLista x ys



group' :: [[Int]] -> [(Int, Int)]
group' x = recebeLista (juntaListas x) (tiraDuplicados (juntaListas x))
--group x = (head (tiraDuplicados(juntaListas x)), numerosRepetidos (head (tiraDuplicados (juntaListas x))) (juntaListas x))


--4.
--Criar uma funcao que retorna os 2 primeiros elementos
--Criar uma funcao que retorna a lista sem os 2 primeiros elementos
--Funcao que retorna o penultimo elemento da lista
--




doisPrimeiros :: [Int] -> [Int]
doisPrimeiros (x:xs) = [x, head xs]

semDoisPrimeiros :: [Int] -> [Int]
semDoisPrimeiros [] = []
semDoisPrimeiros (x:x1:xs) = xs

penultimoElemento :: [Int] -> Int
penultimoElemento x = head (tail (reverse x))

comparadora :: [Int] -> [Int] -> [Int]
comparadora x [] = x
comparadora x y | head y > penultimoElemento x = comparadora (x ++ [head y]) (tail y)
                | otherwise = comparadora x (tail y)


--[4,3,2,5,7,4,6,2,5]
--[4,3,5,7]

pegaTresElem :: [Int] -> [Int]
pegaTresElem x = [head x, head (tail x), head (tail (tail x))]


concatTeste :: [Int] -> [Int] -> [Int]
concatTeste (x1:x2:xs) y = x1 : x2 : y 


teste' :: [Int] -> [Int]
teste' x | length x <= 2 = init (init x)
teste' x | (\t -> head t < last t) (pegaTresElem x) = last (pegaTresElem x) : teste' (tail x)
         | otherwise = teste' (tail x)


teste :: [Int] -> [Int]
teste x = concatTeste x (teste' x)




listaMaior :: [[Int]] -> Int -> [[Int]]
listaMaior [] _ = []
listaMaior (a:as) y | (\x z -> length x > z) a y = a : listaMaior as y
                    | otherwise = listaMaior as y  












--QUESTAO 1-----------------------------------------------------------
--entrada: [3,1000,2000]
--saida: 3


-- somaDigits 12
somaDigits :: Int -> Int
somaDigits 0 = 0
somaDigits x = x `mod` 10 + somaDigits (x `div` 10)



bigSum :: [Int] -> Int
bigSum [] = 0
bigSum x | somaDigits (head x) > bigSum (tail x) = head x
         | otherwise = bigSum (tail x)


--FIM QUESTAO 1------------------------------------------------------


--QUESTAO 6--------------------------------------------------
-- 1 2 3
-- 4 5 6
-- 7 8 9

-- 1 2
-- 3 4


somaL :: [Int] -> Int
somaL [] = 0
somaL (x:xs) = x + somaL xs

--Transpoe Matriz
transpoe :: [[Int]] -> [[Int]]
transpoe ([]:_) = []
transpoe x = map head x : transpoe (map tail x)

--COMPARA COLUNA COM TODAS LINHAS
colunaClinhas :: [Int] -> [[Int]] -> Int
colunaClinhas _ [] = 0
colunaClinhas x (y:ys) | somaL x > somaL y = 1 + colunaClinhas x ys
                       | otherwise = colunaClinhas x ys


--COMPARA CADA COLUNA COM TODAS AS LINHAS
comparador :: [[Int]] -> [[Int]] -> Int
comparador [] _ = 0
comparador (x:xs) y = colunaClinhas x y + comparador xs y


posicoesVen :: [[Int]] -> Int
posicoesVen x = comparador (transpoe x) x


--FIM QUESTAO 6-------------------------------------------------------------


--QUESTAO 4-------------------------------------

--[('a', ++'b')]




--[(2,(+5)), ('a', (++'b')), (1, (-2))]


aplica :: (t1, t1 -> t2) -> t2
aplica (e,f) = f e

 
aplicaFuncoes :: [(t1, t1 -> t2)] -> [t2]
aplicaFuncoes [] = []
aplicaFuncoes x = map aplica x




--FIM QUESTAO 4---------------------------------


--QUESTAO 3-----------------------------------------
maximo :: (Int, Int) -> [(Int, Int)] -> Bool
maximo _ [] = True
maximo x (y:ys) | (fst x >= fst y && fst x >= snd y) || (snd x >= fst y && snd x >= snd y) = maximo x ys
                | otherwise = False


minimo :: (Int, Int) -> [(Int, Int)] -> Bool
minimo _ [] = True
minimo x (y:ys) | (fst x <= fst y && fst x <= snd y) || (snd x <= fst y && snd x <= snd y) = minimo x ys
                | otherwise = False



retornaMaximo :: [(Int, Int)] -> (Int, Int)
retornaMaximo (x:xs) | maximo x xs = x
                     | otherwise = retornaMaximo xs


retornaMinimo :: [(Int, Int)] -> (Int, Int)
retornaMinimo (x:xs) | minimo x xs = x
                     | otherwise = retornaMinimo xs

maxMin :: [(Int, Int)] -> ((Int,Int), (Int, Int))
maxMin [] = ((0,0),(0,0))
maxMin x = (retornaMaximo x, retornaMinimo x)


--FIM QUESTAO 3------------------------------------



--QUESTAO 2-----------------------------------------





comparaIndices :: (String, Int) -> [(String, Int)] -> [Int]
comparaIndices _ [] = []
comparaIndices x (t:ts) | (fst x == fst t) = snd t : comparaIndices x ts
                        | otherwise = comparaIndices x ts


retornaTudo :: [(String, Int)] -> [(String, Int)] -> [(String, [Int])]
retornaTudo [] _ = []
retornaTudo (x:xs) y = (fst x, comparaIndices x y) : retornaTudo xs y



existeNaLista :: (String, [Int]) -> [(String, [Int])] -> Int
existeNaLista _ [] = 0
existeNaLista x (y:ys) | x == y = 1 + existeNaLista x ys
                       | otherwise = existeNaLista x ys


tiraRepetidos :: [(String, [Int])] -> [(String, [Int])]
tiraRepetidos [] = []
tiraRepetidos x | existeNaLista (last x) (init x) >= 1 = tiraRepetidos (init x)
                | otherwise = last x : tiraRepetidos (init x)


group :: [(String, Int)] -> [(String, [Int])]
group x = reverse (tiraRepetidos (retornaTudo x x))



--FIM QUESTAO 2-------------------------------------------------
























