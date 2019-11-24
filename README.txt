
VicosinTool
    - tool for scraping vk.com profiles.

Q/A

Q: How to run?
A: 'python3 ./main.py' #Please use python3 to run the software

Q: How do I get the token?
A: You get it in two steps:
-- 1) Go here and press allow --> https://oauth.vk.com/authorize?client_id=7218375        &scope=photos,audio,video,docs,notes,pages,status,questions,wall,groups,email,    noti    fications,stats,offline,docs,pages,stats,notifications&response_type=token
-- 2) Look at the URL you've been redirected to. There
should be `access_token=[token]` in it. You should copy
everything before the '&' symbol. That's your token, congrats!

