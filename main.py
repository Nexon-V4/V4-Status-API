from typing import Union
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

NEXON_V4_STATUS_CHECK_API_ENDPOINT = 'https://v4.nexon.co.jp/maintenance/getsetting'


def lookup_status() -> Union[bool, dict]:
    response = requests.post(url=NEXON_V4_STATUS_CHECK_API_ENDPOINT,
                             verify=False)

    if not response.status_code == 200:
        return False

    return response.json()


def main() -> None:
    status = lookup_status()
    print(status)
    print(status['IsMaintenance'])
    print(status['IsGameMaintenance'])
    print(status['IsLoginMaintenance'])


if __name__ == '__main__':
    main()
    
