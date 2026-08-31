from typing import Literal

ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentAttr = Literal["sync_mode"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentAttr
] = {
    "sync_mode",
}


def check_api_v1_idp_identityproviders_create_sync_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateSyncModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
