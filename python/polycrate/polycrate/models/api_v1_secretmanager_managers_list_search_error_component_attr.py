from typing import Literal

ApiV1SecretmanagerManagersListSearchErrorComponentAttr = Literal["search"]

API_V1_SECRETMANAGER_MANAGERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_secretmanager_managers_list_search_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListSearchErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
