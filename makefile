define write_file =
echo `CLIENT_ID: 'CLIENT_ID'\nCLIENT_SECRET: 'CLIENT_SECRET'\nUSERNAME: 'USERNAME'\nDER_FONKYBEATZ: True` > spotify.yaml
endef

define funky_message
ok cool dude just make sure you grab your api keys at

https://developer.spotify.com/

and throw them in spotify.yaml
endef

install: python -m pip install -r requirements.txt

funkybeats:
			$(value write_file)
			@echo "$$funky_message"