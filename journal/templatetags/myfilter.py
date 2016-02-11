from django import template

register = template.Library()
@register.filter
def taglist(s):
	tglist = s.split(',')
	del(tglist[0])
	return tglist

@register.filter
def inc(x):
	return x+1

@register.filter
def dec(x):
	return x-1