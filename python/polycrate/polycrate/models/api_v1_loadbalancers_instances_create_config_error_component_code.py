from typing import Literal

ApiV1LoadbalancersInstancesCreateConfigErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_LOADBALANCERS_INSTANCES_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesCreateConfigErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_loadbalancers_instances_create_config_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesCreateConfigErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_CREATE_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
