#SQLZOO
#SELECT names 11~15
#https://sqlzoo.net/wiki/SELECT_names
#11
SELECT name FROM world WHERE name LIKE capital;
#12
#capital 끝에 City가 들어간 name 찾기
SELECT name FROM world WHERE capital LIKE '%City';
#13
#capital 안에 name이 들어있는 경우 찾기
SELECT capital, name FROM world WHERE capital LIKE CONCAT('%',name,'%');
#14
#capital과 name의 앞이 일치하고 capital의 길이가 name보다 길 경우 찾기
SELECT capital, name FROM world WHERE capital LIKE CONCAT(name, '%') AND LEN(capital) > LEN(name);
#15
#https://github.com/arthur-vieira/sqlzoo/blob/master/1-SELECT-names.sql
#맞았다는 표시가 안 뜨는데 다들 이 답을 사용하기에...
SELECT name, REPLACE(capital, name, '') AS ext FROM world where capital LIKE CONCAT(name, '_%');
