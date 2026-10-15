from typing import Literal

PatchedProviderDetailRequestApiPublicDocs = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES: set[PatchedProviderDetailRequestApiPublicDocs] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_api_public_docs(value: str) -> PatchedProviderDetailRequestApiPublicDocs:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_API_PUBLIC_DOCS_VALUES!r}"
    )
