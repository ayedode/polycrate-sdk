from typing import Literal

ApiV1PrefixesListStateErrorComponentAttr = Literal["state"]

API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_prefixes_list_state_error_component_attr(value: str) -> ApiV1PrefixesListStateErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
