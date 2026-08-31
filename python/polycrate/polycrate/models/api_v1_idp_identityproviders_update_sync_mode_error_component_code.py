from typing import Literal

ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_idp_identityproviders_update_sync_mode_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
