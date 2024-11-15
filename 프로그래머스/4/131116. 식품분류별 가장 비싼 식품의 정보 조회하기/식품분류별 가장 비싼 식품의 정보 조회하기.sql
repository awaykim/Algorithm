SELECT CATEGORY, price AS MAX_PRICE, PRODUCT_NAME
FROM food_product
WHERE (category, price) IN (
    SELECT category, MAX(price)
    FROM food_product
    GROUP BY category
)
AND (category LIKE '%과자%' OR category LIKE '%국%' OR category LIKE '%김치%' OR category LIKE '%식용유%')
ORDER BY PRICE DESC 