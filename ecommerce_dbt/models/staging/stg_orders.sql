SELECT
    order_id,
    customer_id,
    order_status,
    CAST(order_purchase_timestamp AS TIMESTAMP) as purchased_at,
    CAST(order_delivered_customer_date AS TIMESTAMP) as delivered_at,
    CAST(order_estimated_delivery_date AS TIMESTAMP) as estimated_delivery_at
FROM {{source('raw_ecommerce', 'orders')}}
WHERE order_id IS NOT NULL
