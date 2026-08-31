from typing import Literal

ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_blocks_run_discovery_create_created_by_brc_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
