import requests
import aiohttp

async def get_tasks(token: str, org_id: str, user_id: str):
    url = f'https://api.tracker.yandex.net/v2/issues?filter=assignee.id:{user_id}'

    headers = {
        'Authorization': f'hidden',
        'X-Org-Id': f'hidden'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            tasks = await response.json()

    return tasks

class YandexTracker:
    def __init__(self, token):
        self.base_url = 'https://api.tracker.yandex.net/v2'
        self.token = token
        self.headers = {'Authorization': f'hidden'}

    def get_issues(self, user_id):
        url = f'{self.base_url}/issues?filter={{"assignee":"{user_id}"}}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['issues']
        else:
            raise Exception(f'Error {response.status_code}: {response.text}')
        
