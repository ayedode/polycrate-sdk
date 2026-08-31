from typing import Literal

ApiV1PrefixesListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_PREFIXES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PrefixesListStateNotErrorComponentAttr] = {
    "state_not",
}


def check_api_v1_prefixes_list_state_not_error_component_attr(
    value: str,
) -> ApiV1PrefixesListStateNotErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
