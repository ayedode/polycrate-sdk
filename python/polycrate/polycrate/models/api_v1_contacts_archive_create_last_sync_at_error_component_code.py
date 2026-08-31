from typing import Literal

ApiV1ContactsArchiveCreateLastSyncAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsArchiveCreateLastSyncAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_contacts_archive_create_last_sync_at_error_component_code(
    value: str,
) -> ApiV1ContactsArchiveCreateLastSyncAtErrorComponentCode:
    if value in API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_ARCHIVE_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
