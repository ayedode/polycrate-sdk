from typing import Literal

ApiV1CredentialsCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_credentials_create_organization_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateOrganizationErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
