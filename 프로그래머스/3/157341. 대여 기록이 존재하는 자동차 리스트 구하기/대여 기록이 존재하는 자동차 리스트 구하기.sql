/*
자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다.
'세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력
*/

SELECT C.CAR_ID
FROM (
    CAR_RENTAL_COMPANY_CAR AS C
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
    ON C.CAR_ID = H.CAR_ID
)
WHERE (
    MONTH(H.START_DATE) = 10
    AND C.CAR_TYPE = '세단'
)
GROUP BY C.CAR_ID
ORDER BY C.CAR_ID DESC;