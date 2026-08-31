from typing import Literal

ApiV1EndpointsUpdateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null"]

API_V1_ENDPOINTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
}


def check_api_v1_endpoints_update_organization_id_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
