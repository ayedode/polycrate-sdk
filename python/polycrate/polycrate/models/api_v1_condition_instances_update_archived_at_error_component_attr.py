from typing import Literal

ApiV1ConditionInstancesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_condition_instances_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
