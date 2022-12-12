## Enums vs Check Constraints in Postgres

### eg1

```plsql
CREATE TYPE order_status AS ENUM (
  'pending',
  'shipped',
  'cancelled'
);

CREATE TABLE orders (
    id serial,
    status order_status,
    created_at timestamp default now(),
    updated_at timestamp default now(),
    tracking_id text
);
```



### eg2 

````
CREATE TABLE orders2 (
    id serial,
    status text CHECK (status in ('pending', 'shipped', 'cancelled')),
    created_at timestamp default now(),
    updated_at timestamp default now(),
    tracking_id text
);
````

