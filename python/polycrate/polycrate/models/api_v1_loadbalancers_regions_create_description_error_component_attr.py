from typing import Literal

ApiV1LoadbalancersRegionsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_LOADBALANCERS_REGIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_loadbalancers_regions_create_description_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateDescriptionErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
