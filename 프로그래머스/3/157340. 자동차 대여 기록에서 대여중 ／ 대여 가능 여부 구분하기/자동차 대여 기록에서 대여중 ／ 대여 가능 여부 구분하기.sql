/*
2022년 10월 16일
-> 대여중 -> '대여중'이라고 표시
-> 대여아님 -> '대여 가능'이라고 표시
컬럼명 availability

2022년 10월 16일 이 END_DATE인 경우 대여 가능임을 확인
-> 하루 빼주기
*/

SELECT CAR_ID,
    MAX(
        CASE
            WHEN "20221016" BETWEEN START_DATE AND END_DATE THEN '대여중'
            ELSE '대여 가능'
        END
    ) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;