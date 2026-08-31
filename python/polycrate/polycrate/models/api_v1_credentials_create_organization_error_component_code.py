from typing import Literal

ApiV1CredentialsCreateOrganizationErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsCreateOrganizationErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_credentials_create_organization_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateOrganizationErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
