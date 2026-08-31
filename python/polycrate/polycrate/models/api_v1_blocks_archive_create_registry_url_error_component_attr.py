from typing import Literal

ApiV1BlocksArchiveCreateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_BLOCKS_ARCHIVE_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateRegistryUrlErrorComponentAttr
] = {
    "registry_url",
}


def check_api_v1_blocks_archive_create_registry_url_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateRegistryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
