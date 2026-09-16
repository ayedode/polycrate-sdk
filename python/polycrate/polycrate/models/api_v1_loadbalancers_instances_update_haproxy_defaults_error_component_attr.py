from typing import Literal

ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentAttr = Literal["haproxy_defaults"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentAttr
] = {
    "haproxy_defaults",
}


def check_api_v1_loadbalancers_instances_update_haproxy_defaults_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateHaproxyDefaultsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
