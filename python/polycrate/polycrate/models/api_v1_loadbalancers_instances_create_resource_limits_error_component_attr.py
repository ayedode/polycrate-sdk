from typing import Literal

ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentAttr = Literal["resource_limits"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentAttr
] = {
    "resource_limits",
}


def check_api_v1_loadbalancers_instances_create_resource_limits_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateResourceLimitsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
