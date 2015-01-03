#!/usr/bin/python
from __future__ import print_function
import pprint

from datetime import datetime
pp = pprint.PrettyPrinter(indent=4)

winter = datetime.strptime('Dec 21 2014  7:51AM', '%b %d %Y %I:%M%p')
summer = datetime.strptime('Jun 21 2015  5:40AM', '%b %d %Y %I:%M%p')

def secondsIntoDay( t ):
	return( t.hour * 60 * 60 + t.minute * 60 + t.second )


def timeInfo( t ):
	print( t )
	print( 'hour  :', t.hour )
	print( 'minute:', t.minute )
	print( 'second:', t.second )
	print( 'microsecond:', t.microsecond )
	print( 'tzinfo:', t.tzinfo )
	print( 'secs in day:', secondsIntoDay( t ) )

timeInfo( winter )
print( '' )
timeInfo( summer )

timeRange = secondsIntoDay( winter ) - secondsIntoDay( summer )
print( '' )
print( 'timeRange:', timeRange )

dateRange = summer - winter
print( '' )
print( 'dateRange:', dateRange )

pp.pprint( dateRange )



# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
