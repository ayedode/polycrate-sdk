from typing import Literal

ApiV1ContactsPartialUpdateSyncSourceErrorComponentAttr = Literal["sync_source"]

API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsPartialUpdateSyncSourceErrorComponentAttr
] = {
    "sync_source",
}


def check_api_v1_contacts_partial_update_sync_source_error_component_attr(
    value: str,
) -> ApiV1ContactsPartialUpdateSyncSourceErrorComponentAttr:
    if value in API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_PARTIAL_UPDATE_SYNC_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
