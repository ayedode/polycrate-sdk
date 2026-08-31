from typing import Literal

ApiV1BlocksCreateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_BLOCKS_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateRegistryUrlErrorComponentAttr] = {
    "registry_url",
}


def check_api_v1_blocks_create_registry_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateRegistryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
