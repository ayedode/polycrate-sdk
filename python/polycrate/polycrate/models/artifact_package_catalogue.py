from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artifact_kind_enum import ArtifactKindEnum, check_artifact_kind_enum

if TYPE_CHECKING:
    from ..models.artifact_package_catalogue_latest_changelog_parsed import (
        ArtifactPackageCatalogueLatestChangelogParsed,
    )
    from ..models.artifact_package_catalogue_latest_source_urls import ArtifactPackageCatalogueLatestSourceUrls
    from ..models.artifact_repository_simple import ArtifactRepositorySimple


T = TypeVar("T", bound="ArtifactPackageCatalogue")


@_attrs_define
class ArtifactPackageCatalogue:
    """Rich ArtifactPackage serializer for CatalogueApp / catalogue context.

    Uses ``ArtifactDerivedFieldsMixin`` to transparently expose metadata
    (version, license, changelog, readme …) from the latest Artifact of
    the package - or from a specifically requested one when
    ``_artifact_override`` is set in the serializer context.

    Per .specs/0.12.0/catalogue-app.md

        Attributes:
            id (UUID):
            name (str):
            display_name (None | str): The display name is used to display the object in the UI. It can be different from
                the name.
            kind (ArtifactKindEnum): * `helm` - Helm
                * `docker` - Docker
                * `polycrate` - Polycrate
                * `oci` - OCI
                * `source` - Source Code
            url (str):
            icon_url (None | str):
            artifact_repository (ArtifactRepositorySimple): Simple serializer for embedding ArtifactRepository in other
                serializers.
            artifact_count (int):
            created_at (datetime.datetime):
            latest_version (str):
            latest_app_version (str):
            latest_license (str):
            latest_website_url (str):
            latest_content_url (str):
            latest_source_urls (ArtifactPackageCatalogueLatestSourceUrls):
            latest_readme_md (str):
            latest_changelog (str):
            latest_changelog_parsed (ArtifactPackageCatalogueLatestChangelogParsed):
            latest_artifact_id (UUID):
    """

    id: UUID
    name: str
    display_name: None | str
    kind: ArtifactKindEnum
    url: str
    icon_url: None | str
    artifact_repository: ArtifactRepositorySimple
    artifact_count: int
    created_at: datetime.datetime
    latest_version: str
    latest_app_version: str
    latest_license: str
    latest_website_url: str
    latest_content_url: str
    latest_source_urls: ArtifactPackageCatalogueLatestSourceUrls
    latest_readme_md: str
    latest_changelog: str
    latest_changelog_parsed: ArtifactPackageCatalogueLatestChangelogParsed
    latest_artifact_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        kind: str = self.kind

        url = self.url

        icon_url: None | str
        icon_url = self.icon_url

        artifact_repository = self.artifact_repository.to_dict()

        artifact_count = self.artifact_count

        created_at = self.created_at.isoformat()

        latest_version = self.latest_version

        latest_app_version = self.latest_app_version

        latest_license = self.latest_license

        latest_website_url = self.latest_website_url

        latest_content_url = self.latest_content_url

        latest_source_urls = self.latest_source_urls.to_dict()

        latest_readme_md = self.latest_readme_md

        latest_changelog = self.latest_changelog

        latest_changelog_parsed = self.latest_changelog_parsed.to_dict()

        latest_artifact_id = str(self.latest_artifact_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "kind": kind,
                "url": url,
                "icon_url": icon_url,
                "artifact_repository": artifact_repository,
                "artifact_count": artifact_count,
                "created_at": created_at,
                "latest_version": latest_version,
                "latest_app_version": latest_app_version,
                "latest_license": latest_license,
                "latest_website_url": latest_website_url,
                "latest_content_url": latest_content_url,
                "latest_source_urls": latest_source_urls,
                "latest_readme_md": latest_readme_md,
                "latest_changelog": latest_changelog,
                "latest_changelog_parsed": latest_changelog_parsed,
                "latest_artifact_id": latest_artifact_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact_package_catalogue_latest_changelog_parsed import (
            ArtifactPackageCatalogueLatestChangelogParsed,
        )
        from ..models.artifact_package_catalogue_latest_source_urls import ArtifactPackageCatalogueLatestSourceUrls
        from ..models.artifact_repository_simple import ArtifactRepositorySimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        kind = check_artifact_kind_enum(d.pop("kind"))

        url = d.pop("url")

        def _parse_icon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_url = _parse_icon_url(d.pop("icon_url"))

        artifact_repository = ArtifactRepositorySimple.from_dict(d.pop("artifact_repository"))

        artifact_count = d.pop("artifact_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        latest_version = d.pop("latest_version")

        latest_app_version = d.pop("latest_app_version")

        latest_license = d.pop("latest_license")

        latest_website_url = d.pop("latest_website_url")

        latest_content_url = d.pop("latest_content_url")

        latest_source_urls = ArtifactPackageCatalogueLatestSourceUrls.from_dict(d.pop("latest_source_urls"))

        latest_readme_md = d.pop("latest_readme_md")

        latest_changelog = d.pop("latest_changelog")

        latest_changelog_parsed = ArtifactPackageCatalogueLatestChangelogParsed.from_dict(
            d.pop("latest_changelog_parsed")
        )

        latest_artifact_id = UUID(d.pop("latest_artifact_id"))

        artifact_package_catalogue = cls(
            id=id,
            name=name,
            display_name=display_name,
            kind=kind,
            url=url,
            icon_url=icon_url,
            artifact_repository=artifact_repository,
            artifact_count=artifact_count,
            created_at=created_at,
            latest_version=latest_version,
            latest_app_version=latest_app_version,
            latest_license=latest_license,
            latest_website_url=latest_website_url,
            latest_content_url=latest_content_url,
            latest_source_urls=latest_source_urls,
            latest_readme_md=latest_readme_md,
            latest_changelog=latest_changelog,
            latest_changelog_parsed=latest_changelog_parsed,
            latest_artifact_id=latest_artifact_id,
        )

        artifact_package_catalogue.additional_properties = d
        return artifact_package_catalogue

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
