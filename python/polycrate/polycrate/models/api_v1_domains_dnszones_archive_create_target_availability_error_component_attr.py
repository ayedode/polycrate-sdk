from typing import Literal

ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_domains_dnszones_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
