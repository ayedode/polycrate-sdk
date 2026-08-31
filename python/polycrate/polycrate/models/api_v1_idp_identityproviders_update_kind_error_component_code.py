from typing import Literal

ApiV1IdpIdentityprovidersUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_idp_identityproviders_update_kind_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateKindErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
