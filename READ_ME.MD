del_newVideo 是用来删除input_video里的临时文件_new mp4
input_music 是存放目标歌曲的（注意最终导出来的视频长度与目标歌曲一致）
input_videos 存放原视频，原视频的长度大于目标歌曲较好
output_videos 最终交付文件夹

需要安装的包有
pip3 install moviepy

brew install ffmpeg

pip3 install -r requirements.txt

brew install imagemagick



打开终端，进入该文件所在目录，运行命令chmod +x 文件名.sh，赋予文件可执行权限
在终端中运行该文件，命令为./文件名.sh





```java
curl 'https://edith.xiaohongshu.com/api/media/v1/upload/web/permit?biz_name=spectrum&scene=video&file_count=1&version=1&source=web' \
  -H 'authority: edith.xiaohongshu.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: zh-CN,zh;q=0.9,ja;q=0.8' \
  -H 'authorization: AT-cfa6639de5124914bc82d18ec9638002-5c7e7b2e95c84f70a166d73dec0d7b73' \
  -H 'cookie: xhsTrackerId=e1146c0e-a760-492c-a91b-a4de845e1f5b; xhsTrackerId.sig=IJnVPrUa0Yuf2kXaKV24coPlUcmrssMxD6UF04g2Hh0; a1=187d227db2czoc2le5k1vaydclliurku5v7lgphte30000178198; webId=108910db7f52de52476cf351ae42e73d; gid=yYWfJJWfdy2DyYWfJJWfDhUxJSulSJ1d2TyhW9d0vfS111q837FT7k888yWYyjY8Jfiy40KY; gid.sign=jop6OBB7z3wTZcSqpWKh3KGB0gY=; customerClientId=422613414134359; x-user-id-eva.xiaohongshu.com=64706092640000000000000b; x-user-id-creator.xiaohongshu.com=5cc2cceb000000001101fd4b; access-token-creator.xiaohongshu.com=customer.ares.AT-81d6aa57b35046d186f507847d34e63c-96baa18cd49d4816a664d4aafeb21920; x-user-id-gaia.xiaohongshu.com=6470b39b7500000000000009; x-user-id-pro.xiaohongshu.com=6470b39b7500000000000009; gr_user_id=a849eb53-22da-4118-b98e-28d4fb00d53b; x-user-id-fuwu.xiaohongshu.com=6470b39b7500000000000009; x-user-id-ad.xiaohongshu.com=647438f47500000000000009; x-user-id-school.xiaohongshu.com=6470b39b7500000000000009; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%22188dd58c7c2451-0befb3e0197b46-1b525634-1296000-188dd58c7c3178d%22%7D; timestamp2=1688357422183d8de9eeeec76a6673415e9196492cf02a1a80c0147f6aa9ff5; timestamp2.sig=W3exnnAxj7Wq7VcORebzGyso-4pKGdgEBs1frK6ygNk; webBuild=2.14.4; web_session=040069b504379c2e2aec06b899364b63c22a0a; acw_tc=81a46282bfccb024053fc93ddec666af01cd4bcc9e9d215cd86c473619ffa3d2; websectiga=2a3d3ea002e7d92b5c9743590ebd24010cf3710ff3af8029153751e41a6af4a3; customerBeakerSessionId=5dc69599fa83d8469a93bda1bf51179450bf8667gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAlgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2StNTE0/fVgJAAAAYXV0aFRva2VucQNYQQAAAGEwYjc5MWM2MGJmZjQ1M2U5NWRlM2ZlOGQxMTNmNzdiLWJkYzQxNzAwYzYwMTQxN2ZhMGIzZDRjZjUzZGExYWRicQRYAwAAAF9pZHEFWCAAAAAzYjg4OTY0ODJjMTQ0YzRmOGJjOTU1ZjU4NjFlMDIzNnEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZK01MTT99WAYAAAB1c2VySWRxCFgYAAAANjRhNTZjOTA2NDAwMDAwMDAwMDAwMDA2cQlYAwAAAHNpZHEKWBgAAAA2NGFkMzUzMTY0MDAwMDAwMDAwMDAwMThxC3Uu; customer-sso-sid=64ad35316400000000000018; x-user-id-ark.xiaohongshu.com=64a56c906400000000000006; access-token-ark.xiaohongshu.com=customer.ark.AT-cfa6639de5124914bc82d18ec9638002-5c7e7b2e95c84f70a166d73dec0d7b73; xsecappid=share-modules; beaker.session.id=4bbc87abbbf00df1a55d5b2886886f5bcc36e662gAJ9cQEoWA4AAAByYS11c2VyLWlkLWFya3ECWBgAAAA2NGE1NmM5MDY0MDAwMDAwMDAwMDAwMDZxA1UIX2V4cGlyZXNxBGNkYXRldGltZQpkYXRldGltZQpxBVUKB+cICgsCOwx3V4VScQZYCwAAAGFyay1saWFzLWlkcQdYGAAAADY0YTU2ZDFlZDMxNDM4MDAwMTY0M2ZiZnEIWA4AAABfYWNjZXNzZWRfdGltZXEJR0HZK03CSjwpVQNfaWRxClggAAAAYmQxZDMyMmY0M2Q5NDNmZTg4NTVmNjE1YTM0Nzc5MWZxC1gRAAAAcmEtYXV0aC10b2tlbi1hcmtxDFhBAAAAYTBiNzkxYzYwYmZmNDUzZTk1ZGUzZmU4ZDExM2Y3N2ItYmRjNDE3MDBjNjAxNDE3ZmEwYjNkNGNmNTNkYTFhZGJxDVgOAAAAX2NyZWF0aW9uX3RpbWVxDkdB2StNTHx64XUu' \
  -H 'origin: https://ark.xiaohongshu.com' \
  -H 'referer: https://ark.xiaohongshu.com/' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1' \
  -H 'x-s: O21GO6TK1gZUOY1bZYO6OgOv02FbOi5p0g46Z2sL0gv3' \
  -H 'x-subsystem: ark' \
  -H 'x-t: 1689073508221' \
  --compressed
```

```json
{
    "code": 0,
    "success": true,
    "data": {
        "result": {
            "success": true
        },
        "uploadTempPermits": [
            {
                "uploadId": 78,
                "token": "VZY80d2BUB41U7mEW_8Pz89iy7w:eyJkZWFkbGluZSI6MTY4OTA4MDcwOCwiYWxsb3dQcmVmaXhlcyI6WyJDYkVGUjlObFhpcTFsSFNQZzYzdW5aZ1Z1bV9OekZZV2ZyVnZROVlXRFJoaXJYMCJdfQ",
                "uploadAddr": "ros-upload.xiaohongshu.com",
                "expireTime": 1689080708557,
                "cloudType": 4,
                "region": "unknown",
                "qos": 0.99,
                "bucket": "unknown",
                "fileIds": [
                    "spectrum/CbEFR9NlXiq1lHSPg63unZgVum_NzFYWfrVvQ9YWDRhirX0"
                ]
            },
            {
                "token": "eo41WiQvVKBjtaLaA3kqdT6aOmD7s6xabcdfe5b3c030f0760b0726246b5e5c14cmGsE45zkYhqS0umOrubKhuGZbyrQoPgs4_cYNQYxARMZVRQ1lCsTJ5YWnWBObiBptgsMDppgPZWAW6VbIxWhZjKAn7VztYhCpoOisA84d96wHoL35xLmFkZUBHao1a1psp6xMlyL88oxTLGdwGLi8rUJl057Ig-BOD7yVIO3DXF3J4FFrth-LIMa6w4k1E6it2GaI2iW0C1E6Q9FICB63gy6wY0xG0rxKkLQhHWogT6rOrUDhTEdLEhuK-HV7qqsKnmlgDo6hWiZ1gnGsYItbWibKDwwsdMVwiXDwE3lzkko7Avw1pQ-n_sETRM1x0YQwyoP722C-Yd9lECk3n2vH--OF7itGAtKTjyarUFSC6jrtlY2QuE9IrYQia7QSw1fJO6tZigTe_GeRsdVbUHeHQa41WuVffsZcd2HsZ9bGf3tbVB4-ksxbesCNlOa6GmK-SKAUel7V47IbR2JhqemEG-PJTXFFIFeV_Zh3cohESc-AJgpry8dC34A9EzHTXEIFkn2ROZJ41Rcv8TEZVpO_Eh7dAe8JKNqzcbxTQlWEPnoIRIqZfe-mNd5DVPV91wEmLmYbGARcuaPXqmbTeDFrtbLcNoaPdPsPtKGZNkmbw15yDyV6Xz01LA2qSVjcRh",
                "uploadAddr": "note-video-qc-1251524319.cos.accelerate.myqcloud.com",
                "cloudType": 1,
                "region": "ap-shanghai",
                "fileIds": [
                    "spectrum/03037b01ky3dsh18j8t2614wnv10cwtvwy"
                ],
                "masterCloudId": 2,
                "cdnDomain": "http://sns-video-qc.xhscdn.com",
                "secretId": "AKIDamAZfyblufoIXCnVKgVSRtSIe62QJQnlLplgAlCuATDFJJfco5bAk3iwl_FPgZyo",
                "expireTime": 1689080708588,
                "qos": 0.9,
                "bucket": "note-video-qc-1251524319",
                "uploadId": 79,
                "secretKey": "Z1Ix4+mhoCfeqbDL3KPGuqdO1jrUFW1Ln9RZ7FBKMd0="
            },
            {
                "secretKey": "Z1Ix4+mhoCfeqbDL3KPGuqdO1jrUFW1Ln9RZ7FBKMd0=",
                "token": "eo41WiQvVKBjtaLaA3kqdT6aOmD7s6xabcdfe5b3c030f0760b0726246b5e5c14cmGsE45zkYhqS0umOrubKhuGZbyrQoPgs4_cYNQYxARMZVRQ1lCsTJ5YWnWBObiBptgsMDppgPZWAW6VbIxWhZjKAn7VztYhCpoOisA84d96wHoL35xLmFkZUBHao1a1psp6xMlyL88oxTLGdwGLi8rUJl057Ig-BOD7yVIO3DXF3J4FFrth-LIMa6w4k1E6it2GaI2iW0C1E6Q9FICB63gy6wY0xG0rxKkLQhHWogT6rOrUDhTEdLEhuK-HV7qqsKnmlgDo6hWiZ1gnGsYItbWibKDwwsdMVwiXDwE3lzkko7Avw1pQ-n_sETRM1x0YQwyoP722C-Yd9lECk3n2vH--OF7itGAtKTjyarUFSC6jrtlY2QuE9IrYQia7QSw1fJO6tZigTe_GeRsdVbUHeHQa41WuVffsZcd2HsZ9bGf3tbVB4-ksxbesCNlOa6GmK-SKAUel7V47IbR2JhqemEG-PJTXFFIFeV_Zh3cohESc-AJgpry8dC34A9EzHTXEIFkn2ROZJ41Rcv8TEZVpO_Eh7dAe8JKNqzcbxTQlWEPnoIRIqZfe-mNd5DVPV91wEmLmYbGARcuaPXqmbTeDFrtbLcNoaPdPsPtKGZNkmbw15yDyV6Xz01LA2qSVjcRh",
                "uploadAddr": "note-video-qc-1251524319.cos.ap-shanghai.myqcloud.com",
                "cloudType": 1,
                "bucket": "note-video-qc-1251524319",
                "fileIds": [
                    "spectrum/03037b01ky3dsh18j8t2614wnv10cwtvwy"
                ],
                "cdnDomain": "http://sns-video-qc.xhscdn.com",
                "secretId": "AKIDamAZfyblufoIXCnVKgVSRtSIe62QJQnlLplgAlCuATDFJJfco5bAk3iwl_FPgZyo",
                "expireTime": 1689080708588,
                "qos": 0.89,
                "region": "ap-shanghai",
                "masterCloudId": 2,
                "uploadId": 78
            }
        ]
    }
}
```