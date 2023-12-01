class ResponsClient:
    @property
    def not_found(self):
        return {"detail": {"detail": "Клиент не найден"}}

    @property
    def unique_error(self):
        return {"detail": "Клиент с такой почтой уже существует"}

    @property
    def deleted(self):
        return {"detail": "Данные клиента успешно удалены"}
