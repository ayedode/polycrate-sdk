from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentAttr = Literal["haproxy_defaults"]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentAttr
] = {
    "haproxy_defaults",
}


def check_api_v1_loadbalancers_instances_partial_update_haproxy_defaults_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateHaproxyDefaultsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
