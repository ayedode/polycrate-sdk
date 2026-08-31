from typing import Literal

ApiV1BlocksCreateReleasesUrlErrorComponentAttr = Literal["releases_url"]

API_V1_BLOCKS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateReleasesUrlErrorComponentAttr] = {
    "releases_url",
}


def check_api_v1_blocks_create_releases_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateReleasesUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
