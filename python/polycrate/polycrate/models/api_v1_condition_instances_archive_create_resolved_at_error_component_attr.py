from typing import Literal

ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentAttr = Literal["resolved_at"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentAttr
] = {
    "resolved_at",
}


def check_api_v1_condition_instances_archive_create_resolved_at_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
