"""
    1. Install python 2.X
        1.1 Mechenize requires python 2.X
    
    2. Install mechanize
        2.1 Linux:
            run the command:
            $ sudo pip install mechanize
        2.2 Windows: download mechanize from http://wwwsearch.sourceforge.net/mechanize/src/mechanize-0.2.5.zip
                     unpack
                     access the folder from command prompt
                     run the command:
                     python setup.py install
    
    3. Not tested with captcha.
"""

import sys
import mechanize

reload(sys)
sys.setdefaultencoding('utf8')

times = int(input('How many times do you want to submit form? '))
address = 'https://address.site/contact_page/here/'
browser = mechanize.Browser()
browser.open(address)

for time in range(0, times):
    browser.select_form(nr = 2)
    browser.form['name'] = 'Name ' + str(time)
    browser.form['email'] = 'em@il' + str(time) + '.com'
    browser.form['fone'] = '+5585999999999'
    browser.form['subject'] = 'Subject ' + str(time)
    browser.form['message'] = 'Message ' + str(time)
    browser.submit()
    print(time)
