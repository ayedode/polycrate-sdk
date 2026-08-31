from typing import Literal

ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_blocks_run_discovery_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
