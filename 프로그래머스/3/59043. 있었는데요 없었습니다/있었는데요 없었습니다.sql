/*
입양일이 잘못 입력되었습니다
보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회

보호 시작일이 빠른 순으로 조회
*/

SELECT I.ANIMAL_ID AS ANIMAL_ID,
    I.NAME AS NAME
FROM (
    ANIMAL_INS AS I
    JOIN ANIMAL_OUTS AS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
)
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME ASC;

