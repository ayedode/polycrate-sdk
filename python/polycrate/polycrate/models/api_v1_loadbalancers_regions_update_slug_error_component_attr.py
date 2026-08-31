from typing import Literal

ApiV1LoadbalancersRegionsUpdateSlugErrorComponentAttr = Literal["slug"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateSlugErrorComponentAttr
] = {
    "slug",
}


def check_api_v1_loadbalancers_regions_update_slug_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateSlugErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_SLUG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
