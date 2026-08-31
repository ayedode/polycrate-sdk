from typing import Literal

ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentAttr = Literal["created_by_brc"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentAttr
] = {
    "created_by_brc",
}


def check_api_v1_blocks_run_discovery_create_created_by_brc_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateCreatedByBrcErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
