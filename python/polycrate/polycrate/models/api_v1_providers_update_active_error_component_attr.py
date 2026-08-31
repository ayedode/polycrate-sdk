from typing import Literal

ApiV1ProvidersUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1_providers_update_active_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateActiveErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
