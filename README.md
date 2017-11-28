# 20171128_Logs-Analysis-Project
Udacity Logs Analysis project
This program shows the answer of questions below

## Questions
1. What are the most popular 3 articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## How to run
1. Load the **news** data in the database.
```sql
psql -d news -f newsdata.sql
```
2. Connect to the **news** database.
```sql
psql -d news
```
3. Create views.
check the "Create views" section below
4. Disconnect from **news** database.
5. Execute `logs_analysis.py`.

## Create views
```sql
create view logview as
(select substring(path from 10) slug, ip, method, status, time, id from log);
```

```sql
create view authorview as
(select au.id, au.name, ar.slug from authors au, articles ar where au.id = ar.author);
```

```sql
create view PopularArticles as
(select a.slug, a.title, count(*) as view from articles a, logview lv
where a.slug = lv.slug group by a.slug, a.title order by view desc);
```

```sql
create view PopularAuthors as
(select av.name, sum(PA.view) as view
from authorview av, PopularArticles PA
where av.slug = PA.slug
group by av.name
order by view desc);
```

```sql
create view ErrorRate as
(select errorcount.date, cast(errorcount.count as real)/cast(totalcount.count as real) errorrate 
from (select time::timestamp::date as date, count(*) from log where status != '200 OK' group by date) as errorcount, 
(select time::timestamp::date as date, count(*) from log group by date) as totalcount 
where errorcount.date = totalcount.date and cast(errorcount.count as real)/cast(totalcount.count as real) > 0.01);
```
