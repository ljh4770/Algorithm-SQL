/*
 공간을 둘 이상 등록한 사람을 "헤비 유저"
 헤비 유저가 등록한 공간의 정보
 
 아이디 순
*/



SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
) # 헤비 유저 고르기
ORDER BY ID ASC;