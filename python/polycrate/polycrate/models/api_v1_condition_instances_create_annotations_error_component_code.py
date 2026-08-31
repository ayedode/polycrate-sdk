from typing import Literal

ApiV1ConditionInstancesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ConditionInstancesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_condition_instances_create_annotations_error_component_code(
    value: str,
) -> ApiV1ConditionInstancesCreateAnnotationsErrorComponentCode:
    if value in API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
