from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentAttr = Literal["slug"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_loadbalancers_regions_archive_create_slug_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateSlugErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
