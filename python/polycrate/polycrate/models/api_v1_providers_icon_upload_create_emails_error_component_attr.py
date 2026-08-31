from typing import Literal

ApiV1ProvidersIconUploadCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersIconUploadCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_providers_icon_upload_create_emails_error_component_attr(
    value: str,
) -> ApiV1ProvidersIconUploadCreateEmailsErrorComponentAttr:
    if value in API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ICON_UPLOAD_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
