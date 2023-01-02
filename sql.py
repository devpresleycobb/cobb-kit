create_repositories_sql = """
create table if not exists repositories
(
    id         INTEGER not null
        constraint repositories_pk
            primary key autoincrement,
    name       INTEGER not null,
    created_at DATETIME default CURRENT_TIME
);

create unique index if not exists repositories_id_uindex
    on repositories (id);

create unique index if not exists repositories_name_uindex
    on repositories (name);


"""
