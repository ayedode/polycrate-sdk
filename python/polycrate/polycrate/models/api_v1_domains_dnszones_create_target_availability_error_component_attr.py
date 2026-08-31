from typing import Literal

ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_DOMAINS_DNSZONES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_domains_dnszones_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
