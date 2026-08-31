from typing import Literal

ApiV1PopsListKindErrorComponentAttr = Literal["kind"]

API_V1_POPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pops_list_kind_error_component_attr(value: str) -> ApiV1PopsListKindErrorComponentAttr:
    if value in API_V1_POPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
