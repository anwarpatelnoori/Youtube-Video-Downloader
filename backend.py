from pytube import YouTube
import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer


class DownloadVideo(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        response_data = {'message':'you clicked the button'}
        reponse_json = json.dumps(response_data)
        self.wfile.write(reponse_json.encode('utf-8'))
def run():
        server_address = ('127.0.0.1',5500)
        httpd = HTTPServer(server_address,DownloadVideo)
        print(f'http://{server_address[0]}:5500')
        httpd.serve_forever()


run() 
 




# url = "https://www.youtube.com/watch?v=v1mZ0aSG2-U"
# yt = YouTube(url)
# video_title = yt.title
# video_channel = yt.author
# video_duration = yt.length
# video_thumnail = yt.thumbnail_url
# video_views = yt.views
# # print(yt.streams)
# streams = yt.streams.filter(file_extension='mp4', type='video', only_video=True )
# print(f'length is {len(streams)}')
# for stream in streams:
#     print(f"Resolution: {stream.resolution}\n")
# print(f'Title {video_title}')
# print(f'Owner{video_channel}')
# print(f'Length{video_duration}')
# print(f'THumbnail{video_thumnail}')
# print(f'Views{video_views}')






