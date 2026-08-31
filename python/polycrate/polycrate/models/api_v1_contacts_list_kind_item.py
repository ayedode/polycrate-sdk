from typing import Literal

ApiV1ContactsListKindItem = Literal["generic"]

API_V1_CONTACTS_LIST_KIND_ITEM_VALUES: set[ApiV1ContactsListKindItem] = {
    "generic",
}


def check_api_v1_contacts_list_kind_item(value: str) -> ApiV1ContactsListKindItem:
    if value in API_V1_CONTACTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_KIND_ITEM_VALUES!r}")
