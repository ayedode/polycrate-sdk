from typing import Literal

ApiV1ApmApmstacksListStateErrorComponentAttr = Literal["state"]

API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ApmApmstacksListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_apm_apmstacks_list_state_error_component_attr(
    value: str,
) -> ApiV1ApmApmstacksListStateErrorComponentAttr:
    if value in API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
