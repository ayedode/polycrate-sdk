from typing import Literal

ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_create_resource_limits_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
