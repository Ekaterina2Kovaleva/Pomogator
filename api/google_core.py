from django.conf import settings
from Pomogator.settings import logger
from servicesApp.google_api_client import DOCS_SERVICE, DRIVE_SERVICE


def create_textfile(name, data):
    """Создает текстовый файл с отправленным текстом в Google Docs"""
    body = {
        'title': name
    }
    document = DOCS_SERVICE.documents().create(
        body=body
    ).execute()
    document_id = document.get('documentId')
    document_title = document.get('title')
    doc_content = {
        'requests': [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': data
                }
            }
        ]
    }
    DOCS_SERVICE.documents().batchUpdate(documentId=document_id, body=doc_content).execute()
    logger.info(f'Создан документ с названием: {document_title}')
    logger.info('Документ создан ссылка:')
    logger.info(f'https://docs.google.com/document/d/{document_id}/')
    logger.info('Содержимое успешно добавлено в документ.')
    return document_id


def set_user_permissions(document_id):
    """Выдает права доступа пользователю"""
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.EMAIL_USER
    }
    DRIVE_SERVICE.permissions().create(
        fileId=document_id,
        body=permissions_body,
        fields='id'
    ).execute()