from typing import Literal

ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_provider_accounts_partial_update_last_rate_limited_at_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateLastRateLimitedAtErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_LAST_RATE_LIMITED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
