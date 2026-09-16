from typing import Literal

ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_update_haproxy_defaults_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
