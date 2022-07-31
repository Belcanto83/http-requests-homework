import requests


class StackOverFlow:
    base_url = 'https://api.stackexchange.com'

    def get_questions(self, site='stackoverflow', tagged='python', **kwargs):
        get_questions_url = self.base_url + '/2.3/questions'

        necessary_params = dict(site=site, tagged=tagged)
        params = {**necessary_params, **kwargs}

        # pagination
        one_page_response = requests.get(get_questions_url, params=params).json()
        response = one_page_response
        page = 1
        while one_page_response['has_more']:
            page += 1
            params['page'] = page
            one_page_response = requests.get(get_questions_url, params=params).json()
            response['items'].extend(one_page_response['items'])
        response['has_more'] = one_page_response['has_more']
        response['quota_remaining'] = one_page_response['quota_remaining']

        return response
