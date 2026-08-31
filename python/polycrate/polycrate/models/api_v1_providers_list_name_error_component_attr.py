from typing import Literal

ApiV1ProvidersListNameErrorComponentAttr = Literal["name"]

API_V1_PROVIDERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_providers_list_name_error_component_attr(value: str) -> ApiV1ProvidersListNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
