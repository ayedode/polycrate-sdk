from typing import Literal

ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_blocks_run_discovery_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
