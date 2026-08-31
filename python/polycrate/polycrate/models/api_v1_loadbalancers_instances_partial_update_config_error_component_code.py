from typing import Literal

ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_loadbalancers_instances_partial_update_config_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesPartialUpdateConfigErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_PARTIAL_UPDATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
