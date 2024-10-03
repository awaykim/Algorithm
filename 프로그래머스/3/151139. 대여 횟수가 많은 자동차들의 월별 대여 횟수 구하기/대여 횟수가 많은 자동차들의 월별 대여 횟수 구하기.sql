-- 코드를 입력하세요
SELECT 
    month(start_date) as month,
    car_id,
    COUNT(*) AS record
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    START_DATE BETWEEN '2022-08-01' AND '2022-10-31' and
    car_id in (SELECT car_id FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31' GROUP BY car_id HAVING count(*)>=5)
GROUP BY
    month, car_id
HAVING 
    record > 0
ORDER BY
    month(START_DATE) ASC,
    CAR_ID DESC;
