from typing import Literal

ApiV1ApmApmstacksListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ApmApmstacksListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_apm_apmstacks_list_state_error_component_code(
    value: str,
) -> ApiV1ApmApmstacksListStateErrorComponentCode:
    if value in API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
