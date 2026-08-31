from typing import Literal

ApiV1BlocksArchiveCreateFlavorErrorComponentAttr = Literal["flavor"]

API_V1_BLOCKS_ARCHIVE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateFlavorErrorComponentAttr
] = {
    "flavor",
}


def check_api_v1_blocks_archive_create_flavor_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateFlavorErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
