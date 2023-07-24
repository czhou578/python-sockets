import asyncio
import aiofiles
import getopt
import sys
import aiohttp
import json




def download_file(file_path):
    print('download not successful')


async def upload_file(url, file_path):
    try:
        async with aiohttp.ClientSession() as session:
            async with aiofiles.open(file_path, mode='r') as file:
                content = await file.read()
                async with session.post(server_url, json=content) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        print('response: ', response_data)

    except Exception as e:
        print("an error: ", str(e))

    print('upload successful')


if len(sys.argv) != 3:
    print("Usage: python upload_file_async.py <server_url> <file_path>")

else:
    server_url = sys.argv[1]
    file_path = sys.argv[2]
    asyncio.run(upload_file(server_url, file_path))



# call get asyncio with download_file