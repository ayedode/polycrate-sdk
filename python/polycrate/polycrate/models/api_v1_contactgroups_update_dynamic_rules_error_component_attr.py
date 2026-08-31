from typing import Literal

ApiV1ContactgroupsUpdateDynamicRulesErrorComponentAttr = Literal["dynamic_rules"]

API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsUpdateDynamicRulesErrorComponentAttr
] = {
    "dynamic_rules",
}


def check_api_v1_contactgroups_update_dynamic_rules_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsUpdateDynamicRulesErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
