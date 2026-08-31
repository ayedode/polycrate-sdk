from typing import Literal

ApiV1ContactgroupsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_contactgroups_list_state_not_error_component_code(
    value: str,
) -> ApiV1ContactgroupsListStateNotErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
