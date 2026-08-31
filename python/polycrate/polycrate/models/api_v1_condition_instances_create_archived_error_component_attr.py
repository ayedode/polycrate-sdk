from typing import Literal

ApiV1ConditionInstancesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_CONDITION_INSTANCES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_condition_instances_create_archived_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateArchivedErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
