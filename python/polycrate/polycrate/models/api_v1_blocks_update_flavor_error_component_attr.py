from typing import Literal

ApiV1BlocksUpdateFlavorErrorComponentAttr = Literal["flavor"]

API_V1_BLOCKS_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateFlavorErrorComponentAttr] = {
    "flavor",
}


def check_api_v1_blocks_update_flavor_error_component_attr(value: str) -> ApiV1BlocksUpdateFlavorErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
