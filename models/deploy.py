# -*- coding: utf-8 -*-
"""
Application health endpoints
"""
import httpx
import logging



def deploy():
    """
    Deploy BPM models and forms
    """
    logging.info("Deploying application")

    try:
        response = httpx.get("http://localhost:8080/deploy")
        logging.info(response.text)
    except Exception as e:
        logging.error(e)






data = {
	"variables": [],
	"info": {
		"name": "Camunda",
		"_postman_id": "7198f63a-a9c8-684d-d1a4-ec50443fba02",
		"description": "",
		"schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
	},
	"item": [
		{
			"name": "http://localhost:8080/engine-rest/deployment/create",
			"request": {
				"url": "http://localhost:8080/engine-rest/deployment/create",
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "file",
							"value": "",
							"description": "",
							"type": "file"
						},
						{
							"key": "deployment-name",
							"value": "TestDeployment",
							"description": "",
							"type": "text"
						}
					]
				},
				"description": ""
			},
			"response": []
		}
	]
}