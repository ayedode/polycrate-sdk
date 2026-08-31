from typing import Literal

ApiV1PrefixesListKindErrorComponentAttr = Literal["kind"]

API_V1_PREFIXES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_prefixes_list_kind_error_component_attr(value: str) -> ApiV1PrefixesListKindErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
