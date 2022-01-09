from requests import post

class XShort:
	def __init__(self, ACCESS_TOKEN: str) -> None:
		self.headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Content-Type': 'application/json'}

	def shortener(self, link: str) -> dict:
		return post("https://api-ssl.bitly.com/v4/shorten", json={"long_url": link}, headers=self.headers).json()

	def __repr__(self) -> str:
		return f"URL Shortener"
