from typing import Literal

ApiV1ConditionInstancesArchiveCreateImmediateErrorComponentAttr = Literal["immediate"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateImmediateErrorComponentAttr
] = {
    "immediate",
}


def check_api_v1_condition_instances_archive_create_immediate_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateImmediateErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_IMMEDIATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
