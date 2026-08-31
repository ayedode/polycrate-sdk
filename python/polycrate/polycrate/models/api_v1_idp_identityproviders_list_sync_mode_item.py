from typing import Literal

ApiV1IdpIdentityprovidersListSyncModeItem = Literal["disabled", "full", "pull", "push"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ITEM_VALUES: set[ApiV1IdpIdentityprovidersListSyncModeItem] = {
    "disabled",
    "full",
    "pull",
    "push",
}


def check_api_v1_idp_identityproviders_list_sync_mode_item(value: str) -> ApiV1IdpIdentityprovidersListSyncModeItem:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_SYNC_MODE_ITEM_VALUES!r}"
    )
