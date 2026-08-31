from typing import Literal

ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponentAttr = Literal["renewal_mode"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponentAttr
] = {
    "renewal_mode",
}


def check_api_v1_domains_domains_archive_create_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
