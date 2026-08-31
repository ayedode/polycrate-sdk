from typing import Literal

ApiV1IdpIdentityprovidersListSyncModeErrorComponentAttr = Literal["sync_mode"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListSyncModeErrorComponentAttr
] = {
    "sync_mode",
}


def check_api_v1_idp_identityproviders_list_sync_mode_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListSyncModeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
