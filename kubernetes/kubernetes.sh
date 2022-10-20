#!/bin/bash

kubectl apply -f ./secret
sleep 2
kubectl apply -f ./db
sleep 2
kubectl apply -f ./odoo