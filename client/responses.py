class ResponsClient:
    @property
    def not_found(self):
        return {'detail': {'detail': f'Клиент не найден'}}
    
    @property
    def unique_error(self):
        return {'detail': 'Клиент с такой почтой уже существует'}

    @property
    def deleted(self):
        return {'detail': f'Данные клиента успешно удалены'}
