import requests
import optparse
from termcolor import cprint

parser = optparse.OptionParser()

parser.add_option('-u', '--url', action="store", dest="url", help="Target URL")

parser.add_option('-c', action="store_true",dest="response_code", help="Include to print response code")

parser.add_option('-b', action="store_true",dest="show_body", help="Include to show the body of the response")

parser.add_option('-H', action="store_true",dest="headers", help="Show header from response")

parser.add_option('-p', action="store_true", dest="prettyPrint", help="If set - we will do our best to pretty-print the output")


options, args = parser.parse_args()

if not options.url:
    cprint("MUST specify a URL, scanner.py -h for help", 'red')


response = requests.get(options.url)


if (options.response_code == True):
    cprint(response.status_code, 'blue')

if (options.headers == True):
    cprint(response.headers, 'green')


if (options.show_body == True):
    cprint(response.text, 'cyan')
