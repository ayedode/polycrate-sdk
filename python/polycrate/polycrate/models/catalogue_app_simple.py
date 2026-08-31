from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CatalogueAppSimple")


@_attrs_define
class CatalogueAppSimple:
    """Simple serializer for embedding CatalogueApp in other serializers (e.g. dependencies).

    Attributes:
        id (UUID):
        name (str):
        display_name (None | str): The display name is used to display the object in the UI. It can be different from
            the name.
        url (str):
        serial_number (int): Serial number from app catalogue (S/N)
        draft (bool): Draft apps are not visible in the public catalogue
        is_new (bool): Highlight as new app in the catalogue
        supports_ha (bool): Whether HA (zero-downtime) deployment mode is supported for this app. Mirrors
            block.SupportsHA (CLI YAML: supports_ha).
        screenshot_url (str):
    """

    id: UUID
    name: str
    display_name: None | str
    url: str
    serial_number: int
    draft: bool
    is_new: bool
    supports_ha: bool
    screenshot_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        url = self.url

        serial_number = self.serial_number

        draft = self.draft

        is_new = self.is_new

        supports_ha = self.supports_ha

        screenshot_url = self.screenshot_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "url": url,
                "serial_number": serial_number,
                "draft": draft,
                "is_new": is_new,
                "supports_ha": supports_ha,
                "screenshot_url": screenshot_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        url = d.pop("url")

        serial_number = d.pop("serial_number")

        draft = d.pop("draft")

        is_new = d.pop("is_new")

        supports_ha = d.pop("supports_ha")

        screenshot_url = d.pop("screenshot_url")

        catalogue_app_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            url=url,
            serial_number=serial_number,
            draft=draft,
            is_new=is_new,
            supports_ha=supports_ha,
            screenshot_url=screenshot_url,
        )

        catalogue_app_simple.additional_properties = d
        return catalogue_app_simple

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
