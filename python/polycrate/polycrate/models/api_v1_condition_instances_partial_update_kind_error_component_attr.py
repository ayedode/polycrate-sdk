from typing import Literal

ApiV1ConditionInstancesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionInstancesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_condition_instances_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1ConditionInstancesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITION_INSTANCES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
