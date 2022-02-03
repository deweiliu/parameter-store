install:
	cd cdk-standard-parameters && npm install
	cd sdk-secure-parameters && pip3 install -r requirements.txt 
deploy:
	cd cdk-standard-parameters && npm run deploy
synth:
	cd cdk-standard-parameters && npm run synth

secure:
	cd sdk-secure-parameters && python3 main.py