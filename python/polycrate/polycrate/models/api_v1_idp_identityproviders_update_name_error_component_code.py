from typing import Literal

ApiV1IdpIdentityprovidersUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_idp_identityproviders_update_name_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateNameErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
