from typing import Literal

ApiV1LoadbalancersInstancesUpdateResourceLimitsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateResourceLimitsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_update_resource_limits_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateResourceLimitsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
