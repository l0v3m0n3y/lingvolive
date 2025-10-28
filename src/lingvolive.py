import requests
class Client():
	def __init__(self):
		self.api="https://api.lingvolive.com"
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "application/json"}
	def translate(self,text,lang_id,translate_lang_id:str="1044"):
		return requests.get(f"{self.api}/Translation/Translate?text={text}&srcLang={lang_id}&dstLang={translate_lang_id}&returnJsonArticles=true",headers=self.headers).json()
	def Inflected_forms(self,text,lang_id):
		return requests.get(f"{self.api}/Translation/InflectedForms?text={text}&lang={lang_id}&returnJson=true",headers=self.headers).json()
	def translation_posts(self,text,lang_id,translate_lang_id):
		return requests.get(f"{self.api}/social/feed/translationPosts?dstLang={translate_lang_id}&heading={text}&srcLang={lang_id}",headers=self.headers).json()