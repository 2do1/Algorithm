SELECT DISTINCT A.CART_ID
FROM CART_PRODUCTS AS A INNER JOIN CART_PRODUCTS AS B ON A.CART_ID = B.CART_ID
WHERE A.NAME = 'Milk' AND B.NAME = 'Yogurt'
ORDER BY A.CART_ID

-- 서브쿼리
-- SELECT DISTINCT CART_ID
-- FROM CART_PRODUCTS
-- WHERE NAME = 'Milk' AND 
-- CART_ID IN (SELECT DISTINCT CART_ID
--             FROM CART_PRODUCTS
--             WHERE NAME = 'Yogurt')
-- ORDER BY CART_ID

-- GROUP BY, HAVING
-- SELECT CART_ID
-- FROM CART_PRODUCTS
-- WHERE NAME IN ('Milk', 'Yogurt')
-- GROUP BY CART_ID
-- HAVING COUNT(DISTINCT NAME) = 2
-- ORDER BY CART_ID