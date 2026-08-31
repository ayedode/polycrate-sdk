from typing import Literal

ApiV1EndpointsCreateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null"]

API_V1_ENDPOINTS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
}


def check_api_v1_endpoints_create_organization_id_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateOrganizationIdErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
