/*
7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로
상위 3개의 맛을 조회
*/

SELECT FLAVOR
FROM (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS CNT 
    FROM (
        SELECT * FROM FIRST_HALF
        UNION ALL
        SELECT * FROM JULY
    ) AS O
    GROUP BY FLAVOR
    ORDER BY CNT DESC
) AS R
LIMIT 3;
