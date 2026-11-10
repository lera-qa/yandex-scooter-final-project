SELECT c.login,
       COUNT(o."courierId") AS orders_in_delivery
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
    ON c.id = o."courierId"
   AND o."inDelivery" = true
GROUP BY c.login;
