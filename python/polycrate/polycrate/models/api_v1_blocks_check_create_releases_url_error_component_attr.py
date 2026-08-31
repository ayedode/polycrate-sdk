from typing import Literal

ApiV1BlocksCheckCreateReleasesUrlErrorComponentAttr = Literal["releases_url"]

API_V1_BLOCKS_CHECK_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateReleasesUrlErrorComponentAttr
] = {
    "releases_url",
}


def check_api_v1_blocks_check_create_releases_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateReleasesUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_RELEASES_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
