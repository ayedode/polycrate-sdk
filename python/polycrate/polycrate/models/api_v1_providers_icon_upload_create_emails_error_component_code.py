from typing import Literal

ApiV1ProvidersIconUploadCreateEmailsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersIconUploadCreateEmailsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_icon_upload_create_emails_error_component_code(
    value: str,
) -> ApiV1ProvidersIconUploadCreateEmailsErrorComponentCode:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
