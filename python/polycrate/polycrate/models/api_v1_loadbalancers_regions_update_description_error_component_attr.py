from typing import Literal

ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_loadbalancers_regions_update_description_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateDescriptionErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
