input goal, year_of_job, self_eva, requirement weight

select name, (svcw.skill_self_eval-self_eva)+(svcw.year of job_category - year_of_job)/2 as score
from svcw
where goal=svcw.prog1.buddy_name
having svcw.year_of_job_category - year_of_job>=3
and (svcw.skill_self_eval-self_eva)-(svcw.year of job_category - year_of_job) <=10
order by score desc
limit 5

output name, score, requirement weight