from typing import Literal

ApiV1ContactsUpdateLastSyncAtErrorComponentAttr = Literal["last_sync_at"]

API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsUpdateLastSyncAtErrorComponentAttr
] = {
    "last_sync_at",
}


def check_api_v1_contacts_update_last_sync_at_error_component_attr(
    value: str,
) -> ApiV1ContactsUpdateLastSyncAtErrorComponentAttr:
    if value in API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
