from typing import Literal

ApiV1BlocksRunDiscoveryCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_blocks_run_discovery_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
