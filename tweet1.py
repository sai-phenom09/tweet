import tweepy
ak='a9UyotPauePF56HDrC0XYyTKN'
aks= '9tCAHrU8joOAYhEXbWczFJ5dku29IBbhkjvVL8WW7aH7o0yvJh'
at='1347415729637756930-XAlE0TzaE4SatF4aJ8YGWgC9uruzHP'
ats='5qukSJrRH69yP5TFs4y0sIJi7J0nI9KH1DYtpQUiPPHpM'
def OAuth():
    try:
        auth=tweepy.OAuthHandler(ak,aks)
        auth.set_access_token(at,ats)
        return auth
    except Exception as e:
        return none

apicall = tweepy.API(OAuth())

apicall.update_status('congrats TeamIndia')
print('Tweet created')
