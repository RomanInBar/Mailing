class ResponsMailing:
    @property
    def not_found(self):
        return {'detail': {'detail': f'Рассылка не найдена'}}
    
    @property
    def unique_error(self):
        return {'detail': 'Рассылка с таким сообщением уже существует'}

    @property
    def deleted(self):
        return {'detail': f'Данные рассылки успешно удалены'}
