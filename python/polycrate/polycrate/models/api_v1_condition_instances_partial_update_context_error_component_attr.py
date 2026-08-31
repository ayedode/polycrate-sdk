from typing import Literal

ApiV1ConditionInstancesPartialUpdateContextErrorComponentAttr = Literal["context"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateContextErrorComponentAttr
] = {
    "context",
}


def check_api_v1_condition_instances_partial_update_context_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateContextErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
