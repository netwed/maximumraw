from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, \

OnSiteOrRemoteFilters, IndustryFilters, SalaryBaseFilters

query = Query(
    query='Systems Administrator',
    options=QueryOptions(
        locations=['United States, Canada'],
        apply_link=True,
        skip_promoted_jobs=True,
        limit=5,
        filters=QueryFilters(
            relevance=RelevanceFilters.RECENT,
            time=TimeFilters.WEEK,
            type=[TypeFilters.FULL_TIME,],
            experience=[ExperienceLevelFilters.MID_SENIOR],
            on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
            industry=[IndustryFilters.IT_SERVICES],
            base_salary=SalaryBaseFilters.SALARY_80K
        )
    )
)