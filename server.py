from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Обрабатывает GET-запросы и возвращает страницу Контакты"""
        self._send_html()

    def do_POST(self):
        """Обрабатывает POST-запросы: читает данные формы и возвращает Контакты"""
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        data = parse_qs(body)

        print("=" * 40)
        print("Получены данные формы:")
        print(f"Имя:       {data.get('name', [''])[0]}")
        print(f"Почта:     {data.get('email', [''])[0]}")
        print(f"Сообщение: {data.get('message', [''])[0]}")
        print("=" * 40)

        self._send_html()

    def _send_html(self):
        """Читает page_4.html и отправляет его клиенту"""
        with open("page_4.html", "r", encoding="utf-8") as file:
            content = file.read()

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен: http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")