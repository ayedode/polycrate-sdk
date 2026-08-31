from typing import Literal

ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentAttr = Literal["api_backoff_minutes"]

API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentAttr
] = {
    "api_backoff_minutes",
}


def check_api_v1_provider_accounts_create_api_backoff_minutes_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
