from typing import Literal

ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_endpoints_partial_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
