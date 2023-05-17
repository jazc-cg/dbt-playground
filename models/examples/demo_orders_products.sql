with orders as (
    select *
    from {{ source('raw_data', 'orders') }}
),
products as (
    select *
    from {{ source('raw_data', 'products') }}
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