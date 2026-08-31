from typing import Literal

ApiV1ContactsUpdateLastSyncAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsUpdateLastSyncAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_contacts_update_last_sync_at_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateLastSyncAtErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_LAST_SYNC_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
