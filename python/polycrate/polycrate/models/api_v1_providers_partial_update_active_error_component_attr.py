from typing import Literal

ApiV1ProvidersPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_providers_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateActiveErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
