from typing import Literal

ApiV1ProvidersUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_providers_update_name_error_component_attr(value: str) -> ApiV1ProvidersUpdateNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
