drop table if exists queries;

create table if not exists queries (
    id bigint generated always as identity primary key,
    query text not null,
    created_at timestamptz not null default now(),
    response_type text,
    chat_session_id uuid
);

alter table queries enable row level security;
