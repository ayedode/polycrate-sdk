from typing import Literal

ApiV1IdpIdentityprovidersCreateHostnameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateHostnameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_idp_identityproviders_create_hostname_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateHostnameErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
