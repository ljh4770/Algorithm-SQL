/*
사원별 성과금 정보를 조회


*/
WITH CTE AS (
    SELECT E.EMP_NO AS EMP_NO,
        AVG(SCORE) AS YEAR_SCORE
    FROM (
        HR_EMPLOYEES AS E
        JOIN HR_GRADE AS G
        ON E.EMP_NO = G.EMP_NO
    )
    GROUP BY E.EMP_NO
)
SELECT E2.EMP_NO AS EMP_NO,
    E2.EMP_NAME AS EMP_NAME,
    (
        CASE 
        WHEN CTE.YEAR_SCORE >= 96 THEN 'S'
        WHEN CTE.YEAR_SCORE >= 90 THEN 'A'
        WHEN CTE.YEAR_SCORE >= 80 THEN 'B'
        ELSE 'C'
        END
    ) AS GRADE,
    ROUND(
    (
        CASE 
        WHEN CTE.YEAR_SCORE >= 96 THEN SAL * 0.2
        WHEN CTE.YEAR_SCORE >= 90 THEN SAL * 0.15
        WHEN CTE.YEAR_SCORE >= 80 THEN SAL * 0.1
        ELSE SAL * 0.0
        END
    ), 1
    ) AS BONUS
FROM (
    HR_EMPLOYEES AS E2
    JOIN CTE
    ON E2.EMP_NO = CTE.EMP_NO
)
ORDER BY E2.EMP_NO ASC;