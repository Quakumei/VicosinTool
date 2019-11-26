VicosinTool
    - tool for scraping vk.com profiles.

Q/A
Q: What are prerequirements?
A: Python3, requests.

Q: How to run?
Linux A: 
    1) 'chmod +x vicosin.py' to make file executable
    2) './vicosin.py --help' to use
Windows A:
    1) 'python3 vicosin.py --help'

Q: How do I get the token?
A: You get it in two steps:
-- 1) Go here and press allow --> https://oauth.vk.com/authorize?client_id=7218375&scope=photos,audio,video,docs,notes,pages,status,questions,wall,groups,email,notifications,stats,offline,docs,pages,stats,notifications&response_type=token
-- 2) Look at the URL you've been redirected to. There
should be `access_token=[token]` in it. You should copy
everything before the '&' symbol. That's your token, congrats!
