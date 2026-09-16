from typing import Literal

ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_create_haproxy_defaults_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
