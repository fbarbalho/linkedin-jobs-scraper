import requests
from bs4 import BeautifulSoup
import urllib

# User parameters
user_login = ''
user_password = ''

# Page Parameters
url_login = 'https://www.linkedin.com/uas/login'
#url_login = 'https://www.linkedin.com/uas/login-submit'
#url_home = 'http://www.linkedin.com/nhome'

# Parameters for job and location
job_keyword = urllib.quote('Data Science')
job_location = urllib.quote('San Francisco Bay Area')

# url job
url_job = 'https://www.linkedin.com/jobs/search/?keywords={}&location={}&start={}'.format(job_keyword,job_location,0)

# Create session to persist across requests
session = requests.session()

# Get url function
def get_url(url):
    return session.get(url)

# Post url function
def post_url(url,post):
    return session.post(url, data=post)

# Create new beautifulsoup object
def beautify(url):
    content = get_url(url)
    return BeautifulSoup(content.text,"html.parser")

# Get login page and transform into beautifulsoup object
login = beautify(url_login)

# Get hidden form inputs
inputs = login.find('form', {'name': 'login'}).findAll('input', {'type': ['hidden', 'submit']})


# Create POST data
post = {input.get('name'): input.get('value') for input in inputs}

# Define session key and password
post['session_key'] = user_login
post['session_password'] = user_password

# Post login
post_response = post_url(url_login,post)

# Get job page and transform into beautifulsoup object
jobs = beautify(url_job)

results_context = jobs.find('occludable-update card-list__item jobs-search-two-pane__search-result-item ember-view')
print(len(results_context))



print results_context
#n_jobs = int(results_context.text.replace(',','')) 

print "###### Number of job postings #######"

#print n_jobs

print "#####################################"