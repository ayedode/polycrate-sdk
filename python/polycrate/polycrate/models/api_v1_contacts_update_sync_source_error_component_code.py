from typing import Literal

ApiV1ContactsUpdateSyncSourceErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ContactsUpdateSyncSourceErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_update_sync_source_error_component_code(
    value: str,
) -> ApiV1ContactsUpdateSyncSourceErrorComponentCode:
    if value in API_V1_CONTACTS_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
