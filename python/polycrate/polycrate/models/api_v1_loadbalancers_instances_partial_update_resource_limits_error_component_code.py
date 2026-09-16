from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_partial_update_resource_limits_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
