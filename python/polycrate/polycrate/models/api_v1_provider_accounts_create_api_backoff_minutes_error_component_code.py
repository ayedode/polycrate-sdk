from typing import Literal

ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_provider_accounts_create_api_backoff_minutes_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateApiBackoffMinutesErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
