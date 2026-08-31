from typing import Literal

ApiV1ConditionInstancesListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_CONDITION_INSTANCES_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesListOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_condition_instances_list_organization_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesListOrganizationErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
