import json
import allure
from requests import Response
from allure_commons.types import AttachmentType


def info_attaching(response: Response):
    allure.attach(
        body=response.request.method + ' ' + response.request.url,
        name="Request",
        attachment_type=AttachmentType.TEXT,
        extension="txt"
    )

    if response.request.body:
        body = response.request.body

        if isinstance(body, (bytes, bytearray)):
            try:
                body = body.decode("utf-8")
                body = json.dumps(json.loads(body), indent=4, ensure_ascii=False)
                attachment_type = AttachmentType.JSON
                extension = "json"
            except Exception:
                attachment_type = AttachmentType.TEXT
                extension = "txt"
        else:
            body = json.dumps(body, indent=4, ensure_ascii=False)
            attachment_type = AttachmentType.JSON
            extension = "json"

        allure.attach(
            body=body,
            name="Request body",
            attachment_type=attachment_type,
            extension=extension,
        )

    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )
