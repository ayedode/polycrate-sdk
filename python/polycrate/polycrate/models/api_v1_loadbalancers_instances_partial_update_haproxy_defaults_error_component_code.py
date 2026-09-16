from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_instances_partial_update_haproxy_defaults_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
