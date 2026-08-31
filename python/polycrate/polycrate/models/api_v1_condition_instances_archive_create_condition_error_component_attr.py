from typing import Literal

ApiV1ConditionInstancesArchiveCreateConditionErrorComponentAttr = Literal["condition"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateConditionErrorComponentAttr
] = {
    "condition",
}


def check_api_v1_condition_instances_archive_create_condition_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateConditionErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONDITION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
