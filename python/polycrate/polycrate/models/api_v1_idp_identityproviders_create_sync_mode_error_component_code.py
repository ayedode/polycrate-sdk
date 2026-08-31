from typing import Literal

ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_idp_identityproviders_create_sync_mode_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
