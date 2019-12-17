install: python -m pip install -r requirements.txt

funkybeats: echo `CLIENT_ID: 'CLIENT_ID'				\
			CLIENT_SECRET: 'CLIENT_SECRET'				\
			CUSTOM_TRACK: 'SPOTIFY_URI'					\
			USERNAME: 'USERNAME'						\
			DER_FONKYBEATZ: True` > spotify.yaml		\
			echo "ok cool dude just make sure you grab	\
			your api keys at							\
			https://developer.spotify.com/ and throw	\
			them in spotify.yaml"