default:	| clean setup rebuild
setup:
	docker volume create nodemodules_<%= customerSnakeCase %>
	docker-compose -f docker-compose.builder.yml run --rm install
rebuild:
	docker-compose down
	docker-compose build
	docker-compose up -d --remove-orphans
run:
	docker-compose up -d --remove-orphans
dev:
	docker exec -it <%= customerSnakeCase %>-dev npm run dev
enter:
	docker exec -it <%= customerSnakeCase %>-dev /bin/sh
clean:
	docker-compose down

.PHONY: default setup rebuild run dev enter clean