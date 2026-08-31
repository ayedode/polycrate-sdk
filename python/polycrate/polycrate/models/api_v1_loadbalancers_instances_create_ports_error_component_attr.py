from typing import Literal

ApiV1LoadbalancersInstancesCreatePortsErrorComponentAttr = Literal["ports"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreatePortsErrorComponentAttr
] = {
    "ports",
}


def check_api_v1_loadbalancers_instances_create_ports_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreatePortsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
