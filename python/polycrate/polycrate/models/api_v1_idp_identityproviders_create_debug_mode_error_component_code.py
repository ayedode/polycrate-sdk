from typing import Literal

ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
