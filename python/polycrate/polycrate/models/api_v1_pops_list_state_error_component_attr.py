from typing import Literal

ApiV1PopsListStateErrorComponentAttr = Literal["state"]

API_V1_POPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_pops_list_state_error_component_attr(value: str) -> ApiV1PopsListStateErrorComponentAttr:
    if value in API_V1_POPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
