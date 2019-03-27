from django.http.response import HttpResponse
from django.conf import settings
import requests
import lxml.html


def handle_request(request):
	local_site = request.scheme + "://" + request.META["HTTP_HOST"]
	path = request.path
	headers = {
	    'User-Agent': settings.USER_AGENT,
	}
	#requesting original page
	req = requests.get(settings.PROXIED_SITE + path, headers = headers)
	content_type = "text/html"
	if 'Content-Type' in req.headers:
		content_type = req.headers['Content-Type']
		if "text/html" in content_type:
			content = req.text
			doc = lxml.html.document_fromstring(content)
			#all links to initial site should be rewrited to local
			elements = doc.xpath('//a')
			for element in elements:
				url = element.get("href")
				if url and settings.PROXIED_SITE in url:
					url = url.replace(settings.PROXIED_SITE, local_site)
					element.set("href", url)
			# search text content to add symbol
			root = doc.getroot()
			for element in root.iter():
				text = element.text
			return HttpResponse(lxml.html.tostring(doc), content_type = content_type)
	#bypassing non-html content
	return HttpResponse(req.text, content_type = content_type)



	