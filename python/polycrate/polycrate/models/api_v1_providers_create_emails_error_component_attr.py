from typing import Literal

ApiV1ProvidersCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_PROVIDERS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateEmailsErrorComponentAttr] = {
    "emails",
}


def check_api_v1_providers_create_emails_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateEmailsErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
