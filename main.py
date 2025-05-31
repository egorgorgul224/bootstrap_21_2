from http.server import BaseHTTPRequestHandler, HTTPServer

# Адрес для доступа по сети
hostName = "localhost"
# Порт для доступа по сети
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        # Отправка кода ответа
        self.send_response(200)
        # Отправка типа данных, который будет передаваться
        self.send_header("Content-type", "text/html")
        # Завершение формирования заголовков ответа
        self.end_headers()
        with open("main.html", "r", encoding="utf-8") as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
