from typing import Literal

ApiV1ContactsListSearchErrorComponentAttr = Literal["search"]

API_V1_CONTACTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_contacts_list_search_error_component_attr(value: str) -> ApiV1ContactsListSearchErrorComponentAttr:
    if value in API_V1_CONTACTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
