# DBT PlayGround
This DBT repo. is for learning purpose only, not for any deployments.
Please do not clone the repo, you can download this as zip and unzip it on your local machine.

#### Create Init env
$ unzip <zip file name>
$ cd <file folder name>


#### Setup virtual env (conda)
$ conda create --name <env name> python=3.8

#### Active virtual env (conda)
$ conda activate <env name>


#### Build and up Postgres DB using docker-compose
- Create the docker image 
$ docker-compose up -d --build

- Get image id for specific container
$ docker image ls $(docker inspect --format='{{.Config.Image}}' dbt_db_container) -aq

- Confirm entrypoint
$ docker run -it $(docker image ls $(docker inspect --format='{{.Config.Image}}' dbt_db_container) -aq) bash
root@22ca79b62eb1:/# ls
bin  boot  dev  docker-entrypoint-initdb.d  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var


#### stop the docker
$ docker-compose down


#### Enter to the database
db connection info: postgres://dbtuser:pssd@localhost:5432/dbtdb
please use any postgres database tool, ex: DataGrip


#### Install DBT
$ pip install --upgrade pip
$ pip install -r requirements.txt


#### Running demo d

#### Note for docker issue
sometime you get issue with com.docker or com.docker.hyperkit, to resolve the issue, 
you have to kill it to proceed further.
$ rm -rf ~/.docker


dbt for major data integration methodologies ETL and ELT


### Reference:
#### what is DBT?
- Data Build Tool (DBT) enables data engineers to transform data in their data warehouse using Select statements in SQL.
- DBT converts the SQL Select statements into Tables and Views
- DBT performs Transforms (T) operation alone over Extract (E) and Load (L), which means is that you can use it for both ETL and ELT strategies moving source data to one or more multi. targets 
- Since this tool majorly focuses on trasforming, it performes the data already loaded in the data warehouse/lake


### How dbt works?
Version Control and CI/CD
- Deploy safely using dev environments. Git-enabled version control enables collaboration and a return previous states.
Test and Documentation
- Test every model prior to porduction, and share dynamically generated documentation with all data stakeholders.
Develop
- Write modular SQL models with SELECT statements and the ref() function - dbt handles the chore of dependency management.


common commends
dbt init <--- initialize your dbt app, it will create profile.yml file under ~/.dbt folder
dbt debug <--- you can use this to test your connection
dbt run
dbt test
dbt doc generate
dbt parse <--- parses your dbt project and writes detailed timing information.


### working with dbt:
dbt init helps get you started using dbt Core!
$ dbt init dbt

Which database would you like to use?
    [1] postgres
    (Don't see the one you want? https://docs.getdbt.com/docs/available-adapters)
    Enter a number: 1     <---- entry
06:51:41  Profile default written to /Users/jazc/.dbt/profiles.yml using target's sample configuration. Once updated, you'll be able to start developing with dbt.

** if you got symbol not found in flat namespace (_PQbackendPID) issue need to remove psycopg2 psycopg2-binary sqlalchemy from pip if any
** and install dbt-postgres again

$ cat /Users/jazc/.dbt/profiles.yml  <---- will give you pg info
$ vim /Users/jazc/.dbt/profiles.yml  <---- update it

create dbt_project.yml file (template: https://github.com/jre247/dbt-forked/blob/master/sample.dbt_project.yml)
The dbt_project.yml tells dbt key information about the way you’ve structured your project and where to find the resources 
you’re going to be referring back to but we have some additional configuariton we can do here for specifying/overiding dbt default run settings. 

