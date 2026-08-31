from typing import Literal

ApiV1ContactsPartialUpdateSyncSourceErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactsPartialUpdateSyncSourceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_contacts_partial_update_sync_source_error_component_code(
    value: str,
) -> ApiV1ContactsPartialUpdateSyncSourceErrorComponentCode:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
