## QuorAPI

A Python API to extract Quora data as HTML and text.

## Installation
TO-DO

## Usage

```python
>>> from QuorAPI.HTMLparser import get_answer
>>> url = 'http://www.quora.com/Google-India-Intern-2015-Who-all-will-be-joining-as-interns-at-Google-India-Office-s-in-summer-2015/answer/Kaushik-Varanasi'
>>> get_answer(url)
u'<html><b><span>6</span> Upvotes</b><p><div class="ExpandedQText QuotableExpandedAnswer ExpandedAnswer"><span class="qlink_container"><a href="/Dhruvi-Shah-2">Dhruvi Shah</a></span> - DA-IICT<div class="ContentFooter AnswerFooter"><span id="ld_skbksi_46801"><a action_mousedown="AnswerPermalinkClickthrough" class="answer_permalink" href="/Google-India-Intern-2015-Who-all-will-be-joining-as-interns-at-Google-India-Office-s-in-summer-2015/answer/Kaushik-Varanasi" id="__w2_Khb4blw_link">Written Fri</a></span>. 137 views<span id="ld_skbksi_46802"></span>.</div></div></p></html>'
```
## Requirements
1. urllib2
2. BeautifulSoup 4
