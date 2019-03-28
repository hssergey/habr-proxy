from django.test import TestCase
from habr_proxy.proxy.utils import add_symbols


class AddSymbolsTest(TestCase):
	
	def testAddSymbols(self):
		text = "Сейчас на фоне уязвимости Logjam все в индустрии в очередной раз обсуждают проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы поговорить об одной из них, а именно — о настройке ciphersiutes."
		result = add_symbols(text)
		self.assertEqual(result, "Сейчас™ на фоне уязвимости Logjam™ все в индустрии в очередной раз обсуждают проблемы и особенности TLS. Я хочу воспользоваться этой возможностью, чтобы поговорить об одной из них, а именно™ — о настройке ciphersiutes.")