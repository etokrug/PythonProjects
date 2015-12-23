CREATE database JobSearches;

USE JobSearches;

create table Jobs (
	pk_jobs int NOT NULL AUTO_INCREMENT
	, search_terms varchar(300)
	, title varchar(300)
    , company varchar(300)
    , snippet varchar(300)
    , location varchar(300)
    , posting_date datetime
    , indeed_url varchar(2000)
    , job_expired_at_search bool
    , summary varchar(8000)
    , search_date datetime
	, primary key(pk_jobs)
);