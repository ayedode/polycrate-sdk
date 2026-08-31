from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponentAttr = Literal["sync_mode"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponentAttr
] = {
    "sync_mode",
}


def check_api_v1_idp_identityproviders_partial_update_sync_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
