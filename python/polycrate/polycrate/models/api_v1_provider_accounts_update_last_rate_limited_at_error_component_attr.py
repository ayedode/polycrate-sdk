from typing import Literal

ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentAttr = Literal["last_rate_limited_at"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentAttr
] = {
    "last_rate_limited_at",
}


def check_api_v1_provider_accounts_update_last_rate_limited_at_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
