from typing import Literal

ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_domains_domains_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
