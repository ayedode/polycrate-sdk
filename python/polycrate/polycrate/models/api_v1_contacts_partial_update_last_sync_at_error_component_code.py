from typing import Literal

ApiV1ContactsPartialUpdateLastSyncAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsPartialUpdateLastSyncAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_contacts_partial_update_last_sync_at_error_component_code(
    value: str,
) -> ApiV1ContactsPartialUpdateLastSyncAtErrorComponentCode:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
