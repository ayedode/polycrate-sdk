from typing import Literal

ApiV1ContactsCreateLastSyncAtErrorComponentAttr = Literal["last_sync_at"]

API_V1_CONTACTS_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsCreateLastSyncAtErrorComponentAttr
] = {
    "last_sync_at",
}


def check_api_v1_contacts_create_last_sync_at_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateLastSyncAtErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_LAST_SYNC_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
