from twilio.rest import TwilioRestClient


def sendSMS(msg):
	try :
		accountSid = 'AC930b1b72f263207aa6aa89aab1fd05a3'
		authToken = '7792bd90391879f7703ae6e2484cdf38'
		twilioClient = TwilioRestClient(accountSid, authToken)
		myTwilioNumber = '2053922256'
		destCellPhone = '+919560500385'
		myMessage = twilioClient.messages.create(body = msg, from_=myTwilioNumber, to=destCellPhone)
		return True
	except :
		return False