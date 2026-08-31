from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_idp_identityproviders_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
