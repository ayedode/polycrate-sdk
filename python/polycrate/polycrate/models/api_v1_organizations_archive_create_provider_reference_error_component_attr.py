from typing import Literal

ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_organizations_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
