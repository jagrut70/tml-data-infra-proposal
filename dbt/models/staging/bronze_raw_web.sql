with src as (
    select * from {{ ref('seed_bronze_raw') }}
)
select * from src
