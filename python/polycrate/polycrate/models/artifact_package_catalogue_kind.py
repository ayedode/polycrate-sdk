from typing import Literal

ArtifactPackageCatalogueKind = Literal["docker", "helm", "oci", "polycrate", "source"]

ARTIFACT_PACKAGE_CATALOGUE_KIND_VALUES: set[ArtifactPackageCatalogueKind] = {
    "docker",
    "helm",
    "oci",
    "polycrate",
    "source",
}


def check_artifact_package_catalogue_kind(value: str) -> ArtifactPackageCatalogueKind:
    if value in ARTIFACT_PACKAGE_CATALOGUE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ARTIFACT_PACKAGE_CATALOGUE_KIND_VALUES!r}")
