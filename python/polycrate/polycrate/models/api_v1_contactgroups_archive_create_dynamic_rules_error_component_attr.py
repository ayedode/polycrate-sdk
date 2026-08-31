from typing import Literal

ApiV1ContactgroupsArchiveCreateDynamicRulesErrorComponentAttr = Literal["dynamic_rules"]

API_V1_CONTACTGROUPS_ARCHIVE_CREATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsArchiveCreateDynamicRulesErrorComponentAttr
] = {
    "dynamic_rules",
}


def check_api_v1_contactgroups_archive_create_dynamic_rules_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsArchiveCreateDynamicRulesErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_ARCHIVE_CREATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_ARCHIVE_CREATE_DYNAMIC_RULES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
