from typing import Literal

ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponentAttr = Literal["api_backoff_minutes"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponentAttr
] = {
    "api_backoff_minutes",
}


def check_api_v1_provider_accounts_archive_create_api_backoff_minutes_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateApiBackoffMinutesErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_API_BACKOFF_MINUTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
