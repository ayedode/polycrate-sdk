from typing import Literal

ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentAttr = Literal["last_rate_limited_at"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentAttr
] = {
    "last_rate_limited_at",
}


def check_api_v1_provider_accounts_partial_update_last_rate_limited_at_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
