from typing import Literal

ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_dnszones_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
