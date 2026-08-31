from typing import Literal

ApiV1ProvidersPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_providers_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
