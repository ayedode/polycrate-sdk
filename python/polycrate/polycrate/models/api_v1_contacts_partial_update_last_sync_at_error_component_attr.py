from typing import Literal

ApiV1ContactsPartialUpdateLastSyncAtErrorComponentAttr = Literal["last_sync_at"]

API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateLastSyncAtErrorComponentAttr
] = {
    "last_sync_at",
}


def check_api_v1_contacts_partial_update_last_sync_at_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateLastSyncAtErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
