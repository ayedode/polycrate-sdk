from typing import Literal

ApiV1ProvidersArchiveCreateEmailsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersArchiveCreateEmailsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_providers_archive_create_emails_error_component_code(
    value: str,
) -> ApiV1ProvidersArchiveCreateEmailsErrorComponentCode:
    if value in API_V1_PROVIDERS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
