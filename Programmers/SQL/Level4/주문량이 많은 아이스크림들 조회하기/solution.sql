SELECT A.FLAVOR
FROM FIRST_HALF AS A INNER JOIN JULY AS B ON A.FLAVOR = B.FLAVOR
GROUP BY A.FLAVOR
ORDER BY SUM(A.TOTAL_ORDER) + SUM(B.TOTAL_ORDER) DESC
LIMIT 3