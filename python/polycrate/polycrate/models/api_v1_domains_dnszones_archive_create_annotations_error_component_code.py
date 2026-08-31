from typing import Literal

ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
