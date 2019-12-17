define funky_message
ok cool dude just make sure you grab your api keys at

https://developer.spotify.com/

and throw them in spotify.yaml
endef

install: 
			python -m pip install -r requirements.txt

export funky_message
funkybeats:
			cp spotify.example.yaml spotify.yaml
			@echo "$$funky_message"