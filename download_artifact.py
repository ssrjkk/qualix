import urllib.request
import zipfile
import io

dl_url = 'https://api.github.com/repos/ssrjkk/qualix/actions/artifacts/7625364030/zip'
req = urllib.request.Request(dl_url)
req.add_header('Accept', 'application/vnd.github.v3+json')
req.add_header('User-Agent', 'python')

try:
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
        print(f'Downloaded {len(data)} bytes')
        z = zipfile.ZipFile(io.BytesIO(data))
        for name in z.namelist():
            print(f'File in zip: {name}')
            content = z.read(name).decode('utf-8')
            print('=' * 60)
            print(content)
            print('=' * 60)
except urllib.error.HTTPError as e:
    print(f'HTTP Error: {e.code}')
    body = e.read()
    print(f'Body: {body[:1000]}')
except Exception as e:
    print(f'Error: {e}')
