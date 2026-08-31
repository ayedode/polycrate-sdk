from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_idp_identityproviders_partial_update_provider_id_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
