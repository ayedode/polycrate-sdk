from typing import Literal

ApiV1CertificatesSyncCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesSyncCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_certificates_sync_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1CertificatesSyncCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_SYNC_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
