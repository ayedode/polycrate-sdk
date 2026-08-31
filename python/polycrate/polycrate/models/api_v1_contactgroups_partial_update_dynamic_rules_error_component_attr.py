from typing import Literal

ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponentAttr = Literal["dynamic_rules"]

API_V1_CONTACTGROUPS_PARTIAL_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponentAttr
] = {
    "dynamic_rules",
}


def check_api_v1_contactgroups_partial_update_dynamic_rules_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsPartialUpdateDynamicRulesErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_PARTIAL_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_PARTIAL_UPDATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
