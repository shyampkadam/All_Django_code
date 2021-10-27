from rest_framework.throttling import UserRateThrottle

class ChantiRateThrottle(UserRateThrottle):
 scope = 'chanti'