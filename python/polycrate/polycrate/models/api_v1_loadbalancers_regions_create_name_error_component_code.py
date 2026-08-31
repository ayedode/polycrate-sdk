from typing import Literal

ApiV1LoadbalancersRegionsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_loadbalancers_regions_create_name_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateNameErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
