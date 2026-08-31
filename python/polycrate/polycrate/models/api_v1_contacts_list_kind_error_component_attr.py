from typing import Literal

ApiV1ContactsListKindErrorComponentAttr = Literal["kind"]

API_V1_CONTACTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_contacts_list_kind_error_component_attr(value: str) -> ApiV1ContactsListKindErrorComponentAttr:
    if value in API_V1_CONTACTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
