from typing import Literal

ApiV1ProviderAccountsUpdateApiEndpointErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDER_ACCOUNTS_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateApiEndpointErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_provider_accounts_update_api_endpoint_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateApiEndpointErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
