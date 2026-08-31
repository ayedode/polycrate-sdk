from typing import Literal

ApiV1ProvidersUpdateEmailsErrorComponentAttr = Literal["emails"]

API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateEmailsErrorComponentAttr] = {
    "emails",
}


def check_api_v1_providers_update_emails_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateEmailsErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
