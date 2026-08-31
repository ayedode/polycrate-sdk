from typing import Literal

ApiV1ConditionInstancesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_condition_instances_create_kind_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesCreateKindErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
