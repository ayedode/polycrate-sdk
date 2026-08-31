from typing import Literal

ApiV1LoadbalancersInstancesCreatePortsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesCreatePortsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_create_ports_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesCreatePortsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_PORTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
