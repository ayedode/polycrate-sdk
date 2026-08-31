from typing import Literal

ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_condition_instances_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
