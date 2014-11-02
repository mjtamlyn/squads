SHELL := /bin/bash

help:
	@echo "usage:"
	@echo "    make deploy -- deploy to heroku"

deploy:
	git push heroku master

db-refresh:
	heroku pgbackups:url | xargs curl > /tmp/squads.dump && pg_restore -d squads /tmp/squads.dump --clean -x --no-owner
