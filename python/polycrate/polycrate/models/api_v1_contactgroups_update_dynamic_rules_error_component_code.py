from typing import Literal

ApiV1ContactgroupsUpdateDynamicRulesErrorComponentCode = Literal["invalid"]

API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ContactgroupsUpdateDynamicRulesErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_contactgroups_update_dynamic_rules_error_component_code(
    value: str,
) -> ApiV1ContactgroupsUpdateDynamicRulesErrorComponentCode:
    if value in API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
