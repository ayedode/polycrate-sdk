from typing import Literal

ApiV1ProvidersUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PROVIDERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_providers_update_display_name_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
