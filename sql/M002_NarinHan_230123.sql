/*
    M002 Duplicate Emails
    https://leetcode.com/problems/duplicate-emails/
    
    Table 'Persons'
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | email       | varchar |
    +-------------+---------+
    id is the primary key column for this table.
    Each row of this table contains an email. The emails will not contain uppercase letters.

    Write an SQL query to report all the duplicate emails.
    Return the result table in any order.
    The query result format is in the following example.
*/

create table 'Persons' (
    id int primary key,
    email varchar(100)
);

select email 
from Persons
group by email
having count(email) > 1;
