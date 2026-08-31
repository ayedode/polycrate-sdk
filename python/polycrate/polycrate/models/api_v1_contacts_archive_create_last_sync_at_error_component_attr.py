from typing import Literal

ApiV1ContactsArchiveCreateLastSyncAtErrorComponentAttr = Literal["last_sync_at"]

API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsArchiveCreateLastSyncAtErrorComponentAttr
] = {
    "last_sync_at",
}


def check_api_v1_contacts_archive_create_last_sync_at_error_component_attr(
    value: str,
) -> ApiV1ContactsArchiveCreateLastSyncAtErrorComponentAttr:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
