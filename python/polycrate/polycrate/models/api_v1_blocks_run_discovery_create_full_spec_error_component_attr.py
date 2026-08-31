from typing import Literal

ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponentAttr
] = {
    "full_spec",
}


def check_api_v1_blocks_run_discovery_create_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
