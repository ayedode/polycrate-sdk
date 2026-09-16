from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentAttr = Literal["resource_limits"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentAttr
] = {
    "resource_limits",
}


def check_api_v1_loadbalancers_instances_partial_update_resource_limits_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateResourceLimitsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_RESOURCE_LIMITS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
