import os
from datetime import datetime
from pytz import timezone
from crawling import extract_book_data_yes24, extract_book_data_aladin
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    
    ############## Setting
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "yes24_aladin_crawler"
    
    ############## Timezone
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    
    ############## upload
    ## ---- Yes24
    issue_title_yes24 = f"YES24 IT 신간 도서 알림({today_date})"
    upload_contents_yes24 = extract_book_data_yes24()
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title_yes24, upload_contents_yes24)

    ## ---- Aladin
    issue_title_aladin = f"알라딘 IT 신간 도서 알림({today_date})"
    upload_contents_aladin = extract_book_data_aladin()
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title_aladin, upload_contents_aladin)

    print("Upload Github Issue Success!")


