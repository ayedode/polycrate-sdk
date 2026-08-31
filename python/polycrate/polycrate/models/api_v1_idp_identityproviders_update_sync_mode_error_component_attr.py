from typing import Literal

ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentAttr = Literal["sync_mode"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentAttr
] = {
    "sync_mode",
}


def check_api_v1_idp_identityproviders_update_sync_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
