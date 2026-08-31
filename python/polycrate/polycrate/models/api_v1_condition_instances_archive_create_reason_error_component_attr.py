from typing import Literal

ApiV1ConditionInstancesArchiveCreateReasonErrorComponentAttr = Literal["reason"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateReasonErrorComponentAttr
] = {
    "reason",
}


def check_api_v1_condition_instances_archive_create_reason_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateReasonErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
