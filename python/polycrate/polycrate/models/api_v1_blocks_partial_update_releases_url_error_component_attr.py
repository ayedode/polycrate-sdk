from typing import Literal

ApiV1BlocksPartialUpdateReleasesUrlErrorComponentAttr = Literal["releases_url"]

API_V1_BLOCKS_PARTIAL_UPDATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateReleasesUrlErrorComponentAttr
] = {
    "releases_url",
}


def check_api_v1_blocks_partial_update_releases_url_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateReleasesUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
