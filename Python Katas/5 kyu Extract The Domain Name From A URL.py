"""
Description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"


"""

# Revised Solution
import re

def domain_name(url):
    domainNameRegex = re.compile(r'''
                                    (\.|\/\/|www\.)*
                                    ([\w\d-]+)
                                    (\.)
                                ''', re.VERBOSE)

    mo = domainNameRegex.search(url)

    return mo.group(2)


# First Solution
import re

def domain_name(url):
    try:
        domainNameRegex = re.compile(r'''
                                        ((?<=\.)|(?<=\/\/)|(?<=www\.))*
                                        ([^www/\.][a-zA-Z0-9-]+)
                                        (?=\.)
                                    ''', re.VERBOSE)

        mo = domainNameRegex.search(url)
        
        print(url)
        return mo.group(2)

    except:
        print(url)


