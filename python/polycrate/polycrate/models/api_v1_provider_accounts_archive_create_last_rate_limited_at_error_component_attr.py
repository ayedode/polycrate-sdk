from typing import Literal

ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponentAttr = Literal["last_rate_limited_at"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponentAttr
] = {
    "last_rate_limited_at",
}


def check_api_v1_provider_accounts_archive_create_last_rate_limited_at_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateLastRateLimitedAtErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
