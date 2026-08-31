from typing import Literal

ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_idp_identityproviders_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
