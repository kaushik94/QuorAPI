import urllib2

from bs4 import BeautifulSoup as BS


def get_answer(url):
	'''
	Given an answer url, returns a string of html code of the answer written.

	Example
	=======
	
	>>> from QuorAPI.HTMLparser import get_answer
	>>> url = 'http://www.quora.com/Google-India-Intern-2015-Who-all-will-be-joining-as-interns-at-Google-India-Office-s-in-summer-2015/answer/Kaushik-Varanasi'
	>>> get_answer(url)
	<html><b><span>6</span> Upvotes</b><p><div class="ExpandedQText QuotableExpandedAnswer ExpandedAnswer"><span class="qlink_container"><a href="/Dhruvi-Shah-2">Dhruvi Shah</a></span> - DA-IICT<div class="ContentFooter AnswerFooter"><span id="ld_kbglrj_100065"><a action_mousedown="AnswerPermalinkClickthrough" class="answer_permalink" href="/Google-India-Intern-2015-Who-all-will-be-joining-as-interns-at-Google-India-Office-s-in-summer-2015/answer/Kaushik-Varanasi" 	id="__w2_SgsCtB8_link">Written Fri</a></span>. 127 views<span id="ld_kbglrj_100066"></span>.</div></div></p></html>

	'''

	content = urllib2.urlopen(url)
	html_ans = BS(content)
	string = '<html>'
	string += '<b>' + str(html_ans.find(attrs={'class':'answer_voters'}).find('span')) + ' Upvotes' +'</b>'
	string += '<p>' + str(html_ans.find(attrs={'class':'ExpandedQText QuotableExpandedAnswer ExpandedAnswer'})).decode('utf-8') + '</p>'
	string += '</html>'
	return string

def get_profile(url):
	'''
	Given a profile url, returns a string of html code of the profile.

	Example
	=======

	>>> from QuorAPI.HTMLparser import get_profile
	>>> url = 'http://www.quora.com/Gayle-Laakmann-McDowell'
	>>> get_profile(url)
	<html><center><p><h1><div class="hover_menu hidden show_nub" id="__w2_Fw9HCKm_menu"><div class="hover_menu_contents white_bg" id="__w2_Fw9HCKm_menu_contents"> </div></div><span class="user">Gayle Laakmann McDowell</span><span id="ld_yyouqm_2351"></span><span class="UserTopWriterBadge"><span class="CurrentTopWriterIcon TopWriterIcon" id="__w2_OeKl0BZ_icon"></span></span></h1></p><p><img alt="Gayle Laakmann McDowell" class="profile_photo_img" height="200" src="http://qph.is.quoracdn.net/main-thumb-47758-200-trqmqasqcepzfhlzoohtrofqpkqetigv.jpeg" width="200"/></p><b><p>45.6k Followers</p></b></center></html>

	'''

	content = urllib2.urlopen(url)
	html_profile = BS(content)
	string  = '<html>' + '<center>'
	string += '<p>' + str(html_profile.find(attrs={'class':'ProfileNameAndSig'}).find()).decode('utf-8') + '</p>'
	string += '<p>' + str(html_profile.find(attrs={'class':'profile_photo_img'})).decode('utf-8') + '</p>'
	string += '<b>' + '<p>' + str(html_profile.find(attrs={'class':'count'}).text) + ' Followers' + '</p>' + '</b>'
	string += '</center>' + '</html>'
	return string
