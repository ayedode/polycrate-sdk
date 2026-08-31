from typing import Literal

ApiV1ConditionInstancesArchiveCreateContextErrorComponentAttr = Literal["context"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateContextErrorComponentAttr
] = {
    "context",
}


def check_api_v1_condition_instances_archive_create_context_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateContextErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
