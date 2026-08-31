from typing import Literal

ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_external_credentials_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1ExternalCredentialsCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
