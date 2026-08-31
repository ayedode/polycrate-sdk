from typing import Literal

ApiV1ConditionInstancesUpdateContextErrorComponentAttr = Literal["context"]

API_V1_CONDITION_INSTANCES_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesUpdateContextErrorComponentAttr
] = {
    "context",
}


def check_api_v1_condition_instances_update_context_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesUpdateContextErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_UPDATE_CONTEXT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
