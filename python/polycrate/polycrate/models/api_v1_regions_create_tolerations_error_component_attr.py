from typing import Literal

ApiV1RegionsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_REGIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsCreateTolerationsErrorComponentAttr] = {
    "tolerations",
}


def check_api_v1_regions_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1RegionsCreateTolerationsErrorComponentAttr:
    if value in API_V1_REGIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
