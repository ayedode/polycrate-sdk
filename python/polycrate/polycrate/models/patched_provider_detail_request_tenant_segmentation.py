from typing import Literal

PatchedProviderDetailRequestTenantSegmentation = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES: set[PatchedProviderDetailRequestTenantSegmentation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_tenant_segmentation(
    value: str,
) -> PatchedProviderDetailRequestTenantSegmentation:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES!r}"
    )
