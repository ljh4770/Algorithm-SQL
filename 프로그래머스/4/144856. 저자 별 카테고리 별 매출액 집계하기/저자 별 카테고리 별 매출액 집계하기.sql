/*
2022년 1월의 도서 판매 데이터를 기준
저자 별, 카테고리 별 매출액
    TOTAL_SALES = 판매량 * 판매가
저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력

저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬
*/

SELECT A.AUTHOR_ID, A.AUTHOR_NAME, G.CATEGORY,
    SUM(SUM_SALES * G.PRICE) AS TOTAL_SALES
FROM (
    AUTHOR AS A
    JOIN (
        SELECT B.AUTHOR_ID, B.BOOK_ID, B.PRICE, B.CATEGORY, SUM(SALES) AS SUM_SALES
        FROM (
            BOOK AS B
            JOIN (
                SELECT BOOK_ID, SALES
                FROM BOOK_SALES
                WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
            ) AS S
            ON S.BOOK_ID = B.BOOK_ID
        )
        GROUP BY B.BOOK_ID, B.CATEGORY
    ) AS G 
    ON A.AUTHOR_ID = G.AUTHOR_ID
)
GROUP BY G.AUTHOR_ID, G.CATEGORY
ORDER BY A.AUTHOR_ID ASC, G.CATEGORY DESC;