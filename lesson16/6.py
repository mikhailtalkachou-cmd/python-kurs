class HttpRequest:
    def __init__(self, method, target, headers=None, body=None):
        self.method = method
        self.target = target
        self.headers = headers if headers is not None else {}
        self.body = body if body is not None else "(empty)"

    def display(self):
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print("Headers:")
        
        if self.headers:
            for key, value in self.headers.items():
                print(f"  {key}: {value}")
        else:
            print("(empty)")
            
        print("Body:")
        print(f"  {self.body}")

jakies_headers = {
    ".....": ".../json",
    "key": "token_..."
}
jakies_body = '{"username": "jan_kowalski", "status": "active"}'

request = HttpRequest(
    method="POST", 
    target="/api/users", 
    headers=jakies_headers, 
    body=jakies_body
)

request.display()