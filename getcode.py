import imaplib
import email
import re
import asyncio


async def getcode(id,pw):
    #todo 시간 확인해서
    await asyncio.sleep(1.0)
    userid=id
    userpass=pw
    server = imaplib.IMAP4_SSL('imap.naver.com')
    server.login(userid,userpass)
    rv, data = server.select()
    rv,data=server.search(None,"(UNSEEN)",'FROM','no-reply@dgist.ac.kr')
    data=data[0].split()
    recent_no = data[-1]
    print(data)
    rv, fetched = server.fetch(recent_no, '(RFC822)')
    message = email.message_from_bytes(fetched[0][1])
    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
                break
    else:
        body = message.get_payload(decode=True)
    pattern=re.compile("<span>([0-9]{6})</span>")
    match=pattern.search(body.decode('utf-8'))
    print(match.group(1))
    return match.group(1)