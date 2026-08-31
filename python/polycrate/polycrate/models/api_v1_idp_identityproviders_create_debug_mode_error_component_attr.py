from typing import Literal

ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_idp_identityproviders_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateDebugModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
