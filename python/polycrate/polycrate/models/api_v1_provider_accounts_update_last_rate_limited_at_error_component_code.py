from typing import Literal

ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_provider_accounts_update_last_rate_limited_at_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
