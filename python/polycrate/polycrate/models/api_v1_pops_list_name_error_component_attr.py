from typing import Literal

ApiV1PopsListNameErrorComponentAttr = Literal["name"]

API_V1_POPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pops_list_name_error_component_attr(value: str) -> ApiV1PopsListNameErrorComponentAttr:
    if value in API_V1_POPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
