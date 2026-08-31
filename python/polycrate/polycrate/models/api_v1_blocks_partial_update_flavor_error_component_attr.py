from typing import Literal

ApiV1BlocksPartialUpdateFlavorErrorComponentAttr = Literal["flavor"]

API_V1_BLOCKS_PARTIAL_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateFlavorErrorComponentAttr
] = {
    "flavor",
}


def check_api_v1_blocks_partial_update_flavor_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateFlavorErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
