install:
	cd cdk-general-parameters && npm install
	cd sdk-secure-parameters && pip3 install -r requirements.txt 
deploy:
	cd cdk-general-parameters && npm run deploy
synth:
	cd cdk-general-parameters && npm run synth

secure:
	cd sdk-secure-parameters && python3 main.py