from typing import Literal

ApiV1CertificatesUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CERTIFICATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_certificates_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
