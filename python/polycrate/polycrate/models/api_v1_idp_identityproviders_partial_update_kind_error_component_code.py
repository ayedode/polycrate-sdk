from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_idp_identityproviders_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
