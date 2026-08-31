from typing import Literal

ApiV1ContactgroupsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_contactgroups_list_state_not_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsListStateNotErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
