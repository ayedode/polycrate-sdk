from typing import Literal

ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentAttr = Literal["haproxy_defaults"]

API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentAttr
] = {
    "haproxy_defaults",
}


def check_api_v1_loadbalancers_instances_create_haproxy_defaults_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateHaproxyDefaultsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_HAPROXY_DEFAULTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
