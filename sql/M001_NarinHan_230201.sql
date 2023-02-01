/*
    M001 Customers Who Never Order
    https://leetcode.com/problems/customers-who-never-order/
    
    Table 'customers'
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    +-------------+---------+
    id is the primary key column for this table.
    Each row of this table indicates the ID and name of a customer.

    Table 'orders'
    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | customerId  | int  |
    +-------------+------+
    id is the primary key column for this table.
    customerId is a foreign key of the ID from the Customers table.
    Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

    Write an SQL query to report all customers who never order anything.
    Return the result table in any order.
    The query result format is in the following example.
*/

create table customers (
    id int primary key,
    name varchar
);

create table orders (
    id int primary key,
    customerId int foreign key
);

select customers.name as 'Customers'
from customers
where customers.id not in
(
    select customerId from orders
);