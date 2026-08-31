from typing import Literal

ApiV1ApmApmstacksListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_APM_APMSTACKS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmApmstacksListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_apm_apmstacks_list_name_exact_error_component_code(
    value: str,
) -> ApiV1ApmApmstacksListNameExactErrorComponentCode:
    if value in API_V1_APM_APMSTACKS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
