SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME
FROM ANIMAL_INS INNER JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE ('Intact%') AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE ('Spayed%') OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE ('Neutered%'))
ORDER BY ANIMAL_ID

-- 다른 풀이
-- SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME 
-- FROM ANIMAL_INS as I JOIN ANIMAL_OUTS as O 
-- WHERE I.ANIMAL_ID = O.ANIMAL_ID AND I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
-- ORDER BY I.ANIMAL_ID