from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogueAppDetailTemplateBlockDetailType0")


@_attrs_define
class CatalogueAppDetailTemplateBlockDetailType0:
    """
    Attributes:
        id (UUID | Unset):
        registry_url (str | Unset):
        version (None | str | Unset):
        app_version (None | str | Unset):
        license_ (None | str | Unset):
        license_url (None | str | Unset):
        website_url (None | str | Unset):
        git_repository_url (None | str | Unset):
        documentation_url (None | str | Unset):
        releases_url (None | str | Unset):
        icon_url (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    registry_url: str | Unset = UNSET
    version: None | str | Unset = UNSET
    app_version: None | str | Unset = UNSET
    license_: None | str | Unset = UNSET
    license_url: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    git_repository_url: None | str | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    releases_url: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        registry_url = self.registry_url

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        app_version: None | str | Unset
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

        license_: None | str | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        else:
            license_ = self.license_

        license_url: None | str | Unset
        if isinstance(self.license_url, Unset):
            license_url = UNSET
        else:
            license_url = self.license_url

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        git_repository_url: None | str | Unset
        if isinstance(self.git_repository_url, Unset):
            git_repository_url = UNSET
        else:
            git_repository_url = self.git_repository_url

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        releases_url: None | str | Unset
        if isinstance(self.releases_url, Unset):
            releases_url = UNSET
        else:
            releases_url = self.releases_url

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if version is not UNSET:
            field_dict["version"] = version
        if app_version is not UNSET:
            field_dict["app_version"] = app_version
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_url is not UNSET:
            field_dict["license_url"] = license_url
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if git_repository_url is not UNSET:
            field_dict["git_repository_url"] = git_repository_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if releases_url is not UNSET:
            field_dict["releases_url"] = releases_url
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        registry_url = d.pop("registry_url", UNSET)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_app_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_version = _parse_app_version(d.pop("app_version", UNSET))

        def _parse_license_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_license_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_url = _parse_license_url(d.pop("license_url", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_git_repository_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_repository_url = _parse_git_repository_url(d.pop("git_repository_url", UNSET))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        def _parse_releases_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        releases_url = _parse_releases_url(d.pop("releases_url", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        catalogue_app_detail_template_block_detail_type_0 = cls(
            id=id,
            registry_url=registry_url,
            version=version,
            app_version=app_version,
            license_=license_,
            license_url=license_url,
            website_url=website_url,
            git_repository_url=git_repository_url,
            documentation_url=documentation_url,
            releases_url=releases_url,
            icon_url=icon_url,
        )

        catalogue_app_detail_template_block_detail_type_0.additional_properties = d
        return catalogue_app_detail_template_block_detail_type_0

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
