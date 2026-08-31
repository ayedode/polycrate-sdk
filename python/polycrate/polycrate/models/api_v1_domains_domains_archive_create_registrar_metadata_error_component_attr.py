from typing import Literal

ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponentAttr = Literal["registrar_metadata"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponentAttr
] = {
    "registrar_metadata",
}


def check_api_v1_domains_domains_archive_create_registrar_metadata_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
