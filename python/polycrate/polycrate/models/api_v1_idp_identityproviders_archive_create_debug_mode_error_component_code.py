from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
