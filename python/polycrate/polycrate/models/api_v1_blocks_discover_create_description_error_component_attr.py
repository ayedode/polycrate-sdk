from typing import Literal

ApiV1BlocksDiscoverCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_BLOCKS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_blocks_discover_create_description_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateDescriptionErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
