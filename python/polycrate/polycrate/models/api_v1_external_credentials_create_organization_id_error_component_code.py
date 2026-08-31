from typing import Literal

ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_external_credentials_create_organization_id_error_component_code(
    value: str,
) -> ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentCode:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
