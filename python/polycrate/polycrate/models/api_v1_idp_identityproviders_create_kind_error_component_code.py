from typing import Literal

ApiV1IdpIdentityprovidersCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_idp_identityproviders_create_kind_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateKindErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
