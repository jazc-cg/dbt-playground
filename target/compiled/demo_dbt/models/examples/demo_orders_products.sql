with orders as (
    select *
    from "dbtdb"."public"."orders"
),
products as (
    select *
    from "dbtdb"."public"."products"
),
final as (
    select
        orders.id,
        orders.created_timestamp,
        orders.product_id,
        products.name,
        products.description
    from orders
    left join products
    on orders.product_id = products.id
)

select * from final