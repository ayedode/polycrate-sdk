from typing import Literal

ApiV1PopsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_POPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsListCreatedAtErrorComponentAttr] = {
    "created_at",
}


def check_api_v1_pops_list_created_at_error_component_attr(value: str) -> ApiV1PopsListCreatedAtErrorComponentAttr:
    if value in API_V1_POPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
