from typing import Literal

ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_alertrouters_archive_create_organization_id_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateOrganizationIdErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
