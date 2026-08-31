from typing import Literal

ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_condition_instances_archive_create_resolved_at_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateResolvedAtErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_RESOLVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
