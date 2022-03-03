

async def app(scope, receive, send):
    print("scope: ", scope)
    print("receive: ", receive)
    print("send: ", send)
    # 
    assert scope['type'] == 'http'
    await send({
        'type': 'http.response.start',
        'status': 200,
        'header': [
            b'content-type', b'text/plain'
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, Zhibin Jiang'
    })


