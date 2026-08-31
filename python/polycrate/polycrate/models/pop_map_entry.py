from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pop_map_entry_provider_type_0 import PopMapEntryProviderType0
    from ..models.pop_map_entry_workspaces_item import PopMapEntryWorkspacesItem


T = TypeVar("T", bound="PopMapEntry")


@_attrs_define
class PopMapEntry:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (str):
        url (str):
        latitude (float):
        longitude (float):
        city (None | str):
        country (None | str):
        region (None | str):
        provider (None | PopMapEntryProviderType0):
        workspace_count (int):
        workspaces (list[PopMapEntryWorkspacesItem]):
    """

    id: UUID
    name: str
    display_name: str
    url: str
    latitude: float
    longitude: float
    city: None | str
    country: None | str
    region: None | str
    provider: None | PopMapEntryProviderType0
    workspace_count: int
    workspaces: list[PopMapEntryWorkspacesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pop_map_entry_provider_type_0 import PopMapEntryProviderType0

        id = str(self.id)

        name = self.name

        display_name = self.display_name

        url = self.url

        latitude = self.latitude

        longitude = self.longitude

        city: None | str
        city = self.city

        country: None | str
        country = self.country

        region: None | str
        region = self.region

        provider: dict[str, Any] | None
        if isinstance(self.provider, PopMapEntryProviderType0):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        workspace_count = self.workspace_count

        workspaces = []
        for workspaces_item_data in self.workspaces:
            workspaces_item = workspaces_item_data.to_dict()
            workspaces.append(workspaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "url": url,
                "latitude": latitude,
                "longitude": longitude,
                "city": city,
                "country": country,
                "region": region,
                "provider": provider,
                "workspace_count": workspace_count,
                "workspaces": workspaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pop_map_entry_provider_type_0 import PopMapEntryProviderType0
        from ..models.pop_map_entry_workspaces_item import PopMapEntryWorkspacesItem

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        display_name = d.pop("display_name")

        url = d.pop("url")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_region(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        region = _parse_region(d.pop("region"))

        def _parse_provider(data: object) -> None | PopMapEntryProviderType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = PopMapEntryProviderType0.from_dict(data)

                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopMapEntryProviderType0, data)

        provider = _parse_provider(d.pop("provider"))

        workspace_count = d.pop("workspace_count")

        workspaces = []
        _workspaces = d.pop("workspaces")
        for workspaces_item_data in _workspaces:
            workspaces_item = PopMapEntryWorkspacesItem.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        pop_map_entry = cls(
            id=id,
            name=name,
            display_name=display_name,
            url=url,
            latitude=latitude,
            longitude=longitude,
            city=city,
            country=country,
            region=region,
            provider=provider,
            workspace_count=workspace_count,
            workspaces=workspaces,
        )

        pop_map_entry.additional_properties = d
        return pop_map_entry

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
