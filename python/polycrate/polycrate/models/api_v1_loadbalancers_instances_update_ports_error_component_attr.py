from typing import Literal

ApiV1LoadbalancersInstancesUpdatePortsErrorComponentAttr = Literal["ports"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_PORTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesUpdatePortsErrorComponentAttr
] = {
    "ports",
}


def check_api_v1_loadbalancers_instances_update_ports_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdatePortsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_PORTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_PORTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
