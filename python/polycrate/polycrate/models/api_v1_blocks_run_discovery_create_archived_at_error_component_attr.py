from typing import Literal

ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_blocks_run_discovery_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
