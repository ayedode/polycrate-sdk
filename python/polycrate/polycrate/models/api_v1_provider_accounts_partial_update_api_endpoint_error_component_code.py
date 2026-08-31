from typing import Literal

ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_provider_accounts_partial_update_api_endpoint_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateApiEndpointErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
