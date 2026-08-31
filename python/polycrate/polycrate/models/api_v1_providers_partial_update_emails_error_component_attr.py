from typing import Literal

ApiV1ProvidersPartialUpdateEmailsErrorComponentAttr = Literal["emails"]

API_V1_PROVIDERS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_providers_partial_update_emails_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateEmailsErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
