from typing import Literal

ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_condition_instances_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
