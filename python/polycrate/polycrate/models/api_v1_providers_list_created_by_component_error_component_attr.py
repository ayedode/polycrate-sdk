from typing import Literal

ApiV1ProvidersListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_PROVIDERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_providers_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1ProvidersListCreatedByComponentErrorComponentAttr:
    if value in API_V1_PROVIDERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
