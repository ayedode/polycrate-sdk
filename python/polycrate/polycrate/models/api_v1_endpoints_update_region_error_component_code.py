from typing import Literal

ApiV1EndpointsUpdateRegionErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsUpdateRegionErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_update_region_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateRegionErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_REGION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
