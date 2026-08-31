from typing import Literal

ApiV1CertificatesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_CERTIFICATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_certificates_list_organizations_error_component_attr(
    value: str,
) -> ApiV1CertificatesListOrganizationsErrorComponentAttr:
    if value in API_V1_CERTIFICATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
