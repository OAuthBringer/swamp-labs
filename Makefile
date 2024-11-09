# Orchestrate creation of all deployments
.PHONY: create
create:
	make -f HomeCore create

# Orchestrate deletion of all deployments
.PHONY: delete
delete: 
	make -f HomeCore delete

.PHONY: status
status:
	kubectl get all -n home-core -o wide

.PHONY: home-assistant-available
home-assistant-available:
	minikube service home-assistant-service -n home-core
