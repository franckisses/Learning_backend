

create table trips 
(
id  serial,
 client_id int, 
 driver_id int ,
 city_id  int,
 status     varchar,         
 request_at date

) ;

create table users (
users_id int, banned varchar,
role     varchar
);



1        | No     | client
2        | Yes    | client
3        | No     | client
4        | No     | client
10       | No     | driver
11       | No     | driver
12       | No     | driver
13       | No     | driver



select 
a.request_at as "Day"
, round(sum(case when a.status != 'completed' then 1.0 else 0 end) / count(a.status),2) as "Cancellation Rate"
from trips a 
left join users b on a.client_id = b.users_id 
left join users c on a.driver_id = c.users_id 
where b.banned='No' and c.banned='No' and a.user_id notnull and c.users_id notnull 
group by request_at ;


select
a.request_at as "Day",
a.status 
from trips a 
left join users b on a.client_id = b.users_id 
left join users c on a.driver_id = c.users_id 
where b.banned='No' and c.banned='No'
group by request_at 

create table activity (
 player_id int, 
 device_id int,
 event_date date,
  games_played int 
);



create table stadium (
     id int,
     visit_date date,
     people int
);