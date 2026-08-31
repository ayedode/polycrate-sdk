from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_idp_identityproviders_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
