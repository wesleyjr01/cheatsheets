-- https://docs.aws.amazon.com/athena/latest/ug/rows-and-structs.html
with cte_dataset as (
    SELECT
        event_timestamp
        ,params.key
        ,params.value.string_value
        ,params.value.int_value
    FROM
        "database"."events", UNNEST(event_params) as t(params)
)

select * from cte_dataset;
