from typing import Literal

ApiV1BlocksRunDiscoveryCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_blocks_run_discovery_create_kind_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateKindErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
