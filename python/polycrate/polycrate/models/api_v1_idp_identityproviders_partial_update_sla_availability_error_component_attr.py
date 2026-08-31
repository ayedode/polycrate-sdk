from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_idp_identityproviders_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
