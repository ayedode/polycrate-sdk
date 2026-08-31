from typing import Literal

ApiV1IdpIdentityprovidersListSyncModeErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersListSyncModeErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_idp_identityproviders_list_sync_mode_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersListSyncModeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
