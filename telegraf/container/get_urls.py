import os
import requests
import toml

p = '/etc/telegraf/telegraf.d/ping_test.conf'
t = toml.load(p)
urls = requests.get(f"http://{os.environ.get('BACKEND_URL')}/api/urls")

if not set(t['inputs']['ping'][0]['urls']) == set(urls.json()):
    with open(p, "w") as fp:
        t['inputs']['ping'][0]['urls'] = urls.json()
        toml.dump(t, fp)
    os.system('reboot')
