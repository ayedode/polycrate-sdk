from typing import Literal

ApiV1ConditionInstancesCreateContextErrorComponentAttr = Literal["context"]

API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateContextErrorComponentAttr
] = {
    "context",
}


def check_api_v1_condition_instances_create_context_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateContextErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
