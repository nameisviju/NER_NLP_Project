# Import
import paralleldots
# Setting your API key
paralleldots.set_api_key('gkUHEBzreEfKxTMxAT1nA2be5701Wut6Co51U2j5hqk')
# Get your API key here
def ner(text):
    ner=paralleldots.ner(text)
    return ner