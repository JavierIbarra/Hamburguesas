#!/bin/bash

kubectl apply -f burgers-docker--env-configmap.yaml
sleep 15
kubectl apply -f db-service.yaml
sleep 10
kubectl apply -f db-deployment.yaml
sleep 10
kubectl apply -f web-django-service.yaml
sleep 10
kubectl apply -f web-django-deployment.yaml
sleep 10
kubectl apply -f web-odoo-service.yaml
sleep 10
kubectl apply -f web-odoo-deployment.yaml
sleep 10
kubectl apply -f nginx-service.yaml
sleep 10
kubectl apply -f nginx-deployment.yaml
sleep 15
kubectl port-forward svc/nginx 8000:8000