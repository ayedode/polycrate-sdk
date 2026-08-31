from typing import Literal

ApiV1EndpointsPartialUpdateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsPartialUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
}


def check_api_v1_endpoints_partial_update_organization_id_error_component_code(
    value: str,
) -> ApiV1EndpointsPartialUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
