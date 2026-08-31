from typing import Literal

ApiV1BlocksPartialUpdateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateRegistryUrlErrorComponentAttr
] = {
    "registry_url",
}


def check_api_v1_blocks_partial_update_registry_url_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateRegistryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
