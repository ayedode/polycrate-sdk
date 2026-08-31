from typing import Literal

ApiV1BlocksRunDiscoveryCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_run_discovery_create_labels_error_component_code(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
