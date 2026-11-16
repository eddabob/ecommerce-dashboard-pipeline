WITH orders AS (
  SELECT * FROM {{ref('stg_orders')}}
),

items AS (
  SELECT 
    order_id,
    SUM(price) AS total_revenue,
    SUM(freight_value) AS total_shipping
  FROM {{source('raw_ecommerce', 'order_items')}}
  GROUP BY order_id
)

SELECT
    o.order_id,
    o.customer_id,
    o.order_status,
    DATE_TRUNC('month', o.purchased_at) as order_month,
    COALESCE(i.total_revenue,0) AS total_revenue,
    COALESCE(i.total_shipping,0) AS total_shipping,
    DATE_DIFF('day', o.estimated_delivery_at, o.delivered_at) as days_late
FROM orders o LEFT JOIN items i
ON o.order_id=i.order_id
