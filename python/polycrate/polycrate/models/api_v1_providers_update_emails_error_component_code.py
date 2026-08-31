from typing import Literal

ApiV1ProvidersUpdateEmailsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateEmailsErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_emails_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateEmailsErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
