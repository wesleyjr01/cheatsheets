select 
  round(sum(size_bytes)/pow(10,9), 2) as size
from
  <PROJECT>.__TABLES__
where 
  table_id = 'TABLE_NAME'
