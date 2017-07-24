drop table if exists entries;
creat table entries(
    id integer primary key autoincrement,
    title string not null,
    text string not null
);