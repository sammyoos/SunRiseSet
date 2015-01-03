#!/usr/bin/python
from __future__ import print_function
import pprint

import math
import time

from datetime import datetime, timedelta

pp = pprint.PrettyPrinter(indent=4)

winterMorn = datetime.strptime('Jan 01 2015  7:54AM', '%b %d %Y %I:%M%p')
winterEven = datetime.strptime('Dec 21 2014  4:47PM', '%b %d %Y %I:%M%p')
summerMorn = datetime.strptime('Jun 14 2015  5:39AM', '%b %d %Y %I:%M%p')
summerEven = datetime.strptime('Jun 21 2015  9:06PM', '%b %d %Y %I:%M%p')

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

def getDaysDelta( date1, date2 ):
	dateDelta = date1 - date2
	print( '' )
	print( 'dateRange:', dateDelta )
	print( 'dateRange:', dateDelta.days )

	# is this actually 1 more day...
	daysDelta = dateDelta.days + (1 if ( dateDelta.seconds > 12 * 60 * 60 ) else 0)
	print( 'daysDelta', daysDelta )

	return( daysDelta )
	
def getSecsDelta( date1, date2 ):
	timeRange = secondsIntoDay( winterMorn ) - secondsIntoDay( summerMorn )
	print( '' )
	print( 'timeRange:', timeRange )
	return( timeRange )



def offsetForDay( dayFromWinterSol, dateRange, secRange ):
	return( float(secRange)/2.0 * ( 1.0 - math.cos( float(dayFromWinterSol) * math.pi / float(dateRange ))))


#timeInfo( winterMorn )
#print( '' )
#timeInfo( summerMorn )

secsDelta = getSecsDelta( summerMorn, winterMorn )
daysDelta = getDaysDelta( summerMorn, winterMorn )

#print( 'day 001 offset', offsetForDay(   0, daysDelta, secsDelta ))
#print( 'day 091 offset', offsetForDay(  91, daysDelta, secsDelta ))
#print( 'day 182 offset', offsetForDay( 182, daysDelta, secsDelta ))

oldSecs = offsetForDay( 0, daysDelta, secsDelta)

for d in range( 0, int( daysDelta ) + 1 ):
	secs = offsetForDay( d, daysDelta, secsDelta)
	dateAndTime = winterMorn + timedelta(days=d) - timedelta(seconds=secs)

	#print( 'day(%i) offset(%i seconds) date(%s)' % ( d, secs, dateAndTime ))
	print( '%s - %i seconds difference' % (dateAndTime.strftime( '%b %d %Y %I:%M%p'), secs - oldSecs ))
	oldSecs = secs


# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
