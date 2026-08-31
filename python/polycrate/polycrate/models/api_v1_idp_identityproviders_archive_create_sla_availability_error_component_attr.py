from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_idp_identityproviders_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
