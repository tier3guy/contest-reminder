
from pushbullet import PushBullet
from bs4 import BeautifulSoup
import requests
import time


def __main__():
  codechef_link = "https://www.codechef.com/"
  pushBullet_access_token = "o.96jyHv9X9XHS8pi1YgMW8pWBNyrb6B0V"

  html_content = requests.get(codechef_link).text
  soup = BeautifulSoup(html_content, 'lxml')

  contest_list = soup.find_all('div', class_ = "m-navigation-item__container")[1].find_all('a', class_ = "m-navigation-dropdown__item")
  
  upcoming_contests = []

  for index, link in enumerate(contest_list):
    if(link.span.text == "All Contests" or link.span.text == "Contest Calender"):
      break
    upcoming_contests.append(link)

  msg = ""
  for contest in upcoming_contests:
    msg += (f"{contest.span.text} : {codechef_link}{contest['href']}\n\n")

  if msg == "":
    msg = "No contest has been scheduled"
  
  pb = PushBullet(pushBullet_access_token)
  push = pb.push_note("Contest Reminder", msg)


while True:
  __main__()
  time_wait = 24 * 60
  time.sleep(time_wait * 60)