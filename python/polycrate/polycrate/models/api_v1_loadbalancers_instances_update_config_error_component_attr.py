from typing import Literal

ApiV1LoadbalancersInstancesUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_LOADBALANCERS_INSTANCES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_loadbalancers_instances_update_config_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesUpdateConfigErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
